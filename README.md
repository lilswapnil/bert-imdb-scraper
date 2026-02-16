# Movie Recommendation System Using BERT Transformer

This repository provides a notebook-first workflow for movie recommendations using BERT embeddings over a pre-processed IMDb dataset. A separate Scrapy project is included for collecting raw IMDb data.

<p align="center">
  <img src="./assets/result.png" width="80%" alt="IMDB Movies Scraper" />
</p>

## Contents

- Notebook workflow and dataset
- BERT-based recommendation example
- Scrapy-based IMDb scraper

## Notebook Workflow

The notebook runs end-to-end: load data, generate embeddings, and query recommendations from natural-language prompts.

### What Is Included

- `imdb-scraper.ipynb`: notebook for data loading, embeddings, and recommendations
- `data/imdb_top_1000.csv`: dataset used in the notebook
- `requirements.txt`: notebook dependencies

### Quick Start

```bash
cd notebook

# Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook imdb-scraper.ipynb
```

### Key BERT Recommendation Snippet

```python
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel

df = pd.read_csv("data/imdb_top_1000.csv")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

texts = df["Overview"].fillna("").tolist()
batch = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**batch).last_hidden_state[:, 0, :]

prompt = "action thriller"
query = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    q_vec = model(**query).last_hidden_state[:, 0, :]

scores = torch.matmul(outputs, q_vec.T).squeeze()
top_idx = torch.topk(scores, k=5).indices
print(df.loc[top_idx, ["Series_Title", "IMDB_Rating"]])
```

### Expected Flow In The Notebook

1. Install dependencies (if needed).
2. Load the dataset from `data/imdb_top_1000.csv`.
3. Initialize the BERT tokenizer and model.
4. Generate embeddings for movie overviews.
5. Enter a prompt to receive recommendations.

### Prompt Format

- Put movie titles in double quotes.
- Use `imdb:` to filter by minimum rating.

Examples:

```text
"The Godfather" imdb:8.5
"Inception" "Interstellar" imdb:8.0
action thriller imdb:7.5
```

### Notes

- Embedding generation can take several minutes on CPU.
- If you edit the dataset, re-run the embedding cell.
- The notebook uses `bert-base-uncased` by default.

### Troubleshooting

- Dataset not found: confirm `data/imdb_top_1000.csv` exists.
- Model download issues: clear the Hugging Face cache at `~/.cache/huggingface` and retry.
- Slow runtime: reduce the dataset size or run on a GPU.

## IMDb Web Scraper Component

The Scrapy project extracts movie data from IMDb and can save output in JSON or CSV formats.

### Structure

```
src/
├── IMDb_Scraper/                 # Main Scrapy project
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── imdbspider.py         # IMDb spider implementation
│   ├── items.py                  # Data structure definitions
│   ├── middlewares.py            # Custom middlewares
│   ├── pipelines.py              # Data processing pipelines
│   └── settings.py               # Scrapy configuration
└── scrapy.cfg                    # Project configuration
```

### Quick Start

Prerequisites:

- Python 3.7+
- Scrapy installed (`pip install scrapy`)

Running the spider:

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

### Data Structure

The spider extracts the following data for each movie:

- `title`: Movie title
- `category`: Movie genre/category
- `year`: Release year
- `rating`: IMDb rating
- `description`: Movie plot/overview
- `url`: IMDb page URL
- `image_url`: Movie poster URL

### Settings

Key configuration options in `settings.py`:

- `DOWNLOAD_DELAY = 1`: Delay between requests (seconds)
- `CONCURRENT_REQUESTS_PER_DOMAIN = 1`: Max concurrent requests per domain
- `ROBOTSTXT_OBEY = True`: Respect robots.txt rules

### Development

Create a custom spider:

```bash
scrapy genspider myspider example.com
```

Testing:

```bash
scrapy check
scrapy shell "https://www.imdb.com/"
```

### Notes

- The spider respects IMDb's robots.txt and implements proper delays.
- Data is processed through custom pipelines for cleaning and validation.
- Middlewares handle request headers and error handling.
- Output can be saved in multiple formats (JSON, CSV).