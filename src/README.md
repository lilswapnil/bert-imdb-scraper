# 🕷️ IMDb Web Scraper Component

This directory contains the Scrapy-based web scraping component for extracting movie data from IMDb.

## 📁 Structure

```
src/
├── IMDb_Scraper/                 # Main Scrapy project
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── imdbspider.py        # IMDb spider implementation
│   ├── items.py                  # Data structure definitions
│   ├── middlewares.py            # Custom middlewares
│   ├── pipelines.py              # Data processing pipelines
│   └── settings.py               # Scrapy configuration
└── scrapy.cfg                    # Project configuration
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Scrapy installed (`pip install scrapy`)

### Running the Spider
```bash
# Navigate to src directory
cd src

# Run the IMDb spider
scrapy crawl imdbspider

# Run with custom settings
scrapy crawl imdbspider -s DOWNLOAD_DELAY=2 -s CONCURRENT_REQUESTS=1

# Save output to file
scrapy crawl imdbspider -o movies.json
scrapy crawl imdbspider -o movies.csv
```

### Configuration
Edit `IMDb_Scraper/settings.py` to customize:
- Download delays
- Concurrent requests
- User agents
- Pipeline settings

## 📊 Data Structure

The spider extracts the following data for each movie:
- **title**: Movie title
- **category**: Movie genre/category
- **year**: Release year
- **rating**: IMDb rating
- **description**: Movie plot/overview
- **url**: IMDb page URL
- **image_url**: Movie poster URL

## ⚙️ Settings

Key configuration options in `settings.py`:
- `DOWNLOAD_DELAY = 1`: Delay between requests (seconds)
- `CONCURRENT_REQUESTS_PER_DOMAIN = 1`: Max concurrent requests per domain
- `ROBOTSTXT_OBEY = True`: Respect robots.txt rules

## 🔧 Development

### Creating Custom Spiders
```bash
# Generate new spider
scrapy genspider myspider example.com
```

### Testing
```bash
# Check spider configuration
scrapy check

# Run spider in shell for testing
scrapy shell "https://www.imdb.com/"
```

## 📝 Notes

- The spider respects IMDb's robots.txt and implements proper delays
- Data is processed through custom pipelines for cleaning and validation
- Middlewares handle request headers and error handling
- Output can be saved in multiple formats (JSON