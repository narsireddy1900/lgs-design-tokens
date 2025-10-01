"""
LGS Design System — Color Palettes

Usage:
    import colors
    print(colors.get("apple_green"))   # "#94B143"
    print(colors.rgb("tangerine"))     # (255, 173, 82)
    print(colors.palette("primary"))   # ['#94B143', '#378037']
"""

# -----------------------------
# Source of truth (all HEX)
# -----------------------------
COLORS: dict[str, str] = {
    # Primary
    "apple_green": "#94B143",
    "leaf":        "#378037",

    # Secondary
    "seal_brown":  "#42210B",
    "coffee_bean": "#A00D04",

    # Tertiary
    "mustard":     "#FFD452",
    "tangerine":   "#FFAD52",

    # Greyscale
    "night":       "#0D0D0D",
    "white":       "#FFFFFF",

    # Semantic
    "bg":          "#FFFAEA",
    "error":       "#CC0000",
    "link":        "#0277EC",
}

# Logical groupings
PALETTES: dict[str, list[str]] = {
    "primary":   ["apple_green", "leaf"],
    "secondary": ["seal_brown", "coffee_bean"],
    "tertiary":  ["mustard", "tangerine"],
    "greyscale": ["night", "white"],
    "semantic":  ["bg", "error", "link"],
}

# -----------------------------
# Helpers
# -----------------------------
def get(name: str) -> str:
    """Return HEX for a color token name."""
    return COLORS[name]

def palette(name_or_names: list[str] | str) -> list[str]:
    """Return a list of HEX values from a palette key or list of token names."""
    if isinstance(name_or_names, str):
        names = PALETTES[name_or_names]
    else:
        names = name_or_names
    return [COLORS[n] for n in names]

def rgb(name_or_hex: str) -> tuple[int, int, int]:
    """Return (R,G,B) 0..255 from a token name or hex string."""
    hx = COLORS.get(name_or_hex, name_or_hex).lstrip("#")
    return (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16))

def rgb01(name_or_hex: str) -> tuple[float, float, float]:
    """Return (r,g,b) 0..1 (useful for matplotlib)."""
    r, g, b = rgb(name_or_hex)
    return (r/255.0, g/255.0, b/255.0)
