from pathlib import Path
import re

path = Path('apps/web/src/components/ui/partners.tsx')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'd="(.*?)"', re.DOTALL)

matches = []
for i, m in enumerate(pattern.finditer(text), start=1):
    inner = m.group(1)
    if '\n' in inner or '\r' in inner:
        line = text.count('\n', 0, m.start()) + 1
        snippet = text[max(0, m.start()-80):min(len(text), m.end()+80)]
        matches.append((i, line, repr(inner[:200]), snippet))

print('count', len(matches))
for idx, line, inner_repr, snippet in matches:
    print('---')
    print('match', idx, 'line', line)
    print(inner_repr)
    print('--- snippet ---')
    print(snippet)
