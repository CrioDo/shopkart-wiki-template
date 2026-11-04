"""Applies the B1 sync exercise's changes to your wiki copy, as two commits on a new branch, `wiki-edits`, so
`askdocs sync` has something to sync.

Commit 1: an edit (the cash-on-delivery limit goes from 10,000 to 15,000 rupees) and a new page (exchanges).
Commit 2: a delete (the festive sale page, now that the sale is over), a near-copy of the support FAQ and an empty
page: the last two should be stopped by your quality gates, not indexed.

The commits go on `wiki-edits`, and the script switches you back to the branch you started on, so your main branch
(the wiki your eval numbers and your app use) never changes. Sync reads the branch from GitHub.

Run from the root of your wiki repo:  python edits/apply_edits.py   then  git push -u origin wiki-edits
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "edits" / "round1"
BRANCH = "wiki-edits"


def git(*args: str, capture: bool = False) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, check=True, text=True, capture_output=capture)
    return r.stdout.strip() if capture else ""


if git("status", "--porcelain", capture=True):
    sys.exit("Your wiki copy has uncommitted changes: commit or discard them first.")
if git("branch", "--list", BRANCH, capture=True):
    sys.exit(f"Branch {BRANCH} already exists: the edits are made. Push it with:  git push -u origin {BRANCH}")
start = git("rev-parse", "--abbrev-ref", "HEAD", capture=True)
git("switch", "-c", BRANCH)

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

git("switch", start)
print(f"Two commits made on branch {BRANCH}; you're back on {start}, unchanged. Push the branch:\n"
      f"  git push -u origin {BRANCH}")
