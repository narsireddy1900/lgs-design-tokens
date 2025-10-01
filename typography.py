"""
LGS Design System — Typography Tokens

Usage:
    import typography
    print(typography.style("h1"))
    # {'family': 'heading', 'size': 32, 'weight': 700, 'use': 'Main page headings'}
"""

# -----------------------------
# Font families
# -----------------------------
FONTS: dict[str, str] = {
    "heading": 'Nunito, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
    "body":    'Open Sans, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
}

# -----------------------------
# Text styles
# -----------------------------
STYLES: dict[str, dict[str, object]] = {
    "display":   {"family": "heading", "size": (48, 64), "weight": 800, "use": "Homepage hero"},
    "h1":        {"family": "heading", "size": 32,       "weight": 700, "use": "Main page headings"},
    "h2":        {"family": "heading", "size": 24,       "weight": 600, "use": "Section titles"},
    "h3":        {"family": "heading", "size": 20,       "weight": 600, "use": "Card/Sidebar titles"},
    "body_lg":   {"family": "body",    "size": 18,       "weight": 400, "use": "Intro paragraphs"},
    "body":      {"family": "body",    "size": 16,       "weight": 400, "use": "Primary content"},
    "body_sm":   {"family": "body",    "size": 14,       "weight": 400, "use": "Notes/Descriptions"},
    "caption":   {"family": "body",    "size": 12,       "weight": 600, "use": "Footnotes/Helper labels"},
    "button":    {"family": "heading", "size": 16,       "weight": 600, "use": "Button labels"},
    "input":     {"family": "heading", "size": 16,       "weight": 400, "use": "Input field text"},
    "label":     {"family": "heading", "size": 12,       "weight": 500, "use": "Input label"},
}

# -----------------------------
# Helpers
# -----------------------------
def css_stack(key: str) -> str:
    """Return the CSS-like family stack string ('Nunito, system-ui, ...')."""
    return FONTS[key]

def style(name: str) -> dict[str, object]:
    """Return the raw token dict for a text style (size/weight/family/use)."""
    return STYLES[name]

def point_size(px: int, dpi: int = 96) -> float:
    """Convert px to points (pt) for libraries like reportlab/matplotlib."""
    return px * 72.0 / dpi
