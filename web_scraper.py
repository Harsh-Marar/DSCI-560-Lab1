from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

def scrape_cnbc_with_chromium():
    url = "https://www.cnbc.com/world/?region=world"
    print(f"Scraping: {url}")

    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = None
    try:
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(8)  # wait for JavaScript content
        html_content = driver.page_source

        raw_data_path = "../data/raw_data"
        os.makedirs(raw_data_path, exist_ok=True)
        output_file = os.path.join(raw_data_path, "web_data.html")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Data saved to: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

    finally:
        if driver:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    output_file = scrape_cnbc_with_chromium()
    
    if output_file:
        print("\n" + "="*60)
        print("First 10 lines of web_data.html:")
        print("="*60)
        with open(output_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if i > 10:
                    break
                print(f"{i}: {line.rstrip()}")

