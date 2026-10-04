from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

marker = '    <div class="walking-entry">\n      <button class="walking-entry-btn" onclick="toggleWalkingEntry()" data-ja="🚶 徒歩ルート"'
if marker not in s:
    raise SystemExit('target marker not found')

section = '''    <div class="walking-entry elevator-entry">
      <button class="walking-entry-btn" onclick="toggleElevatorEntry()" data-ja="♿ エレベーター案内" data-en="♿ Elevator guide">♿ エレベーター案内</button>
      <div id="elevatorEntryPanel" class="walking-entry-panel" aria-live="polite">
        <div class="walking-route-note">
          <h3 data-ja="簡易版" data-en="Quick guide">簡易版</h3>
          <p><strong data-ja="① 新幹線改札口（2階）⇔ 1階ロータリー" data-en="① Shinkansen ticket gates (2F) ⇔ 1F bus rotary">① 新幹線改札口（2階）⇔ 1階ロータリー</strong><br>
          <span data-ja="2階のエレベーターを利用します。" data-en="Use the elevator on the 2nd floor.">2階のエレベーターを利用します。</span></p>
          <p><strong data-ja="② 地下鉄 新神戸駅改札口へ" data-en="② To Subway Shin-Kobe Station ticket gates">② 地下鉄 新神戸駅改札口へ</strong><br>
          <span data-ja="2階から渡り廊下を渡り、ホテルのエレベーターを利用します。" data-en="From the 2nd floor, cross the connecting corridor and use the hotel elevator.">2階から渡り廊下を渡り、ホテルのエレベーターを利用します。</span></p>
          <p><strong data-ja="③ 地下鉄改札内の移動" data-en="③ Inside the subway paid area">③ 地下鉄改札内の移動</strong><br>
          <span data-ja="地下鉄駅内のエレベーターを利用します。" data-en="Use the elevator inside the subway station.">地下鉄駅内のエレベーターを利用します。</span></p>
          <p><strong data-ja="④ トンネル入口へ" data-en="④ To the tunnel entrance">④ トンネル入口へ</strong><br>
          <span data-ja="エレベーター・エスカレーターはありません。階段を利用します。" data-en="There is no elevator or escalator. Use the stairs.">エレベーター・エスカレーターはありません。階段を利用します。</span></p>
          <p><strong data-ja="⑤ 駅舎の外へ出る" data-en="⑤ To exit the station building">⑤ 駅舎の外へ出る</strong><br>
          <span data-ja="A：ホテルのエレベーターで1階へ → 屋外のスロープ。B：生田橋を渡って生田川沿いへ。" data-en="A: Take the hotel elevator to 1F, then use the outdoor ramp. B: Cross Ikuta Bridge and continue along the Ikuta River.">A：ホテルのエレベーターで1階へ → 屋外のスロープ。B：生田橋を渡って生田川沿いへ。</span></p>
        </div>
        <details class="site-policy elevator-detail">
          <summary data-ja="詳細説明を見る" data-en="View detailed instructions">詳細説明を見る</summary>
          <div class="site-policy-body">
            <h3 data-ja="詳細説明" data-en="Detailed instructions">詳細説明</h3>
            <p><strong data-ja="新幹線改札口（2階）⇔1階ロータリー" data-en="Shinkansen ticket gates (2F) ⇔ 1F bus rotary">新幹線改札口（2階）⇔1階ロータリー</strong><br>
            <span data-ja="2階では、通路の先にある黄色い「エレベーター」表示を目印にしてください。1階では、案内板のある場所がエレベーターです。" data-en="On the 2nd floor, look for the yellow Elevator sign ahead along the passage. On the 1st floor, the elevator is beside the information sign.">2階では、通路の先にある黄色い「エレベーター」表示を目印にしてください。1階では、案内板のある場所がエレベーターです。</span></p>
            <p><strong data-ja="地下鉄 新神戸駅改札口へ" data-en="To Subway Shin-Kobe Station ticket gates">地下鉄 新神戸駅改札口へ</strong><br>
            <span data-ja="2階から渡り廊下を渡り、ホテル側へ進みます。ホテルのエレベーターで地下鉄改札階へ移動してください。" data-en="From the 2nd floor, cross the connecting corridor toward the hotel, then take the hotel elevator to the subway ticket gate level.">2階から渡り廊下を渡り、ホテル側へ進みます。ホテルのエレベーターで地下鉄改札階へ移動してください。</span></p>
            <p><strong data-ja="地下鉄改札内" data-en="Inside the subway paid area">地下鉄改札内</strong><br>
            <span data-ja="改札内の移動には、地下鉄駅内のエレベーターを利用してください。" data-en="For movement inside the paid area, use the elevator provided inside the subway station.">改札内の移動には、地下鉄駅内のエレベーターを利用してください。</span></p>
            <p><strong data-ja="トンネル入口へ" data-en="To the tunnel entrance">トンネル入口へ</strong><br>
            <span data-ja="トンネル入口へ直接つながるエレベーター・エスカレーターはありません。階段利用が必要です。" data-en="There is no elevator or escalator directly to the tunnel entrance. Stairs are required.">トンネル入口へ直接つながるエレベーター・エスカレーターはありません。階段利用が必要です。</span></p>
            <p><strong data-ja="駅舎の外へ出る：Aルート" data-en="Exit the station building: Route A">駅舎の外へ出る：Aルート</strong><br>
            <span data-ja="ホテルのエレベーターで1階へ下り、屋外のスロープから外へ出ます。スロープを出た先は車道で、横断歩道がありません。周囲の車に十分注意してください。" data-en="Take the hotel elevator down to 1F and exit via the outdoor ramp. The ramp leads directly to a roadway with no pedestrian crossing, so please watch carefully for vehicles.">ホテルのエレベーターで1階へ下り、屋外のスロープから外へ出ます。スロープを出た先は車道で、横断歩道がありません。周囲の車に十分注意してください。</span></p>
            <p><strong data-ja="駅舎の外へ出る：Bルート" data-en="Exit the station building: Route B">駅舎の外へ出る：Bルート</strong><br>
            <span data-ja="生田橋を渡り、生田川沿いへ進んで外へ出る方法もあります。" data-en="You can also cross Ikuta Bridge and continue along the Ikuta River to reach the outside.">生田橋を渡り、生田川沿いへ進んで外へ出る方法もあります。</span></p>
            <p data-ja="まず簡易版で確認し、必要な場合だけ詳細説明をご覧ください。" data-en="Check the quick guide first, then open the detailed instructions only if needed.">まず簡易版で確認し、必要な場合だけ詳細説明をご覧ください。</p>
          </div>
        </details>
      </div>
    </div>
'''

s = s.replace(marker, section + marker, 1)

js_marker = 'function toggleWalkingEntry(){'
if js_marker not in s:
    raise SystemExit('JS marker not found')
js = '''function toggleElevatorEntry(){
  const panel=document.getElementById('elevatorEntryPanel');
  if(panel) panel.classList.toggle('show');
}

'''
s = s.replace(js_marker, js + js_marker, 1)
p.write_text(s, encoding='utf-8')
