"""Validate that public-site local references exist in the repository."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for key in ("href", "src"):
            if key in attributes:
                self.urls.append(attributes[key])

class SiteTests(unittest.TestCase):
    def test_html_assets_and_links(self):
        pages = list(ROOT.rglob("*.html"))
        self.assertGreaterEqual(len(pages), 6)
        for page in pages:
            scanner = Links()
            scanner.feed(page.read_text(encoding="utf-8"))
            for url in scanner.urls:
                parsed = urlsplit(url)
                if parsed.scheme or url.startswith("//") or url.startswith("#") or url.startswith("mailto:"):
                    continue
                target = ROOT / parsed.path.lstrip("/") if parsed.path.startswith("/") else page.parent / parsed.path
                if parsed.path.endswith("/"):
                    target = target / "index.html"
                if target.is_dir():
                    target = target / "index.html"
                with self.subTest(page=page.relative_to(ROOT), link=url):
                    self.assertTrue(target.is_file(), f"Broken site link: {url} from {page}")

    def test_sitemap_xml(self):
        import xml.etree.ElementTree as ET
        ET.parse(ROOT / "sitemap.xml")

if __name__ == "__main__":
    unittest.main()
