"""Validate that public-site local references exist in the repository."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.anchors = set()
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.anchors.add(attributes["id"])
        if tag == "a" and "name" in attributes:
            self.anchors.add(attributes["name"])
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
                if parsed.scheme or parsed.netloc:
                    continue
                path = unquote(parsed.path)
                target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
                if not path:
                    target = page
                if parsed.path.endswith("/"):
                    target = target / "index.html"
                if target.is_dir():
                    target = target / "index.html"
                with self.subTest(page=page.relative_to(ROOT), link=url):
                    self.assertTrue(target.is_file(), f"Broken site link: {url} from {page}")
                    if parsed.fragment and target.suffix == ".html":
                        destination = Links()
                        destination.feed(target.read_text(encoding="utf-8"))
                        self.assertIn(unquote(parsed.fragment), destination.anchors,
                                      f"Missing link target: {url} from {page}")

    def test_sitemap_xml(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse(ROOT / "sitemap.xml")
        locations = [node.text for node in tree.findall(
            "{http://www.sitemaps.org/schemas/sitemap/0.9}url/"
            "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        self.assertEqual(len(locations), len(set(locations)), "Duplicate sitemap entries")
        expected = set()
        for page in ROOT.rglob("*.html"):
            path = page.relative_to(ROOT).as_posix()
            if path == "index.html":
                path = ""
            elif path.endswith("/index.html"):
                path = path[:-len("index.html")]
            expected.add("https://dietricheubank.github.io/" + path)
        self.assertEqual(set(locations), expected)

if __name__ == "__main__":
    unittest.main()
