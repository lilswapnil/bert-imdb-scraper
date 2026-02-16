# Movie Recommendation System Using BERT Transformer

This repository includes two parts:

1. A notebook-first pipeline that generates BERT embeddings for an IMDb dataset and returns movie recommendations from natural-language prompts.
2. A Scrapy project that can collect raw IMDb data if you want to refresh or expand the dataset.

<p align="center">
  <img src="./assets/result.png" width="80%" alt="IMDB Movies Scraper" />
</p>

## Repository Layout

- `notebook/` : Jupyter notebook workflow and dataset
- `src/` : Scrapy project for IMDb crawling
- `requirements.txt` : root dependencies (includes notebook + scraper)

## Python Version

TensorFlow does not yet provide wheels for Python 3.13+, so use Python 3.10 or 3.11 for this project.

## Notebook Workflow

The notebook runs end-to-end: load data, generate BERT embeddings, and query recommendations.

### Included Files

- `notebook/imdb-scraper.ipynb`
- `notebook/data/imdb_top_1000.csv`
- `notebook/requirements.txt`

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

- Dataset not found: confirm `notebook/data/imdb_top_1000.csv` exists.
- Model download issues: clear the Hugging Face cache at `~/.cache/huggingface` and retry.
- Slow runtime: reduce the dataset size or run on a GPU.
- `tensorflow` install fails on Python 3.13+: use Python 3.10 or 3.11.

## IMDb Web Scraper (Scrapy)

The Scrapy project collects movie data from IMDb charts and can export JSON or CSV.

### Scraper Structure

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

### Run The Spider

```bash
cd src

# Run the IMDb spider
scrapy crawl imdbspider

# Run with custom settings
scrapy crawl imdbspider -s DOWNLOAD_DELAY=2 -s CONCURRENT_REQUESTS=1

# Save output to file
scrapy crawl imdbspider -o movies.json
scrapy crawl imdbspider -o movies.csv
```

### Spider Behavior

- Starts from IMDb chart pages: Top 250, Most Popular, and Box Office.
- `ROBOTSTXT_OBEY` is set to `False` in `settings.py`.
- `CONCURRENT_REQUESTS_PER_DOMAIN = 1` and `DOWNLOAD_DELAY = 1` by default.

### Scraped Fields

- `title`: Movie title
- `category`: Movie genre/category
- `year`: Release year
- `rating`: IMDb rating
- `description`: Movie plot/overview
- `url`: IMDb page URL
- `image_url`: Movie poster URL

### Development

```bash
scrapy genspider myspider example.com
scrapy check
scrapy shell "https://www.imdb.com/"
```

## Dependencies

The root `requirements.txt` includes:

- `pandas`, `numpy`, `torch`, `transformers`, `tensorflow`, `scikit-learn`
- `scrapy`, `selenium`