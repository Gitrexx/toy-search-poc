import gradio as gr
import json
import time


# ---------------------------------------------------------------------------
# Mock API
# ---------------------------------------------------------------------------

MOCK_DATASETS = [
    {
        "id": "ds-001",
        "name": "Global Climate Observations 2020-2024",
        "description": "High-resolution climate measurements from 5,000+ weather stations worldwide, including temperature, precipitation, humidity, and wind data.",
        "tags": ["climate", "weather", "environment", "time-series"],
        "format": "CSV / Parquet",
        "size": "42 GB",
        "records": "1,200,000,000",
        "updated": "2024-11-15",
        "license": "CC BY 4.0",
        "source": "NOAA / WMO",
        "score": 0.97,
    },
    {
        "id": "ds-002",
        "name": "Urban Air Quality Index",
        "description": "Daily AQI readings for 300 major cities covering PM2.5, PM10, NO2, SO2, CO, and O3 levels since 2015.",
        "tags": ["air quality", "pollution", "urban", "health"],
        "format": "JSON / CSV",
        "size": "3.8 GB",
        "records": "32,000,000",
        "updated": "2024-12-01",
        "license": "ODbL",
        "source": "OpenAQ",
        "score": 0.91,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
    {
        "id": "ds-003",
        "name": "Ocean Temperature & Salinity (Argo Float)",
        "description": "Depth profiles of temperature and salinity from 4,000 Argo floats deployed across the global ocean.",
        "tags": ["ocean", "marine", "climate", "deep-sea"],
        "format": "NetCDF",
        "size": "280 GB",
        "records": "4,500,000",
        "updated": "2024-10-20",
        "license": "CC0",
        "source": "Argo / Copernicus Marine",
        "score": 0.85,
    },
]


def mock_search_api(query: str) -> list[dict]:
    """Simulate an API call with a small delay."""
    time.sleep(0.6)
    if not query.strip():
        return []
    # Simple filter: keep datasets whose name/tags mention any query word
    words = query.lower().split()
    results = []
    for ds in MOCK_DATASETS:
        text = (ds["name"] + " " + " ".join(ds["tags"])).lower()
        if any(w in text for w in words):
            results.append(ds)
    # Fall back to returning all when nothing matches (demo convenience)
    return results if results else MOCK_DATASETS


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

SCORE_COLOR = {
    (0.90, 1.01): "#22c55e",   # green
    (0.70, 0.90): "#f59e0b",   # amber
    (0.00, 0.70): "#ef4444",   # red
}


def score_badge(score: float) -> str:
    color = "#94a3b8"
    for (lo, hi), c in SCORE_COLOR.items():
        if lo <= score < hi:
            color = c
            break
    pct = int(score * 100)
    return (
        f'<span style="background:{color};color:#fff;padding:2px 8px;'
        f'border-radius:12px;font-size:12px;font-weight:700;">{pct}% match</span>'
    )


def tag_pill(tag: str) -> str:
    return (
        f'<span style="background:#e0e7ff;color:#4338ca;padding:2px 10px;'
        f'border-radius:20px;font-size:12px;margin:2px;display:inline-block;">{tag}</span>'
    )


def render_dataset_card(ds: dict) -> str:
    tags_html = "".join(tag_pill(t) for t in ds["tags"])
    return f"""
<div style="
    border:1px solid #e2e8f0;
    border-radius:12px;
    padding:20px 24px;
    margin-bottom:16px;
    background:#ffffff;
    box-shadow:0 1px 4px rgba(0,0,0,0.06);
    font-family:'Inter',sans-serif;
">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
    <div>
      <span style="font-size:11px;color:#94a3b8;font-weight:600;letter-spacing:.05em;">
        {ds["id"].upper()}
      </span>
      <h3 style="margin:4px 0 6px;font-size:18px;color:#0f172a;">{ds["name"]}</h3>
    </div>
    {score_badge(ds["score"])}
  </div>

  <p style="color:#475569;font-size:14px;margin:0 0 12px;line-height:1.6;">
    {ds["description"]}
  </p>

  <div style="margin-bottom:12px;">{tags_html}</div>

  <div style="
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(160px,1fr));
    gap:8px;
  ">
    {"".join(
        f'<div style="background:#f8fafc;border-radius:8px;padding:8px 12px;">'
        f'<div style="font-size:11px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">{k}</div>'
        f'<div style="font-size:13px;color:#1e293b;font-weight:500;margin-top:2px;">{v}</div>'
        f'</div>'
        for k, v in [
            ("Format", ds["format"]),
            ("Size", ds["size"]),
            ("Records", ds["records"]),
            ("Updated", ds["updated"]),
            ("License", ds["license"]),
            ("Source", ds["source"]),
        ]
    )}
  </div>
</div>
"""


def render_results(datasets: list[dict]) -> str:
    if not datasets:
        return '<p style="color:#94a3b8;text-align:center;padding:40px 0;">No results found.</p>'
    header = (
        f'<p style="color:#64748b;font-size:14px;margin-bottom:16px;">'
        f'Found <strong>{len(datasets)}</strong> dataset(s)</p>'
    )
    cards = "".join(render_dataset_card(ds) for ds in datasets)
    return header + cards


# ---------------------------------------------------------------------------
# Search handler
# ---------------------------------------------------------------------------

def do_search(query: str):
    if not query.strip():
        return '<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search datasets.</p>'
    datasets = mock_search_api(query)
    return render_results(datasets)


# ---------------------------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------------------------

css = """
#search-bar textarea { font-size: 16px !important; }
#search-btn { min-width: 110px; }
#search-row { align-items: center; }
"""

with gr.Blocks(css=css, title="Dataset Search") as demo:
    gr.Markdown(
        """
# Dataset Search
Search across available datasets — enter keywords, topics, or dataset names.
"""
    )

    with gr.Row(elem_id="search-row"):
        search_input = gr.Textbox(
            placeholder="e.g. climate temperature ocean ...",
            show_label=False,
            scale=5,
            elem_id="search-bar",
        )
        search_btn = gr.Button("Search", variant="primary", scale=1, elem_id="search-btn")

    results_html = gr.HTML(
        value='<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search datasets.</p>',
    )

    # Trigger on button click or pressing Enter in the text box
    search_btn.click(fn=do_search, inputs=search_input, outputs=results_html)
    search_input.submit(fn=do_search, inputs=search_input, outputs=results_html)


if __name__ == "__main__":
    demo.launch()
