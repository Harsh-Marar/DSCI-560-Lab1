from bs4 import BeautifulSoup
import csv
import os
import re


def extract_market_data(soup):
    print("Filtering market data...")
    market_data = []

    banner = soup.find("div", class_=re.compile("MarketsBanner-marketData"))
    if not banner:
        print("Market banner not found")
        return market_data

    for card in banner.find_all("a", recursive=True):
        try:
            symbol = card.find(class_=re.compile("symbol|name", re.I))
            price = card.find(class_=re.compile("price|value|stock", re.I))
            change = card.find(class_=re.compile("change|percent", re.I))

            if symbol and price and change:
                market_data.append({
                    "symbol": symbol.get_text(strip=True),
                    "stock_position": price.get_text(strip=True),
                    "change_pct": change.get_text(strip=True)
                })
        except Exception:
            pass

    print(f"Extracted {len(market_data)} market entries")
    return market_data


def extract_news_data(soup):
    print("Filtering news data...")
    news_data = []
    seen_links = set()

    section = soup.find("div", class_=re.compile("LatestNews", re.I))
    if not section:
        print("Latest News section not found")
        return news_data

    items = section.find_all("li", class_=re.compile("LatestNews-item", re.I))

    for item in items:
        try:
            time_elem = item.find("time", class_=re.compile("LatestNews-timestamp", re.I))
            timestamp = time_elem.get_text(strip=True) if time_elem else "N/A"

            link_elem = item.find("a", href=re.compile("/\\d{4}/"))
            if not link_elem:
                continue

            link = link_elem.get("href")
            if link.startswith("/"):
                link = "https://www.cnbc.com" + link

            if link in seen_links:
                continue

            title = link_elem.get_text(strip=True)
            if not title or len(title) < 15:
                continue

            seen_links.add(link)

            news_data.append({
                "timestamp": timestamp,
                "title": title[:200],
                "link": link
            })
        except Exception:
            pass

    print(f"Extracted {len(news_data)} news entries")
    return news_data


def save_to_csv(data, filename, fieldnames):
    path = "../data/processed_data"
    os.makedirs(path, exist_ok=True)

    filepath = os.path.join(path, filename)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV created: {filepath}")


def main():
    html_file = "../data/raw_data/web_data.html"
    print("Starting data filtering process")

    try:
        with open(html_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        market_data = extract_market_data(soup)
        if market_data:
            save_to_csv(
                market_data,
                "market_data.csv",
                ["symbol", "stock_position", "change_pct"]
            )

        news_data = extract_news_data(soup)
        if news_data:
            save_to_csv(
                news_data,
                "news_data.csv",
                ["timestamp", "title", "link"]
            )

        print("Data filtering completed")
        print(f"Market entries: {len(market_data)}")
        print(f"News entries: {len(news_data)}")

    except FileNotFoundError:
        print("web_data.html not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

