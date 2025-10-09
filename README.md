# 🎥 Movie Recommendation System using Transformers and IMDb Web Scraping

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Transformers-4.0+-green.svg)](https://huggingface.co/transformers/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.0+-orange.svg)](https://scrapy.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.0+-yellow.svg)](https://www.crummy.com/software/BeautifulSoup/)

A comprehensive movie recommendation system that combines **BERT-powered semantic similarity** with **IMDb web scraping** to provide personalized movie recommendations. The system processes natural language queries and suggests movies based on content similarity and user preferences.

## 📖 Overview

This project offers **two different implementations** of the movie recommendation system:

### 🕷️ **Variant 1: Web Scraping Implementation (src/)**
- **BeautifulSoup & Requests**: Lightweight web scraping using BeautifulSoup and requests
- **Scrapy Framework**: Professional web scraping with Scrapy spiders
- **Real-time Data**: Extracts fresh movie data directly from IMDb
- **Customizable Scraping**: Configurable delays, user agents, and scraping strategies

### 📊 **Variant 2: CSV-based Implementation (notebook/)**
- **Pre-processed Dataset**: Uses `imdb_top_1000.csv` for faster development and testing
- **Jupyter Notebook**: Interactive development environment
- **BERT Integration**: Full implementation of BERT-powered recommendations
- **Ready-to-use**: No web scraping required, immediate results

Both variants use the same **BERT-powered recommendation engine** but differ in their data acquisition methods, making this project suitable for different use cases and skill levels.

## ✨ Features

### 🕷️ **Web Scraping Implementation (src/) Features**
- **Dual Scraping Methods**: 
  - BeautifulSoup & Requests for simple, lightweight scraping
  - Scrapy framework for professional, scalable web scraping
- **IMDb Data Extraction**: Scrapes movie titles, ratings, genres, descriptions, and metadata
- **Respectful Crawling**: Implements proper delays and respects robots.txt
- **Structured Data Pipeline**: Exports data to CSV/JSON format for analysis
- **Customizable Scraping**: Configurable settings for different scraping strategies
- **Error Handling**: Robust error handling and retry mechanisms
- **Data Validation**: Built-in data cleaning and validation pipelines
- **Multiple Output Formats**: Support for JSON, CSV, and XML export

### 📊 **CSV-based Implementation (notebook/) Features**
- **Pre-processed Dataset**: Uses curated `imdb_top_1000.csv` dataset
- **Interactive Development**: Jupyter notebook environment for experimentation
- **Fast Prototyping**: Immediate results without web scraping delays
- **Educational Value**: Step-by-step implementation with detailed explanations
- **Data Analysis Tools**: Built-in pandas and matplotlib integration
- **Reproducible Results**: Consistent dataset ensures reproducible recommendations

### 🤖 **Shared Recommendation Engine Features**
- **BERT Embeddings**: Uses `bert-base-uncased` for semantic understanding
- **Natural Language Processing**: Parses complex user queries
- **Similarity Calculation**: Cosine similarity between user input and movie descriptions
- **Rating Filtering**: Supports IMDb rating constraints (e.g., `imdb:8.2`)
- **Movie References**: Recognizes specific movie mentions in queries
- **Top-N Recommendations**: Returns ranked list of most relevant movies
- **Query Processing**: Handles multiple movie references and rating filters
- **Semantic Understanding**: Deep understanding of movie content and user preferences

## 🏗️ Project Structure

```
Movie-Recommendation-System-using-Transformers-and-IMDb-web-scraping/
├── src/                              # 🕷️ Web Scraping Implementation
│   ├── IMDb_Scraper/                 # Scrapy project for web scraping
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   └── imdbspider.py        # Main IMDb spider (BeautifulSoup/Requests)
│   │   ├── items.py                  # Data structure definitions
│   │   ├── middlewares.py            # Custom middlewares
│   │   ├── pipelines.py              # Data processing pipelines
│   │   └── settings.py               # Scrapy configuration
│   ├── scrapy.cfg                    # Scrapy project configuration
│   └── README.md                     # Web scraping component documentation
├── notebook/                         # 📊 CSV-based Implementation
│   ├── imdb-scraper.ipynb           # Jupyter notebook with BERT implementation
│   ├── data/
│   │   └── imdb_top_1000.csv        # Pre-processed dataset
│   └── requirements.txt              # Notebook-specific dependencies
├── assets/
│   ├── diagram.png                   # System architecture diagram
│   └── result.png                    # Example output
├── venv/                             # Virtual environment
├── requirements.txt                  # Main project dependencies
└── README.md                         # This comprehensive documentation
```

### 📁 **Directory Breakdown**

#### 🕷️ **src/ - Web Scraping Implementation**
- **IMDb_Scraper/**: Complete Scrapy project structure
- **spiders/**: Contains the main scraping logic using BeautifulSoup and requests
- **items.py**: Defines data structures for scraped movie information
- **middlewares.py**: Custom middleware for request handling and error management
- **pipelines.py**: Data processing and validation pipelines
- **settings.py**: Scrapy configuration with respectful crawling settings

#### 📊 **notebook/ - CSV-based Implementation**
- **imdb-scraper.ipynb**: Complete BERT-powered recommendation system
- **data/**: Contains the pre-processed IMDb dataset
- **requirements.txt**: Specific dependencies for the notebook environment

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step 1: Clone the Repository
```bash
git clone https://github.com/lilswapnil/Movie-Recommendation-System-using-Transformers-and-IMDb-web-scraping.git
cd Movie-Recommendation-System-using-Transformers-and-IMDb-web-scraping
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install main project dependencies (includes BeautifulSoup, requests, scrapy)
pip install -r requirements.txt

# Install notebook-specific dependencies (if using Jupyter)
pip install -r notebook/requirements.txt

# Additional dependencies for web scraping
pip install beautifulsoup4 requests lxml
```

### Step 4: Verify Installation
```bash
# Check if all packages are installed correctly
python -c "import pandas, numpy, torch, transformers, scikit_learn, scrapy; print('All dependencies installed successfully!')"
```

## 📊 Dataset

The system uses the `imdb_top_1000.csv` dataset located in `notebook/data/`. This dataset contains:

- **Series_Title**: Movie title
- **Genre**: Movie genre(s)
- **IMDB_Rating**: IMDb rating (0-10)
- **Overview**: Movie description/synopsis
- **Director**: Director name
- **Star1, Star2, Star3**: Main cast members
- **No_of_Votes**: Number of IMDb votes
- **Gross**: Box office earnings

## 🔧 Usage

### 📊 **Option 1: CSV-based Implementation (Recommended for Beginners)**
```bash
# Navigate to notebook directory
cd notebook

# Start Jupyter notebook
jupyter notebook imdb-scraper.ipynb

# Or run directly with Python
python -m jupyter notebook imdb-scraper.ipynb
```

**Advantages:**
- ✅ Immediate results without web scraping
- ✅ Educational step-by-step implementation
- ✅ Consistent dataset for reproducible results
- ✅ No rate limiting or blocking issues

### 🕷️ **Option 2: Web Scraping Implementation (Advanced Users)**
```bash
# Navigate to src directory
cd src

# Method A: Using Scrapy Framework
scrapy crawl imdbspider

# Run with custom settings
scrapy crawl imdbspider -s DOWNLOAD_DELAY=2 -s CONCURRENT_REQUESTS=1

# Save output to different formats
scrapy crawl imdbspider -o movies.json
scrapy crawl imdbspider -o movies.csv

# Method B: Using BeautifulSoup/Requests (if implemented)
python imdbspider.py
```

**Advantages:**
- ✅ Real-time data from IMDb
- ✅ Customizable scraping strategies
- ✅ Professional web scraping with Scrapy
- ✅ Scalable for large datasets

### 🔄 **Option 3: Hybrid Approach**
```bash
# First, scrape fresh data
cd src
scrapy crawl imdbspider -o ../notebook/data/fresh_movies.csv

# Then use the notebook with fresh data
cd ../notebook
jupyter notebook imdb-scraper.ipynb
```

## 💡 Example Usage

### Input Examples:
```python
# Basic movie recommendation
"movies like Inception"

# With rating filter
"Inception" imdb:8.5

# Multiple movies with rating
"The Dark Knight" "Interstellar" imdb:8.0

# Genre-based with rating
"action movies" imdb:7.5
```

### Expected Output:
```
Recommended Movies:
1. The Dark Knight (9.0) - Action, Crime, Drama
2. Interstellar (8.6) - Adventure, Drama, Sci-Fi
3. The Matrix (8.7) - Action, Sci-Fi
4. Blade Runner 2049 (8.0) - Action, Drama, Mystery
5. Mad Max: Fury Road (8.1) - Action, Adventure, Sci-Fi
...
```

## ⚙️ Configuration

### 🕷️ **Web Scraping Configuration**
Edit `src/IMDb_Scraper/settings.py` to customize:
- **Download delays**: `DOWNLOAD_DELAY = 1` (seconds between requests)
- **Concurrent requests**: `CONCURRENT_REQUESTS_PER_DOMAIN = 1`
- **User agents**: Custom user agent strings
- **Pipeline settings**: Data processing and validation
- **Robots.txt compliance**: `ROBOTSTXT_OBEY = True`

### 📊 **CSV-based Configuration**
Modify the notebook to adjust:
- **Number of recommendations**: Change `top_n` parameter
- **Similarity thresholds**: Adjust cosine similarity cutoffs
- **BERT model selection**: Switch between different BERT models
- **Rating filter ranges**: Modify IMDb rating constraints
- **Dataset path**: Update CSV file location

### 🔧 **Environment Configuration**
```bash
# For web scraping (add to .env or environment variables)
IMDB_BASE_URL=https://www.imdb.com
SCRAPY_DELAY=1
SCRAPY_CONCURRENT_REQUESTS=1

# For BERT model (optional)
BERT_MODEL_NAME=bert-base-uncased
MAX_SEQUENCE_LENGTH=512
```

## 🛠️ Development

### Setting up Development Environment
```bash
# Install development dependencies
pip install jupyter ipykernel

# Register virtual environment as Jupyter kernel
python -m ipykernel install --user --name=movie-rec-venv --display-name "MovieRec (venv)"
```

### Running Tests
```bash
# Test the scraper
cd src
scrapy check

# Test individual components
python -m pytest tests/
```

## 🔍 How It Works

### 🕷️ **Web Scraping Implementation Flow**
1. **Data Collection**
   - Scrapy spider navigates IMDb pages using BeautifulSoup/requests
   - Extracts movie metadata, ratings, genres, and descriptions
   - Implements respectful crawling with delays and user agents
   - Stores data in structured format (JSON/CSV)

2. **Data Processing**
   - Custom pipelines clean and validate scraped data
   - Middlewares handle request headers and error management
   - Data is exported to various formats for analysis

### 📊 **CSV-based Implementation Flow**
1. **Data Loading**
   - Loads pre-processed `imdb_top_1000.csv` dataset
   - Filters relevant columns (title, genre, rating, overview)
   - Handles missing values and data inconsistencies

2. **Text Processing**
   - User input is normalized and parsed
   - Movie names and rating constraints are extracted using regex
   - BERT tokenizer processes the text into tokens

3. **Embedding Generation**
   - BERT model generates semantic embeddings for user queries
   - Movie descriptions are converted to embeddings
   - Similarity matrix is computed using cosine similarity

4. **Recommendation Generation**
   - Cosine similarity scores are calculated between user input and movies
   - Results are filtered by IMDb rating constraints
   - Top-N recommendations are returned with scores and metadata

### 🔄 **Hybrid Approach**
- Combines both methods: scrape fresh data, then use BERT recommendations
- Ensures up-to-date movie information with advanced recommendation algorithms

## 🎯 Key Technologies

### 🕷️ **Web Scraping Technologies**
- **Scrapy**: Professional web scraping framework
- **BeautifulSoup4**: HTML/XML parsing library
- **Requests**: HTTP library for making web requests
- **LXML**: Fast XML and HTML parser
- **Selenium**: Web browser automation (optional)

### 🤖 **Machine Learning Technologies**
- **PyTorch**: Deep learning framework for BERT model
- **Transformers**: Hugging Face library for pre-trained models
- **BERT**: Bidirectional Encoder Representations from Transformers
- **Scikit-learn**: Machine learning utilities and cosine similarity
- **NumPy**: Numerical computing and array operations

### 📊 **Data Processing Technologies**
- **Pandas**: Data manipulation and analysis
- **Jupyter**: Interactive development environment
- **Matplotlib**: Data visualization (optional)
- **CSV/JSON**: Data storage and exchange formats

## 🚧 Limitations

### 🕷️ **Web Scraping Limitations**
- **Rate Limiting**: IMDb may block requests if too aggressive
- **Terms of Service**: Web scraping is subject to IMDb's terms of service
- **HTML Structure Changes**: IMDb website updates may break scrapers
- **IP Blocking**: Risk of IP address blocking with excessive requests
- **Data Consistency**: Scraped data may have inconsistencies

### 📊 **CSV-based Limitations**
- **Static Dataset**: Limited to pre-processed IMDb Top 1000 movies
- **Data Freshness**: Dataset may not include latest movies or updated ratings
- **Limited Scope**: Cannot expand beyond the provided dataset
- **No Real-time Updates**: Requires manual dataset updates

### 🤖 **BERT Model Limitations**
- **Computational Cost**: BERT embeddings are expensive for large datasets
- **Memory Usage**: High memory requirements for embedding generation
- **Processing Time**: Slower inference compared to simpler models
- **Model Size**: Large model files require significant storage space

## 🔮 Future Enhancements

### 🕷️ **Web Scraping Enhancements**
- [ ] **Multi-site Scraping**: Expand to other movie databases (Rotten Tomatoes, Metacritic)
- [ ] **Advanced Anti-detection**: Implement rotating proxies and user agents
- [ ] **Incremental Scraping**: Only scrape new/updated movies
- [ ] **Parallel Processing**: Multi-threaded scraping for better performance
- [ ] **Data Validation**: Enhanced data quality checks and cleaning
- [ ] **Scheduled Scraping**: Automated daily/weekly data updates

### 📊 **CSV-based Enhancements**
- [ ] **Dataset Expansion**: Include more movies beyond Top 1000
- [ ] **Multiple Datasets**: Support for different movie databases
- [ ] **Data Augmentation**: Generate synthetic movie descriptions
- [ ] **Version Control**: Track dataset changes over time
- [ ] **Data Validation**: Automated data quality checks

### 🤖 **Recommendation Engine Enhancements**
- [ ] **Genre-based Filtering**: Advanced genre classification and filtering
- [ ] **Cast and Director Recommendations**: Actor/director-based suggestions
- [ ] **Hybrid Recommendations**: Combine content-based and collaborative filtering
- [ ] **User Preference Learning**: Learn from user interactions
- [ ] **Multi-modal Features**: Include movie posters and trailers
- [ ] **Real-time Recommendations**: Live recommendation updates
- [ ] **Explainable AI**: Provide reasoning for recommendations

### 🌐 **Interface Enhancements**
- [ ] **Web Interface**: Create a user-friendly web application
- [ ] **API Development**: RESTful API for integration with other applications
- [ ] **Mobile App**: Native mobile application
- [ ] **Chrome Extension**: Browser extension for quick recommendations
- [ ] **Voice Interface**: Voice-activated movie recommendations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IMDb** for providing the movie data
- **Hugging Face** for the Transformers library and BERT model
- **Scrapy** team for the excellent web scraping framework
- **PyTorch** team for the deep learning framework

## 📞 Contact

- **Author**: lilswapnil
- **GitHub**: [@lilswapnil](https://github.com/lilswapnil)
- **Project Link**: [Movie Recommendation System](https://github.com/lilswapnil/Movie-Recommendation-System-using-Transformers-and-IMDb-web-scraping)

## 📊 Project Statistics

- **Language**: Python
- **Framework**: Scrapy, PyTorch, Transformers
- **Dataset**: IMDb Top 1000 Movies
- **Model**: BERT-base-uncased
- **License**: MIT

---

⭐ **If you found this project helpful, please consider giving it a star!**