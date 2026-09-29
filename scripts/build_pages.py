"""Build the presentation and a minimal GitHub Pages bundle from committed data."""
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, "status/build.py"], cwd=root, check=True)
docs = root / "docs"
(docs / "graphs").mkdir(parents=True, exist_ok=True)
page = (root / "status/index.html").read_text(encoding="utf-8")
(docs / "index.html").write_text(page.replace("`../${p}`", "`${p}`"), encoding="utf-8")
(docs / ".nojekyll").touch()
for name in ("tech_map.html", "coauthor.html", "project_timeline.html"):
    shutil.copy2(root / "graphs" / name, docs / "graphs" / name)
print("Built docs/: presentation and three interactive maps")
