# Movie Recommendation Notebook

This folder contains the CSV-based, notebook-first implementation of the movie recommendation system. It uses a pre-processed IMDb dataset and BERT embeddings to generate recommendations from natural-language prompts. No web scraping is required for this workflow.

<p align="center">
  <img src="./assets/result.png" width="80%" alt="IMDB Movies Scraper" />
</p>

## What Is Included

- imdb-scraper.ipynb: The end-to-end notebook for data loading, embedding generation, and recommendations.
- data/imdb_top_1000.csv: The dataset used in the notebook.
- requirements.txt: Notebook-specific dependencies.

## Quick Start

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

## Expected Flow In The Notebook

1. Install dependencies (if needed).
2. Load the dataset from data/imdb_top_1000.csv.
3. Initialize BERT tokenizer and model.
4. Generate embeddings for movie overviews.
5. Enter a prompt to receive recommendations.

## Prompt Format

- Put movie titles in double quotes.
- Use imdb: to filter by minimum rating.

Examples:

```text
"The Godfather" imdb:8.5
"Inception" "Interstellar" imdb:8.0
action thriller imdb:7.5
```

## Notes

- Embedding generation can take several minutes on CPU.
- If you edit the dataset, re-run the embedding cell.
- The notebook uses bert-base-uncased by default.

## Troubleshooting

- Dataset not found: confirm data/imdb_top_1000.csv exists.
- Model download issues: clear Hugging Face cache at ~/.cache/huggingface and retry.
- Slow runtime: reduce the dataset size or run on a GPU.