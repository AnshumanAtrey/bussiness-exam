"""Design system: colors, fonts, spacing, shadows, icons, logo."""

COLORS = {
    # Backgrounds
    "page_bg": "#F7F8FA",
    "card_bg": "#FFFFFF",
    "secondary_bg": "#F0F2F5",

    # Text
    "heading": "#0F1114",
    "primary_text": "#1A1D23",
    "muted": "#5F6B7A",

    # Brand
    "brand": "#0D7C66",
    "brand_hover": "#0A6352",
    "brand_tint": "#E6F4F0",
    "secondary": "#4B5E78",

    # Semantic
    "success": "#1A7F4B",
    "success_light": "#E8F5E9",
    "danger": "#C23A3A",
    "danger_light": "#FDEAEA",
    "warning": "#B8860B",
    "warning_light": "#FFF8E1",
    "info": "#2B6CB0",
    "info_light": "#E8F0FE",

    # Structure
    "border": "#E2E5EA",
    "border_light": "#ECEEF1",
    "divider": "#F0F0F0",
}

CHART_COLORS = ["#0D7C66", "#2B6CB0", "#C23A3A", "#B8860B", "#7C5CBF", "#3D8B8B"]

FONTS = {
    "heading": "Space Grotesk",
    "body": "Plus Jakarta Sans",
    "mono": "JetBrains Mono",
}

SPACING = {
    "card_padding": "24px",
    "card_gap": "16px",
    "row_gap": "24px",
    "section_gap": "48px",
    "page_margin": "32px",
}

BORDER_RADIUS = {
    "card": "8px",
    "button": "6px",
    "input": "6px",
    "badge": "4px",
}

SHADOWS = {
    "card": "0 1px 2px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.06)",
    "card_hover": "0 2px 4px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.06)",
    "elevated": "0 4px 8px rgba(0,0,0,0.04), 0 8px 24px rgba(0,0,0,0.08), 0 16px 48px rgba(0,0,0,0.06)",
}

PHOSPHOR_CDN = "https://unpkg.com/@phosphor-icons/web@2.1.1/src/duotone/style.css"
SPACE_GROTESK_CDN = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap"

# SVG logo for SecureNet - minimal shield with checkmark
LOGO_SVG = '''<svg width="180" height="40" viewBox="0 0 180 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 6 L20 2 L32 6 L32 18 C32 26 26 32 20 35 C14 32 8 26 8 18Z" fill="#E6F4F0" stroke="#0D7C66" stroke-width="1.5"/>
  <polyline points="14,18 18,22 26,14" fill="none" stroke="#0D7C66" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="40" y="27" font-family="Space Grotesk, sans-serif" font-size="18" fill="#0F1114" font-weight="700">Secure</text>
  <text x="110" y="27" font-family="Space Grotesk, sans-serif" font-size="18" fill="#0D7C66" font-weight="500">Net</text>
</svg>'''

LOGO_ICON_SVG = '''<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 6 L16 2 L28 6 L28 16 C28 23 22 28 16 31 C10 28 4 23 4 16Z" fill="#E6F4F0" stroke="#0D7C66" stroke-width="1.5"/>
  <polyline points="10,16 14,20 22,12" fill="none" stroke="#0D7C66" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
