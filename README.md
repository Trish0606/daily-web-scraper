# 🕷️ Automated Price & News Tracker

A Python-based web scraper that automatically collects and logs data daily using GitHub Actions.

## 🤖 How it Works
- **Scraper:** A Python script using `BeautifulSoup` to extract the top trending headlines from Hacker News.
- **Automation:** Powered by **GitHub Actions** (CI/CD) to run on a daily cron schedule.
- **Persistence:** Automatically commits and pushes updated data to a `log.csv` file within the repository.

## 🛠️ Tech Stack
- **Language:** Python 3.9
- **Libraries:** Requests, BeautifulSoup4
- **Automation:** GitHub Actions (YAML)

## 📊 Data Collection
The `log.csv` file serves as a historical record of the data collected, providing a simple dataset for future analysis.
