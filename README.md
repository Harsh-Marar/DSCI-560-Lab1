# DSCI-560-Lab1
# CNBC Web Scraping and Data Filtering (DSCI 560 – Lab 1)

## Overview
This repository contains the implementation for DSCI-560 Lab 1, which focuses on setting up a Linux-based Python environment and performing basic web scraping and data processing tasks.
The project demonstrates foundational skills in Linux, Python scripting, dynamic web data collection, HTML parsing, and CSV-based data storage using a real-world news website.
The selected data source is the CNBC World News webpage. The project collects raw web data, extracts structured information from the market banner and latest news section, and stores the processed results in CSV files for further analysis.

## Scripts Overview
Web Data Collection (web_scraper.py)
This script uses Selenium with a headless Chromium browser to load JavaScript-rendered content from the CNBC World News website. The fully rendered HTML page is saved locally for offline processing. After saving the file, the script prints the first ten lines of the HTML file to the terminal for verification.
Output:
web_data.html stored in the data/raw_data directory
Data Filtering and Extraction (data_filter.py)
This script reads the saved HTML file using BeautifulSoup and extracts structured information from the page. Market banner data including the market symbol, stock position, and percentage change is collected. The script also extracts the latest news entries, including timestamps, article titles, and links. The extracted data is stored in CSV format and informative progress messages are printed to the console.
Outputs:
market_data.csv stored in the data/processed_data directory
news_data.csv stored in the data/processed_data directory
Basic Python Input Task
As part of the lab requirements, the project includes a simple Python task that prompts the user to enter their full name and prints a greeting message in the terminal.

## Requirements
The project requires Python version 3.8 or later. The following Python libraries are used: selenium and beautifulsoup4. The standard Python libraries csv, os, re, and time are also utilized. Chromium Browser and ChromeDriver are required system dependencies for Selenium-based web scraping.

## Execution Environment
The project is designed to run on Ubuntu Linux. Chromium is executed in headless mode to ensure compatibility with virtual machine and container-based environments.
Outputs
After successful execution, the project generates the following files:
web_data.html containing the raw scraped HTML content, market_data.csv containing structured market banner data, and news_data.csv containing structured latest news data. These files support further analysis and demonstrate successful data collection and processing from a real-world web source.

## Notes
Selenium is used instead of the Requests library because the CNBC webpage loads content dynamically using JavaScript. All data collected in this project is publicly available and intended solely for educational purposes.

## Course Information
Course: DSCI-560 – Data Science Professional Practicum
Assignment: Lab 1 – Environment Setup and Web Scraping
Semester: Spring 2026
