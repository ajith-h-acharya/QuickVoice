from pathlib import Path
import re

path = Path('apps/web/src/components/ui/partners.tsx')
text = path.read_text(encoding='utf-8')

# Match d="..." including multiline content.
pattern = re.compile(r'd="(.*?)"', re.DOTALL)


def normalize(match):
    inner = match.group(1)
    if '\n' in inner or '\r' in inner:
        normalized = ' '.join(inner.split())
        return f'd="{normalized}"'
    return match.group(0)


new_text = pattern.sub(normalize, text)

if new_text != text:
    path.write_text(new_text, encoding='utf-8')
    print('normalized SVG d attributes')
else:
    print('no multiline SVG d attributes found')
