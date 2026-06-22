from pathlib import Path

root = Path('c:/Users/33623/Desktop/mon-site')
updated = []
skipped = []
for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if 'tracking.js' in text:
        skipped.append(path.name)
        continue
    idx = text.lower().rfind('</body>')
    if idx == -1:
        skipped.append(path.name)
        continue
    new_text = text[:idx] + '    <script src="tracking.js"></script>\n' + text[idx:]
    path.write_text(new_text, encoding='utf-8')
    updated.append(path.name)

print('UPDATED', updated)
print('SKIPPED', skipped)
