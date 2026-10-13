from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

snippet = '''  <script data-goatcounter="https://naomi-kobe.goatcounter.com/count"
          async src="https://gc.zgo.at/count.js"></script>
'''

if 'https://naomi-kobe.goatcounter.com/count' in s:
    raise SystemExit('GoatCounter is already installed; aborting')
if '</head>' not in s:
    raise SystemExit('</head> not found; aborting')

s = s.replace('</head>', snippet + '</head>', 1)
p.write_text(s, encoding='utf-8')
