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
| `asset_id` | Unique dataset identifier — rendered as a clickable link to `https://collibra.com/{asset_id}` |
| `dataset_name` | Human-readable dataset name |
| `country` | Country or region where the dataset originates |
| `application_layer` | Layer in the data platform (e.g. Analytics, Data Lake, Reporting) |
| `structure_type` | Data structure type (Structured, Semi-structured, Unstructured) |
| `domain` | Business or scientific domain the dataset belongs to |
| `partitioned_by` | List of partition keys, shown as pills |
| `score` | Elasticsearch relevance score (0–1) |

The query runs a `multi_match` across `dataset_name`, `domain`, `country`, `application_layer`, `structure_type`, and `partitioned_by`. The metadata grid uses a flexible auto-fill layout so long field values wrap within their cells rather than overflowing.

---

## Attribute Search (Attributes tab)

Searches across attribute-level documents in the ES `attributes` index. Every attribute (column) of every dataset is ingested as an individual document.

| Field | Description |
|-------|-------------|
| `attribute_name` | Attribute / column name |
| `status` | Lifecycle status: Active, Deprecated, Draft, Under Review — colour-coded badge |
| `domain` | Domain of the parent dataset |
| `description` | What the attribute holds |
| `info_sensitivity_class` | Data sensitivity level: Public, Internal, Confidential, Restricted — colour-coded badge with lock icon |
| `score` | Elasticsearch relevance score (0–1) |

The query runs a `multi_match` across `attribute_name`, `description`, `domain`, `status`, and `info_sensitivity_class`.

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
