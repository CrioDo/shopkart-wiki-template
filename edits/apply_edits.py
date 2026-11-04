"""Applies the B1 sync exercise's changes to your wiki copy, as two commits, so `askdocs sync` has something to sync.

Commit 1: an edit (the cash-on-delivery limit goes from 10,000 to 15,000 rupees) and a new page (exchanges).
Commit 2: a delete (the festive sale page, now that the sale is over), a near-copy of the support FAQ and an empty
page: the last two should be stopped by your quality gates, not indexed.

Run from the root of your wiki repo:  python edits/apply_edits.py   then  git push
"""
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "edits" / "round1"


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


shutil.copy(SRC / "cash-on-delivery.md", ROOT / "docs/policies/cash-on-delivery.md")
shutil.copy(SRC / "exchanges.md", ROOT / "docs/policies/exchanges.md")
git("add", "docs")
git("commit", "-m", "Raise the COD limit to 15,000 rupees; add the exchanges policy")

(ROOT / "docs/faq/festive-sale-2026.md").unlink()
shutil.copy(SRC / "support-faq-copy.md", ROOT / "docs/faq/support-faq-copy.md")
(ROOT / "docs/drafts").mkdir(exist_ok=True)
shutil.copy(SRC / "empty.md", ROOT / "docs/drafts/empty.md")
git("add", "-A", "docs")
git("commit", "-m", "Remove the festive sale page; add two pages (a copy and an empty draft)")
print("Two commits made. Push them:  git push")
