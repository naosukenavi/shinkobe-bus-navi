from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = '''        <div class="point pink" style="margin-bottom:14px">
          <strong>🔴 ${t('関西空港（関空リムジン）','Kansai International Airport (Airport Limousine)')}</strong>
          <div>${t('4階ホテル玄関前発着','Departs from the 4F Hotel Entrance')}</div>
        </div>'''
new = '''        <div class="point pink" style="margin-bottom:14px">
          <strong>🔴 ${t('関西空港（関空リムジン）','Kansai International Airport (Airport Limousine)')}</strong>
          <div>${t('4階ホテル玄関前発着','Departs from the 4F Hotel Entrance')}</div>
          <div style="margin-top:8px"><strong>🕒 ${t('発車時刻','Departure times')}</strong></div>
          <div><strong>11:00／14:20</strong></div>
          <div>${t('1日2便（2026年9月現在）','2 services per day (as of September 2026)')}</div>
          <figure class="photo guide-shot" style="margin-top:12px">
            <img src="assets/kanku_limousine_bus.png" alt="関空リムジン車体 / Kansai Airport limousine bus vehicle">
            <figcaption>関空リムジン車体 / Kansai Airport limousine bus vehicle</figcaption>
          </figure>
        </div>'''

if old not in s:
    raise SystemExit('STEP4 Kansai block not found; aborting')
s = s.replace(old, new, 1)

# Remove the previously inserted vehicle photo from the separate Kansai Airport route,
# leaving its departure-time information intact.
wrong = '''        <figure class="photo guide-shot" style="margin-top:12px">
          <img src="assets/kanku_limousine_bus.png" alt="関空リムジン車体 / Kansai Airport limousine bus vehicle">
          <figcaption>関空リムジン車体 / Kansai Airport limousine bus vehicle</figcaption>
        </figure>'''
# The first occurrence after frontKansaiAirport is the misplaced one; the new STEP4 one occurs later/elsewhere.
front_pos = s.find('function frontKansaiAirport()')
if front_pos != -1:
    wrong_pos = s.find(wrong, front_pos)
    if wrong_pos != -1:
        s = s[:wrong_pos] + s[wrong_pos + len(wrong):]

p.write_text(s, encoding='utf-8')
