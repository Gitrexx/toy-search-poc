import gradio as gr
import time


# ---------------------------------------------------------------------------
# Mock data – dataset level
# ---------------------------------------------------------------------------

MOCK_DATASETS = [
    {
        "asset_id": "ds-001",
        "dataset_name": "Global Climate Observations 2020-2024",
        "country": "USA",
        "application_layer": "Analytics",
        "structure_type": "Structured",
        "domain": "Environmental Science",
        "partitioned_by": ["year", "month", "station_id"],
        "score": 0.97,
    },
    {
        "asset_id": "ds-002",
        "dataset_name": "Urban Air Quality Index",
        "country": "Multi-country",
        "application_layer": "Reporting",
        "structure_type": "Structured",
        "domain": "Public Health",
        "partitioned_by": ["city", "date"],
        "score": 0.91,
    },
    {
        "asset_id": "ds-003",
        "dataset_name": "Ocean Temperature & Salinity (Argo Float)",
        "country": "International",
        "application_layer": "Data Lake",
        "structure_type": "Semi-structured",
        "domain": "Marine Science",
        "partitioned_by": ["float_id", "year"],
        "score": 0.85,
    },
    {
        "asset_id": "ds-004",
        "dataset_name": "Global Forest Cover Change 2000-2023",
        "country": "International laksjflkajsdlfkjalskjfasdkfjhaksjdfhkasjdfhkajsfhksadjfhksajdfhkajsdfhkasjdfhksfhkasjdfhkajsdfhksdjf",
        "application_layer": "Data Lake",
        "structure_type": "Unstructured",
        "domain": "Environmental Science",
        "partitioned_by": ["year", "region"],
        "score": 0.78,
    },
    {
        "asset_id": "ds-005",
        "dataset_name": "Global Earthquake Catalog (USGS)",
        "country": "USA",
        "application_layer": "Analytics",
        "structure_type": "Structured",
        "domain": "Geoscience",
        "partitioned_by": ["year", "magnitude_range"],
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
        if any(
            w in (
                ds["dataset_name"] + " " + ds["domain"] + " "
                + ds["country"] + " " + ds["application_layer"] + " "
                + ds["structure_type"] + " " + " ".join(ds["partitioned_by"])
            ).lower()
            for w in words
        )
    ]
    return results if results else MOCK_DATASETS


# ---------------------------------------------------------------------------
# Mock data – attribute level
# ---------------------------------------------------------------------------

MOCK_ATTRIBUTES = [
    {
        "attribute_name": "station_id",
        "status": "Active",
        "domain": "Environmental Science",
        "description": "Unique identifier for the weather station that recorded the measurement.",
        "info_sensitivity_class": "Public",
        "score": 0.95,
    },
    {
        "attribute_name": "temperature_celsius",
        "status": "Active",
        "domain": "Environmental Science",
        "description": "Air temperature measured at 2 m above ground level in degrees Celsius.",
        "info_sensitivity_class": "Public",
        "score": 0.97,
    },
    {
        "attribute_name": "pm25_ugm3",
        "status": "Active",
        "domain": "Public Health",
        "description": "Concentration of fine particulate matter (PM2.5) in micrograms per cubic metre.",
        "info_sensitivity_class": "Internal",
        "score": 0.96,
    },
    {
        "attribute_name": "aqi_category",
        "status": "Active",
        "domain": "Public Health",
        "description": "AQI category label: Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, or Hazardous.",
        "info_sensitivity_class": "Public",
        "score": 0.91,
    },
    {
        "attribute_name": "depth_meters",
        "status": "Active",
        "domain": "Marine Science",
        "description": "Depth below sea surface at which the measurement was taken, in metres.",
        "info_sensitivity_class": "Public",
        "score": 0.94,
    },
    {
        "attribute_name": "sea_temperature_celsius",
        "status": "Active",
        "domain": "Marine Science",
        "description": "In-situ seawater temperature at the recorded depth, in degrees Celsius.",
        "info_sensitivity_class": "Public",
        "score": 0.97,
    },
    {
        "attribute_name": "tree_cover_pct",
        "status": "Deprecated",
        "domain": "Environmental Science",
        "description": "Percentage of canopy cover by tree vegetation for the pixel in the reference year 2000.",
        "info_sensitivity_class": "Internal",
        "score": 0.91,
    },
    {
        "attribute_name": "loss_year",
        "status": "Active",
        "domain": "Environmental Science",
        "description": "Year in which forest loss occurred for this pixel (0 if no loss).",
        "info_sensitivity_class": "Internal",
        "score": 0.87,
    },
    {
        "attribute_name": "magnitude",
        "status": "Active",
        "domain": "Geoscience",
        "description": "Moment magnitude (Mw) of the seismic event.",
        "info_sensitivity_class": "Public",
        "score": 0.94,
    },
    {
        "attribute_name": "patient_record_id",
        "status": "Active",
        "domain": "Public Health",
        "description": "Anonymised identifier linking the AQI exposure record to an individual health monitoring record.",
        "info_sensitivity_class": "Restricted",
        "score": 0.88,
    },
    {
        "attribute_name": "internal_cost_code",
        "status": "Draft",
        "domain": "Geoscience",
        "description": "Internal cost-centre code used for budget allocation of data collection operations.",
        "info_sensitivity_class": "Confidential",
        "score": 0.72,
    },
]


def mock_attribute_search(query: str) -> list[dict]:
    time.sleep(0.5)
    if not query.strip():
        return []
    words = query.lower().split()
    results = [
        attr for attr in MOCK_ATTRIBUTES
        if any(
            w in (
                attr["attribute_name"] + " " + attr["description"] + " "
                + attr["domain"] + " " + attr["status"] + " "
                + attr["info_sensitivity_class"]
            ).lower()
            for w in words
        )
    ]
    return results if results else MOCK_ATTRIBUTES


# ---------------------------------------------------------------------------
# Shared rendering helpers
# ---------------------------------------------------------------------------

SCORE_COLOR = {
    (0.90, 1.01): "#22c55e",
    (0.70, 0.90): "#f59e0b",
    (0.00, 0.70): "#ef4444",
}

STATUS_STYLE = {
    "Active":      ("#dcfce7", "#15803d"),
    "Deprecated":  ("#fee2e2", "#b91c1c"),
    "Draft":       ("#fef9c3", "#854d0e"),
    "Under Review": ("#dbeafe", "#1d4ed8"),
}

SENSITIVITY_STYLE = {
    "Public":       ("#dcfce7", "#15803d"),
    "Internal":     ("#dbeafe", "#1d4ed8"),
    "Confidential": ("#fef3c7", "#b45309"),
    "Restricted":   ("#fee2e2", "#b91c1c"),
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


def pill(label: str, bg: str = "#e0e7ff", fg: str = "#4338ca") -> str:
    return (
        f'<span style="background:{bg};color:{fg};padding:2px 10px;'
        f'border-radius:20px;font-size:12px;margin:2px;display:inline-block;">{label}</span>'
    )


def status_badge(status: str) -> str:
    bg, fg = STATUS_STYLE.get(status, ("#f1f5f9", "#334155"))
    return (
        f'<span style="background:{bg};color:{fg};padding:2px 10px;'
        f'border-radius:6px;font-size:12px;font-weight:600;">{status}</span>'
    )


def sensitivity_badge(cls: str) -> str:
    bg, fg = SENSITIVITY_STYLE.get(cls, ("#f1f5f9", "#334155"))
    return (
        f'<span style="background:{bg};color:{fg};padding:2px 10px;'
        f'border-radius:6px;font-size:12px;font-weight:600;">'
        f'&#128274; {cls}</span>'
    )


# ---------------------------------------------------------------------------
# Dataset card
# ---------------------------------------------------------------------------

def render_dataset_card(ds: dict) -> str:
    partitions_html = "".join(pill(p) for p in ds["partitioned_by"])
    meta_items = [
        ("Country", ds["country"]),
        ("Application Layer", ds["application_layer"]),
        ("Structure Type", ds["structure_type"]),
        ("Domain", ds["domain"]),
    ]
    return f"""
<div style="
    border:1px solid #e2e8f0;border-radius:12px;padding:20px 24px;margin-bottom:16px;
    background:#ffffff;box-shadow:0 1px 4px rgba(0,0,0,0.06);font-family:'Inter',sans-serif;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
    <div>
      <span style="font-size:11px;color:#94a3b8;font-weight:600;letter-spacing:.05em;">
        {ds["asset_id"].upper()}
      </span>
      <h3 style="margin:4px 0 6px;font-size:18px;color:#0f172a;">
        <a href="https://collibra.com/{ds['asset_id']}" target="_blank"
           style="color:#0f172a;text-decoration:none;border-bottom:1px solid #cbd5e1;"
           onmouseover="this.style.color='#2563eb'" onmouseout="this.style.color='#0f172a'">
          {ds["dataset_name"]}
        </a>
      </h3>
    </div>
    {score_badge(ds["score"])}
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(180px,100%),1fr));gap:8px;margin-bottom:12px;">
    {"".join(
        f'<div style="background:#f8fafc;border-radius:8px;padding:8px 12px;min-width:0;">'
        f'<div style="font-size:11px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">{k}</div>'
        f'<div style="font-size:13px;color:#1e293b;font-weight:500;margin-top:2px;word-break:break-word;overflow-wrap:anywhere;">{v}</div>'
        f'</div>'
        for k, v in meta_items
    )}
  </div>
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
    <span style="font-size:11px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">
      Partitioned by
    </span>
    {partitions_html}
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
# Attribute card
# ---------------------------------------------------------------------------

def render_attribute_card(attr: dict) -> str:
    return f"""
<div style="
    border:1px solid #e2e8f0;border-radius:12px;padding:20px 24px;margin-bottom:16px;
    background:#ffffff;box-shadow:0 1px 4px rgba(0,0,0,0.06);font-family:'Inter',sans-serif;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
      {status_badge(attr["status"])}
      <h3 style="margin:0;font-size:17px;color:#0f172a;font-family:monospace;">{attr["attribute_name"]}</h3>
    </div>
    {score_badge(attr["score"])}
  </div>
  <p style="color:#475569;font-size:14px;margin:10px 0 12px;line-height:1.6;">{attr["description"]}</p>
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;">
    <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/><path d="M12 2a15 15 0 0 1 0 20M2 12h20"/>
      </svg>
      <span>Domain: <strong style="color:#1e293b;">{attr["domain"]}</strong></span>
    </div>
    {sensitivity_badge(attr["info_sensitivity_class"])}
  </div>
</div>
"""


def render_attribute_results(attributes: list[dict]) -> str:
    if not attributes:
        return '<p style="color:#94a3b8;text-align:center;padding:40px 0;">No results found.</p>'
    header = (
        f'<p style="color:#64748b;font-size:14px;margin-bottom:16px;">'
        f'Found <strong>{len(attributes)}</strong> attribute(s)</p>'
    )
    return header + "".join(render_attribute_card(a) for a in attributes)


# ---------------------------------------------------------------------------
# Search handlers
# ---------------------------------------------------------------------------

EMPTY_DS = '<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search datasets.</p>'
EMPTY_ATTR = '<p style="color:#94a3b8;text-align:center;padding:40px 0;">Enter a query to search attributes.</p>'


def search_datasets(query: str) -> str:
    if not query.strip():
        return EMPTY_DS
    return render_dataset_results(mock_dataset_search(query))


def search_attributes(query: str) -> str:
    if not query.strip():
        return EMPTY_ATTR
    return render_attribute_results(mock_attribute_search(query))


# ---------------------------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------------------------

css = """
#ds-search textarea, #attr-search textarea { font-size: 16px !important; }
#ds-btn, #attr-btn { min-width: 110px; align-self: center; }
"""

with gr.Blocks(css=css, title="Data Search") as demo:
    gr.Markdown("# Data Search\nSearch datasets and their attributes powered by Elasticsearch.")

    with gr.Tabs():
        # ── Tab 1: Dataset Search ──────────────────────────────────────────
        with gr.Tab("Datasets"):
            gr.Markdown("Search across available datasets — enter keywords, domain, country, or dataset names.")
            with gr.Row():
                ds_input = gr.Textbox(
                    placeholder="e.g. climate analytics structured ...",
                    show_label=False,
                    scale=5,
                    elem_id="ds-search",
                )
                ds_btn = gr.Button("Search", variant="primary", scale=1, elem_id="ds-btn")
            ds_results = gr.HTML(value=EMPTY_DS)
            ds_btn.click(fn=search_datasets, inputs=ds_input, outputs=ds_results)
            ds_input.submit(fn=search_datasets, inputs=ds_input, outputs=ds_results)

        # ── Tab 2: Attribute Search ────────────────────────────────────────
        with gr.Tab("Attributes"):
            gr.Markdown("Search individual attributes across all datasets — by name, domain, status, or sensitivity.")
            with gr.Row():
                attr_input = gr.Textbox(
                    placeholder="e.g. temperature public health restricted ...",
                    show_label=False,
                    scale=5,
                    elem_id="attr-search",
                )
                attr_btn = gr.Button("Search", variant="primary", scale=1, elem_id="attr-btn")
            attr_results = gr.HTML(value=EMPTY_ATTR)
            attr_btn.click(fn=search_attributes, inputs=attr_input, outputs=attr_results)
            attr_input.submit(fn=search_attributes, inputs=attr_input, outputs=attr_results)


if __name__ == "__main__":
    demo.launch()
