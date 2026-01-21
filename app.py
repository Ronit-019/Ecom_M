import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import re

st.set_page_config(page_title="E-Store", layout="wide")

BASE_DIR = Path(__file__).parent
html_file = BASE_DIR / "index.html"

if html_file.exists():
    html = html_file.read_text(encoding="utf-8")

    # Extract CSS
    style_match = re.search(r"<style>(.*?)</style>", html, re.S)
    styles = style_match.group(1) if style_match else ""

    # Extract BODY
    body_match = re.search(r"<body>(.*?)</body>", html, re.S)
    body = body_match.group(1) if body_match else html

    final_html = f"""
    <style>
    {styles}
    html, body {{
        margin: 0;
        padding: 0;
    }}
    </style>

    {body}
    """

    components.html(final_html, height=3000, scrolling=True)
else:
    st.error("index.html not found")
