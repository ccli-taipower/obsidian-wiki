"""Convert Obsidian [[wikilinks]] to GitHub-compatible markdown links.

Patterns:
  [[name]]                → [name](name.md)
  [[name|display]]        → [display](name.md)
  [[../wiki_X/page]]      → [page](../wiki_X/page.md)
  [[../wiki_X/page|disp]] → [disp](../wiki_X/page.md)
  [[../score-claude/memory/X]] → *memory: X* (not in this repo → italic plain text)

Run from /Users/ccli/Downloads/Obsidian/ root.
"""
import re
import sys
from pathlib import Path

WIKILINK = re.compile(r'\[\[([^\[\]]+?)\]\]')

def convert_link(match):
    body = match.group(1)
    # split alias
    if '|' in body:
        target, display = body.split('|', 1)
    else:
        target = body
        display = body
    target = target.strip()
    display = display.strip()
    # references outside obsidian-wiki repo (score-claude/memory) → italic plain
    if 'score-claude/memory' in target or 'score-claude/' in target:
        # extract last component for readability
        last = target.split('/')[-1]
        return f"*{display if display != target else last}*"
    # path-bearing wiki link (cross-wiki, same repo)
    if '/' in target:
        return f"[{display}]({target}.md)"
    # simple same-wiki link
    return f"[{display}]({target}.md)"

def convert_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    new_text, n_subs = WIKILINK.subn(convert_link, text)
    if n_subs > 0:
        path.write_text(new_text, encoding='utf-8')
    return n_subs

def main():
    root = Path(__file__).resolve().parent
    total_files = 0
    total_subs = 0
    for wiki_dir in ('wiki_articulation', 'wiki_phrase', 'wiki_piano'):
        wd = root / wiki_dir
        if not wd.is_dir():
            continue
        for md in sorted(wd.glob('*.md')):
            n = convert_file(md)
            if n > 0:
                print(f"  {wiki_dir}/{md.name}: {n} links converted")
                total_subs += n
                total_files += 1
    print(f"\nTotal: {total_subs} links converted across {total_files} files.")

if __name__ == '__main__':
    main()
