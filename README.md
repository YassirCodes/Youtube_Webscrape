# 🎥 YouTube Scraper using Scrapy

A powerful YouTube scraping tool built with **Scrapy** and **yt-dlp** that:

- Fetches YouTube video data based on user-specified keywords  
- Extracts metadata (title, views, channel, description)  
- Downloads the corresponding videos automatically  
- Exports everything neatly into a **CSV file**

---

## 🚀 Features

✅ Extract video metadata from YouTube search results  
✅ Download videos automatically via **yt-dlp**  
✅ Save results to `videos.csv` (title, channel, views, description, video_url, local_path)  
✅ Random **User-Agent rotation** for anonymity  
✅ Automatic **proxy rotation** for bypassing IP limits  
✅ **Cloud-ready** design (can deploy on Zyte Scrapy Cloud or any VPS)

---

## 🧠 Project Workflow

```mermaid
flowchart TD
A[User Input] --> B[YouTube Search URL]
B --> C[Scrapy Spider Requests Page]
C --> D[Extract ytInitialData JSON]
D --> E[Parse Video Metadata]
E --> F[Pipeline - yt-dlp Downloads Video]
F --> G[Export Results to CSV]

## ⚙️ Installation

### Clone this repository
```bash
git clone https://github.com/YassirCodes/Youtube_Webscraping.git
cd Youtube_Webscraping
