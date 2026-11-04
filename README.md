# ShopKart internal wiki (training copy)

ShopKart's internal knowledge base: policies, runbooks, team pages and FAQs, as support agents and engineers read
them. **ShopKart and everything in this wiki are fictional**, written by Crio for the AI Engineering program.

You use it in project B1 AskDocs: the assistant you build answers questions from `docs/`, cites the pages, and
keeps itself in sync as the wiki changes.

## Get your copy
1. On GitHub, click **Use this template → Create a new repository**. Name it `shopkart-wiki`; public or private
   both work.
2. Create a fine-grained personal access token with **read-only** "Contents" access to that repository only
   (GitHub → Settings → Developer settings → Fine-grained tokens). B1 reads your wiki with it; it must never be
   able to write.
3. Clone it next to your B1 repo: `git clone https://github.com/<you>/shopkart-wiki.git`.

## What's here
| Folder | What it is |
|---|---|
| `docs/` | the wiki itself: 32 markdown pages, 3 help-centre HTML pages and 1 PDF |
| `edits/` | a set of changes you apply in B1's sync module, to see an add, an edit and a delete reach the index |

## Apply the edits (B1, sync module)
```bash
cd shopkart-wiki
python edits/apply_edits.py      # two commits on a new branch, wiki-edits: an edit and a new page, then a delete and two bad pages
git push -u origin wiki-edits
```
The edits go on their own branch and your `main` stays as it is: your eval numbers and your deployed app read
`main`. B1's README shows how to sync the branch.
