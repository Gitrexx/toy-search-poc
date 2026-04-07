# Search PoC

A proof-of-concept search UI backed by Elasticsearch, built with [Gradio](https://gradio.app). The single app (`frontend.py`) provides two tabs:

- **Datasets** — search at the dataset level
- **Columns** — search at the column level

Both tabs use mocked Elasticsearch responses so the app runs offline without a live ES cluster.

---

## Running

```bash
pip install -r requirements.txt
python frontend.py
# Open http://localhost:7860
```

---

## Dataset Search (Datasets tab)

Searches across dataset-level documents in the ES `datasets` index. Each document represents a single dataset.

| Field | Description |
|-------|-------------|
| `id` | Unique dataset identifier |
| `name` | Human-readable dataset name |
| `description` | Free-text description |
| `tags` | List of topic/domain tags |
| `format` | Storage format (CSV, Parquet, NetCDF, …) |
| `size` | Approximate storage size |
| `records` | Number of rows/records |
| `updated` | Date of last update |
| `license` | Data license (CC BY 4.0, ODbL, CC0, …) |
| `source` | Originating organisation or system |
| `score` | Elasticsearch relevance score (0–1) |

The query runs a `multi_match` across `name`, `description`, and `tags`, returning results ranked by relevance.

---

## Column Search (Columns tab)

Searches across column-level documents in the ES `columns` index. Every column of every dataset is ingested as an individual document, enabling fine-grained discovery by column name, data type, or description.

| Field | Description |
|-------|-------------|
| `id` | Unique column identifier |
| `column_name` | Column / field name |
| `data_type` | Data type (`float`, `integer`, `string`, `datetime`, `date`, …) |
| `description` | What the column holds |
| `dataset_id` | Parent dataset identifier |
| `dataset_name` | Parent dataset name |
| `nullable` | Whether null values are allowed |
| `sample_values` | Representative sample values |
| `tags` | Topic/domain tags |
| `score` | Elasticsearch relevance score (0–1) |

The query runs a `multi_match` across `column_name`, `description`, `data_type`, and `tags`. Each result card shows the parent dataset for context.

---

## Project Structure

```
search-poc/
├── frontend.py        # Gradio app (Datasets tab + Columns tab)
├── requirements.txt   # Python dependencies (gradio)
└── README.md
```

## Dependencies

```
gradio>=4.44.0
```
