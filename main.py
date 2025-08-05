import re
from pathlib import Path

# Folder where your .tex files are located
folder = Path("./")

# Pattern: match $...$, not preceded by \ and not $$...$$
pattern = re.compile(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)', re.DOTALL)

for tex_file in folder.glob("*.tex"):
    content = tex_file.read_text(encoding='utf-8')

    # Replace inline math $...$ with \( ... \)
    new_content = pattern.sub(lambda m: r'\(' + m.group(1).strip() + r'\)', content)

    tex_file.write_text(new_content, encoding='utf-8')
    print(f"Updated: {tex_file.name}")
