from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '          <div><strong>11:00／14:20</strong></div>'
if marker not in s:
    raise SystemExit('Kansai departure time marker not found')
start = s.index(marker)
target = '        </div>\n      </div>'
pos = s.index(target, start)
insert = '''        </div>
        <figure class="photo guide-shot" style="margin-top:12px">
          <img src="assets/kanku_limousine_bus.png" alt="関空リムジン車体 / Kansai Airport limousine bus vehicle">
          <figcaption>関空リムジン車体 / Kansai Airport limousine bus vehicle</figcaption>
        </figure>
      </div>'''
if 'assets/kanku_limousine_bus.png' in s[start:start+1500]:
    raise SystemExit('Kansai limousine image is already present')
s = s[:pos] + insert + s[pos+len(target):]
p.write_text(s, encoding='utf-8')
