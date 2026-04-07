import gradio as gr
import time


# ---------------------------------------------------------------------------
# Mock data – dataset level
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
        "id": "ds-004",
        "name": "Global Forest Cover Change 2000-2023",
        "description": "Annual land-cover classification and forest-loss / gain layers derived from Landsat imagery at 30 m resolution.",
        "tags": ["forestry", "land cover", "remote sensing", "environment"],
        "format": "GeoTIFF / Parquet",
        "size": "610 GB",
        "records": "N/A",
        "updated": "2024-03-10",
        "license": "CC BY 4.0",
        "source": "Hansen / GFW",
        "score": 0.78,
    },
    {
        "id": "ds-005",
        "name": "Global Earthquake Catalog (USGS)",
        "description": "Seismic event records since 1900 including magnitude, depth, location, and focal mechanism data.",
        "tags": ["seismology", "geology", "natural disaster", "time-series"],
        "format": "CSV / GeoJSON",
        "size": "1.2 GB",
        "records": "3,400,000",
        "updated": "2024-12-10",
        "license": "Public Domain",
        "source": "USGS NEIC",
        "score": 0.83,
    },
]


def mock_dataset_search(query: str) -> list[dict]:
    time.sleep(0.5)
    if not query.strip():
        return []
    words = query.lower().split()
    results = [
        ds for ds in MOCK_DATASETS
        if any(w in (ds["name"] + " " + " ".join(ds["tags"])).lower() for w in words)
    ]
    return results if results else MOCK_DATASETS


# ---------------------------------------------------------------------------
# Mock data – column level
# ---------------------------------------------------------------------------

MOCK_COLUMNS = [
    # ── Global Climate Observations ─────────────────────────────────────────
    {
        "id": "col-001",
        "column_name": "station_id",
        "data_type": "string",
        "description": "Unique identifier for the weather station that recorded the measurement.",
        "dataset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "nullable": False,
        "sample_values": ["USW00094728", "GME00111690", "ASN00066062"],
        "tags": ["climate", "weather", "identifier"],
        "score": 0.95,
    },
    {
        "id": "col-002",
        "column_name": "temperature_celsius",
        "data_type": "float",
        "description": "Air temperature measured at 2 m above ground level in degrees Celsius.",
        "dataset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "nullable": True,
        "sample_values": ["-12.3", "4.7", "31.2", "18.0"],
        "tags": ["climate", "temperature", "weather"],
        "score": 0.97,
    },
    {
        "id": "col-003",
        "column_name": "precipitation_mm",
        "data_type": "float",
        "description": "Daily total precipitation in millimetres.",
        "dataset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "nullable": True,
        "sample_values": ["0.0", "2.4", "15.8", "102.3"],
        "tags": ["climate", "precipitation", "weather"],
        "score": 0.93,
    },
    {
        "id": "col-004",
        "column_name": "wind_speed_ms",
        "data_type": "float",
        "description": "Mean wind speed over the observation period in metres per second.",
        "dataset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "nullable": True,
        "sample_values": ["1.2", "5.6", "12.3"],
        "tags": ["climate", "wind", "weather"],
        "score": 0.88,
    },
    {
        "id": "col-005",
        "column_name": "observation_timestamp",
        "data_type": "datetime",
        "description": "UTC timestamp of the observation in ISO-8601 format.",
        "dataset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "nullable": False,
        "sample_values": ["2024-01-01T00:00:00Z", "2024-06-15T12:00:00Z"],
        "tags": ["climate", "time-series", "timestamp"],
        "score": 0.90,
    },
    # ── Urban Air Quality Index ──────────────────────────────────────────────
    {
        "id": "col-006",
        "column_name": "city_name",
        "data_type": "string",
        "description": "Name of the city where the AQI reading was recorded.",
        "dataset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "nullable": False,
        "sample_values": ["Beijing", "London", "New York", "Mumbai"],
        "tags": ["air quality", "urban", "location"],
        "score": 0.92,
    },
    {
        "id": "col-007",
        "column_name": "pm25_ugm3",
        "data_type": "float",
        "description": "Concentration of fine particulate matter (PM2.5) in micrograms per cubic metre.",
        "dataset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "nullable": True,
        "sample_values": ["8.2", "35.6", "120.4", "250.1"],
        "tags": ["air quality", "pollution", "pm2.5", "health"],
        "score": 0.96,
    },
    {
        "id": "col-008",
        "column_name": "no2_ppb",
        "data_type": "float",
        "description": "Nitrogen dioxide concentration in parts per billion.",
        "dataset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "nullable": True,
        "sample_values": ["5.1", "22.7", "68.3"],
        "tags": ["air quality", "pollution", "no2"],
        "score": 0.89,
    },
    {
        "id": "col-009",
        "column_name": "aqi_category",
        "data_type": "string",
        "description": "AQI category label: Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, or Hazardous.",
        "dataset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "nullable": False,
        "sample_values": ["Good", "Moderate", "Unhealthy"],
        "tags": ["air quality", "category", "health"],
        "score": 0.91,
    },
    {
        "id": "col-010",
        "column_name": "reading_date",
        "data_type": "date",
        "description": "Date of the AQI reading in YYYY-MM-DD format.",
        "dataset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "nullable": False,
        "sample_values": ["2024-11-01", "2023-07-04"],
        "tags": ["air quality", "time-series", "date"],
        "score": 0.85,
    },
    # ── Ocean Temperature & Salinity ─────────────────────────────────────────
    {
        "id": "col-011",
        "column_name": "depth_meters",
        "data_type": "float",
        "description": "Depth below sea surface at which the measurement was taken, in metres.",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": False,
        "sample_values": ["5.0", "200.0", "1000.0", "2000.0"],
        "tags": ["ocean", "depth", "marine"],
        "score": 0.94,
    },
    {
        "id": "col-012",
        "column_name": "sea_temperature_celsius",
        "data_type": "float",
        "description": "In-situ seawater temperature at the recorded depth, in degrees Celsius.",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": True,
        "sample_values": ["1.8", "12.4", "28.7"],
        "tags": ["ocean", "temperature", "marine", "climate"],
        "score": 0.97,
    },
    {
        "id": "col-013",
        "column_name": "salinity_psu",
        "data_type": "float",
        "description": "Practical salinity of seawater in Practical Salinity Units (PSU).",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": True,
        "sample_values": ["33.8", "35.2", "36.7"],
        "tags": ["ocean", "salinity", "marine"],
        "score": 0.93,
    },
    {
        "id": "col-014",
        "column_name": "float_id",
        "data_type": "string",
        "description": "WMO identifier of the Argo float instrument.",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": False,
        "sample_values": ["6902869", "5905678", "1902345"],
        "tags": ["ocean", "identifier", "argo"],
        "score": 0.82,
    },
    {
        "id": "col-015",
        "column_name": "latitude",
        "data_type": "float",
        "description": "Geographic latitude of the float position in decimal degrees (WGS-84).",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": False,
        "sample_values": ["-45.23", "12.78", "60.01"],
        "tags": ["ocean", "location", "geospatial"],
        "score": 0.86,
    },
    {
        "id": "col-016",
        "column_name": "longitude",
        "data_type": "float",
        "description": "Geographic longitude of the float position in decimal degrees (WGS-84).",
        "dataset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "nullable": False,
        "sample_values": ["-120.45", "15.30", "178.99"],
        "tags": ["ocean", "location", "geospatial"],
        "score": 0.86,
    },
    # ── Global Forest Cover Change ────────────────────────────────────────────
    {
        "id": "col-017",
        "column_name": "tree_cover_pct",
        "data_type": "float",
        "description": "Percentage of canopy cover by tree vegetation for the pixel in the reference year 2000.",
        "dataset_id": "ds-004",
        "dataset_name": "Global Forest Cover Change 2000-2023",
        "nullable": True,
        "sample_values": ["0.0", "45.2", "87.9", "100.0"],
        "tags": ["forestry", "land cover", "environment"],
        "score": 0.91,
    },
    {
        "id": "col-018",
        "column_name": "loss_year",
        "data_type": "integer",
        "description": "Year in which forest loss occurred for this pixel (0 if no loss).",
        "dataset_id": "ds-004",
        "dataset_name": "Global Forest Cover Change 2000-2023",
        "nullable": True,
        "sample_values": ["0", "2015", "2020", "2023"],
        "tags": ["forestry", "deforestation", "time-series"],
        "score": 0.87,
    },
    # ── Global Earthquake Catalog ─────────────────────────────────────────────
    {
        "id": "col-019",
        "column_name": "magnitude",
        "data_type": "float",
        "description": "Moment magnitude (Mw) of the seismic event.",
        "dataset_id": "ds-005",
        "dataset_name": "Global Earthquake Catalog (USGS)",
        "nullable": False,
        "sample_values": ["2.1", "5.8", "7.4", "9.0"],
        "tags": ["seismology", "magnitude", "natural disaster"],
        "score": 0.94,
    },
    {
        "id": "col-020",
        "column_name": "depth_km",
        "data_type": "float",
        "description": "Hypocentral depth of the earthquake in kilometres.",
        "dataset_id": "ds-005",
        "dataset_name": "Global Earthquake Catalog (USGS)",
        "nullable": True,
        "sample_values": ["5.0", "33.0", "120.4", "640.0"],
        "tags": ["seismology", "depth", "geology"],
        "score": 0.88,
    },
]


def mock_column_search(query: str) -> list[dict]:
    time.sleep(0.5)
    if not query.strip():
        return []
    words = query.lower().split()
    results = [
        col for col in MOCK_COLUMNS
        if any(
            w in (
                col["column_name"] + " " + col["description"] + " "
                + " ".join(col["tags"]) + " " + col["data_type"]
                + " " + col["dataset_name"]
            ).lower()
            for w in words
        )
    ]
    return results if results else MOCK_COLUMNS


# ---------------------------------------------------------------------------
# Shared rendering helpers
# ---------------------------------------------------------------------------

SCORE_COLOR = {
    (0.90, 1.01): "#22c55e",
    (0.70, 0.90): "#f59e0b",
    (0.00, 0.70): "#ef4444",
}

TYPE_COLOR = {
    "float": "#dbeafe",
    "integer": "#dbeafe",
    "string": "#dcfce7",
    "datetime": "#fef9c3",
    "date": "#fef9c3",
    "boolean": "#fce7f3",
}
TYPE_TEXT = {
    "float": "#1d4ed8",
    "integer": "#1d4ed8",
    "string": "#15803d",
    "datetime": "#854d0e",
    "date": "#854d0e",
    "boolean": "#9d174d",
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


# ---------------------------------------------------------------------------
# Dataset card
# ---------------------------------------------------------------------------

def render_dataset_card(ds: dict) -> str:
    tags_html = "".join(tag_pill(t) for t in ds["tags"])
    return f"""
<div style="
    border:1px solid #e2e8f0;border-radius:12px;padding:20px 24px;margin-bottom:16px;
    background:#ffffff;box-shadow:0 1px 4px rgba(0,0,0,0.06);font-family:'Inter',sans-serif;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
    <div>
      <span style="font-size:11px;color:#94a3b8;font-weight:600;letter-spacing:.05em;">
        {ds["id"].upper()}
      </span>
      <h3 style="margin:4px 0 6px;font-size:18px;color:#0f172a;">{ds["name"]}</h3>
    </div>
    {score_badge(ds["score"])}
  </div>
  <p style="color:#475569;font-size:14px;margin:0 0 12px;line-height:1.6;">{ds["description"]}</p>
  <div style="margin-bottom:12px;">{tags_html}</div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:8px;">
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


def render_dataset_results(datasets: list[dict]) -> str:
    if not datasets:
        return '<p style="color:#94a3b8;text-align:center;padding:40px 0;">No results found.</p>'
    header = (
        f'<p style="color:#64748b;font-size:14px;margin-bottom:16px;">'
        f'Found <strong>{len(datasets)}</strong> dataset(s)</p>'
    )
    return header + "".join(render_dataset_card(ds) for ds in datasets)


# ---------------------------------------------------------------------------
# Column card
# ---------------------------------------------------------------------------

def type_badge(dtype: str) -> str:
    bg = TYPE_COLOR.get(dtype, "#f1f5f9")
    fg = TYPE_TEXT.get(dtype, "#334155")
    return (
        f'<span style="background:{bg};color:{fg};padding:2px 10px;'
        f'border-radius:6px;font-size:12px;font-weight:600;font-family:monospace;">{dtype}</span>'
    )


def render_column_card(col: dict) -> str:
    tags_html = "".join(tag_pill(t) for t in col["tags"])
    samples_html = "".join(
        f'<code style="background:#f1f5f9;padding:2px 6px;border-radius:4px;'
        f'font-size:12px;margin:2px;display:inline-block;">{v}</code>'
        for v in col["sample_values"]
    )
    nullable_label = "nullable" if col["nullable"] else "not null"
    nullable_color = "#f59e0b" if col["nullable"] else "#22c55e"
    return f"""
<div style="
    border:1px solid #e2e8f0;border-radius:12px;padding:20px 24px;margin-bottom:16px;
    background:#ffffff;box-shadow:0 1px 4px rgba(0,0,0,0.06);font-family:'Inter',sans-serif;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
      {type_badge(col["data_type"])}
      <h3 style="margin:0;font-size:17px;color:#0f172a;font-family:monospace;">{col["column_name"]}</h3>
      <span style="font-size:12px;color:{nullable_color};font-weight:600;">{nullable_label}</span>
    </div>
    {score_badge(col["score"])}
  </div>
  <p style="color:#475569;font-size:14px;margin:10px 0 12px;line-height:1.6;">{col["description"]}</p>
  <div style="margin-bottom:10px;">{tags_html}</div>
  <div style="background:#f8fafc;border-radius:8px;padding:10px 14px;margin-bottom:10px;">
    <div style="font-size:11px;color:#94a3b8;font-weight:600;text-transform:uppercase;
                letter-spacing:.05em;margin-bottom:4px;">Sample values</div>
    <div>{samples_html}</div>
  </div>
  <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>
    </svg>
    <span>Part of &nbsp;<strong style="color:#1e293b;">{col["dataset_name"]}</strong>
      &nbsp;<span style="color:#94a3b8;">({col["dataset_id"]})</span>
    </span>
  </div>
</div>
"""


def render_column_results(columns: list[dict]) -> str:
    if not columns:
        return '<p style="color:#94a3b8;text-align:center;padding:40px 0;">No results found.</p>'
    header = (
        f'<p style="color:#64748b;font-size:14px;margin-bottom:16px;">'
        f'Found <strong>{len(columns)}</strong> column(s)</p>'
    )
    return header + "".join(render_column_card(c) for c in columns)


# ---------------------------------------------------------------------------
# Search handlers
# ---------------------------------------------------------------------------

EMPTY_DS = '<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search datasets.</p>'
EMPTY_COL = '<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search columns.</p>'


def search_datasets(query: str) -> str:
    if not query.strip():
        return EMPTY_DS
    return render_dataset_results(mock_dataset_search(query))


def search_columns(query: str) -> str:
    if not query.strip():
        return EMPTY_COL
    return render_column_results(mock_column_search(query))


# ---------------------------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------------------------

css = """
#ds-search textarea, #col-search textarea { font-size: 16px !important; }
#ds-btn, #col-btn { min-width: 110px; align-self: center; }
"""

with gr.Blocks(css=css, title="Data Search") as demo:
    gr.Markdown("# Data Search\nSearch datasets and their columns powered by Elasticsearch.")

    with gr.Tabs():
        # ── Tab 1: Dataset Search ──────────────────────────────────────────
        with gr.Tab("Datasets"):
            gr.Markdown("Search across available datasets — enter keywords, topics, or dataset names.")
            with gr.Row():
                ds_input = gr.Textbox(
                    placeholder="e.g. climate temperature ocean ...",
                    show_label=False,
                    scale=5,
                    elem_id="ds-search",
                )
                ds_btn = gr.Button("Search", variant="primary", scale=1, elem_id="ds-btn")
            ds_results = gr.HTML(value=EMPTY_DS)
            ds_btn.click(fn=search_datasets, inputs=ds_input, outputs=ds_results)
            ds_input.submit(fn=search_datasets, inputs=ds_input, outputs=ds_results)

        # ── Tab 2: Column Search ───────────────────────────────────────────
        with gr.Tab("Columns"):
            gr.Markdown("Search individual columns across all datasets — by column name, data type, or topic.")
            with gr.Row():
                col_input = gr.Textbox(
                    placeholder="e.g. temperature float ocean pm2.5 ...",
                    show_label=False,
                    scale=5,
                    elem_id="col-search",
                )
                col_btn = gr.Button("Search", variant="primary", scale=1, elem_id="col-btn")
            col_results = gr.HTML(value=EMPTY_COL)
            col_btn.click(fn=search_columns, inputs=col_input, outputs=col_results)
            col_input.submit(fn=search_columns, inputs=col_input, outputs=col_results)


if __name__ == "__main__":
    demo.launch()
