"""Make the static pages portable across GitHub Pages repository paths."""
from pathlib import Path
import re


def prepare_export(out: Path) -> None:
    out = Path(out)
    for page in out.rglob("index.html"):
        depth = len(page.relative_to(out).parts) - 1
        prefix = "../" * depth or "./"
        content = page.read_text(encoding="utf-8")
        # Every root-relative href and src comes from the site's original build.
        content = re.sub(
            r'\b(href|src)="/([^" ]*)"',
            lambda match: f'{match.group(1)}="{prefix}{match.group(2)}"',
            content,
        )
        page.write_text(content, encoding="utf-8")

    css_file = out / "style.css"
    css = css_file.read_text(encoding="utf-8")
    css_file.write_text(
        css.replace('[href="/projects/"]', '[href$="/projects/"]'),
        encoding="utf-8",
    )

    script = out / "app.js"
    js = script.read_text(encoding="utf-8")
    if "const siteBase=" not in js:
        js = js.replace(
            "let indexPromise;",
            "const siteBase=new URL('.',document.querySelector('script[src$=\"app.js\"]').src);\nlet indexPromise;",
        )
    js = js.replace("fetch('/search-index.json')", "fetch(new URL('search-index.json',siteBase))")
    js = js.replace("a.href=hit.url;", "a.href=new URL(hit.url.replace(/^\\//,''),siteBase).href;")
    script.write_text(js, encoding="utf-8")


if __name__ == "__main__":
    prepare_export(Path(__file__).resolve().parent.parent)
