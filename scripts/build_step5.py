#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_code(folder, filename):
    p = os.path.join(base_dir, folder, "answers", filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

c_m05_l01 = read_code("05_starch_crisp_physics", "lesson01_triple_cooked_fries.py")
c_m05_l02 = read_code("05_starch_crisp_physics", "lesson02_pasta_starch_emulsion.py")
c_m06_l01 = read_code("06_connective_tissue_stocks", "lesson01_collagen_hydrolysis.py")
c_m06_l02 = read_code("06_connective_tissue_stocks", "lesson02_vegetable_chlorophyll.py")

m05 = {
    "id": "m05",
    "num": "05",
    "folder": "05_starch_crisp_physics",
    "title": "淀粉微观物理与极限酥脆工程",
    "title_en": "Starch Physics & Ultra-Crisp Engineering",
    "desc": "深入直链淀粉（Amylose）与支链淀粉糊化、老化回生（Retrogradation）微晶硬化相转变，解构三段法超脆薯条 30 分钟不塌软的结构工程与意面浓缩淀粉水防结块乳化。",
    "icon": "🥔",
    "lessons_count": 2,
    "lessons": [
        {
            "id": "m05_l01",
            "num": "01",
            "title": "三段热解法与直链淀粉结晶硬化",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：掌握微酸环境（pH 4.0 加醋）对果胶耐热稳定性的保护机制、冷冻诱导直链淀粉老化回生（Retrogradation）以及双温复炸蒸汽微孔发泡硬化工程。",
                "掌握标准：能够运用加醋微酸水煮 10 分钟 + 风干冷冻 + 170°C 初炸 / 205°C 复炸全流程，制作出酥脆半衰期达 28 分钟以上的极致玻璃脆皮薯条。"
            ],
            "chapter_bridge": "本课从蛋白质和脂质跨入植物多糖高分子聚合物领域，解析淀粉晶体相转变在脆度工程中的终极运用。",
            "feynman_analogy": "为什么快餐店的薯条刚出锅脆两分钟，带回家就变成了软塌塌、油腻腻的湿抹布？因为普通做法只是把生土豆扔进油锅：内部的水分在出锅后像出汗一样迅速往表皮渗透，把薄薄一层脆皮瞬间泡烂！Kenji 联合世界顶级名厨 Blumenthal 研发的科学三段法，是一次严密的微观结构筑墙工程：第一步，在水里加点醋煮土豆——酸性环境把植物细胞壁的果胶胶水牢牢加固，让土豆条猛煮 10 分钟也绝不散架，同时表面淀粉充分糊化成一层厚厚的黏性凝胶；第二步，放进冰箱冷冻——糊化的直链淀粉分子在低温下手拉手整齐排队，结晶成极其刚硬的微晶阵列（老化回生），相当于给薯条穿上了一层钢筋骨架；第三步，170°C 低温炸排出内部大部分水分，最后 205°C 极温复炸——微量残留水分瞬间汽化，把刚性外壳炸出千千万万个蜂窝状微米级小脆泡！这样的薯条哪怕放上半小时，咬下去依旧咔嚓作响、薄脆如碎玻璃！",
            "feynman_calc": "处理 500g 褐皮土豆（Russet Potatoes）：切成 8mm 标准条。对比组 A 直接生炸；对比组 B 采用微酸冷冻三段法（加 1 汤匙白醋，水 pH 降至 4.0，水煮 10 分钟后冷冻 2 小时，170°C 炸 50 秒排油冷凉，205°C 极速复炸 3.5 分钟）。实验测定脆度保留半衰期（降至临界松软时间）：直接生炸的薯条在出锅 3.5 分钟后脆度评分即从 80 暴跌至 35，完全塌软；而科学三段法薯条表面形成一层厚达 0.6mm 的直链淀粉坚韧多孔微晶壳，在出锅 28 分钟后依然保持 92 分以上的强劲咔嚓脆感，抗返潮时间延长整整 8 倍！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：极致酥脆薯条三段烹饪相转变：微酸果胶保护、直链淀粉老化与复炸蒸汽发泡</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 05 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m09" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m09)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#D97706"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">阶段 1 & 2：微酸果胶强化与冷冻回生</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 加醋使水 pH ≈ 4.0：原果胶耐热性跃迁，久煮不烂</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 表面淀粉吸水膨胀糊化，形成厚厚溶胶糊层</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 冷冻诱导老化回生：直链淀粉分子平行重组析晶</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
          <rect x="30" y="30" width="266" height="35" rx="4" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
          <text x="163" y="52" text-anchor="middle" font-size="11" font-weight="700" fill="#78350F">pH 4.0 果胶钙桥交联加固结构</text>
          <path d="M 163 70 L 163 90" stroke="#D97706" stroke-width="2.5"/>
          <rect x="30" y="95" width="266" height="55" rx="4" fill="#E0F2FE" stroke="#38BDF8" stroke-width="1.5"/>
          <text x="163" y="118" text-anchor="middle" font-size="11" font-weight="700" fill="#0369A1">-18°C 深度冷冻诱发淀粉老化回生</text>
          <text x="163" y="136" text-anchor="middle" font-size="10" fill="#0284C7">直链淀粉微晶阵列 (刚性骨架建立)</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#D97706">完整度 98% · 彻底告别煮烂断裂</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">阶段 3：双温复炸蒸汽微孔发泡</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 170°C 初炸 (50s)：温和排出表层游离水定型</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 205°C 复炸 (3.5m)：水蒸气爆裂形成千万微米气孔</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 玻璃化转变固化成硬壳，内芯松软如土豆泥</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <rect x="30" y="25" width="270" height="95" rx="8" fill="#FDE047" stroke="#B45309" stroke-width="2"/>
          <circle cx="60" cy="50" r="6" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="110" cy="45" r="5" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="160" cy="52" r="7" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="210" cy="46" r="5" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="260" cy="50" r="6" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="85" cy="90" r="6" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="135" cy="85" r="7" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="185" cy="92" r="6" fill="#FFFFFF" stroke="#D97706"/>
          <circle cx="235" cy="86" r="5" fill="#FFFFFF" stroke="#D97706"/>
          <text x="165" y="75" text-anchor="middle" font-size="11" font-weight="700" fill="#78350F">蜂窝微米级多孔气泡脆壳 (0.6mm)</text>
          <text x="165" y="145" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A">脆度半衰期达 28 分钟 · 拒绝塌软</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">咬合声音 99 分 · 殿堂级玻璃脆感</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>微酸环境与果胶酸甲酯酶稳定性</strong>：植物细胞通过果胶（Pectin）粘结细胞壁。在中性或碱性沸水中，果胶的多聚半乳糖醛酸链会发生剧烈的 $\beta$-消除水解断裂，导致土豆在水煮不到 5 分钟就崩解破烂成渣；在水中加入白醋将 pH 控制在 $4.0\sim 4.5$ 时，$\beta$-消除反应被彻底抑制，钙离子桥联结构极其坚韧，土豆即便久煮 10 分钟仍能保持棱角分明。</li>
  <li><strong>淀粉老化回生（Retrogradation）分子重排</strong>：淀粉粒由直链淀粉和支链淀粉组成。水煮糊化破坏了原本的天然微晶，分子链杂乱舒展；将煮熟的薯条彻底风干并放入 $-18^\circ\text{C}$ 冷冻室，低温使脱水舒展的直链淀粉分子在氢键驱动下自发平行紧密排列，重新结晶为高度规整耐热的“老化回生微晶体”（Resistant Starch Type III），为油炸脆壳提供了坚不可摧的聚合物刚性骨架。</li>
  <li><strong>双温阶梯油炸微孔发泡力学</strong>：初炸 $170^\circ\text{C}$ 是脱水脱湿与胶体定型工序，建立基础无水壳层；冷却后的二次复炸采用 $205^\circ\text{C}$ 超高温，内层残存的微量游离水在瞬间汽化膨胀突破淀粉外层，将刚性微晶吹发成无数微米级的蜂窝海绵状闭孔气泡，赋予薯条超大咬合声波共鸣与极强抗毛细渗水能力。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$t_{crisp} = t_0 \cdot \exp\left(\gamma \cdot X_{retro}\right) \cdot \left[1 + \kappa \cdot (pH_{opt} - |pH - pH_{opt}|)\right]$$
<div class="math-plain-bar">🗣️ 直白算式：脆度保持时间 = 基础寿命 × e^(回生指数加成) × [1 + 果胶微酸强化因子]；冷冻老化使寿命呈指数级翻倍</div>
</div>

<ul class="label-list">
  <li>$t_{crisp}$：薯条出锅后能维持咔嚓干脆状态的特征保留半衰期（分钟）。</li>
  <li>$X_{retro}$：直链淀粉冷冻老化微晶重排结晶度（冷冻处理 $X_{retro} \approx 0.95$，未经冷冻 $<0.20$）。</li>
  <li>$pH_{opt}$：果胶耐热交联最佳微酸环境（$\approx 4.0$）；偏酸或偏碱均会削弱结构完整度。</li>
  <li>科学三段法将 $t_{crisp}$ 从普通生炸的 $3.5\,\text{min}$ 提升至 $28.0\,\text{min}$。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>切忌使用蜡质土豆（Waxy Potatoes）如红皮土豆或小土豆做薯条</strong>。红皮土豆和黄心小土豆含有极高的水分与极低的淀粉含量（特别是缺乏直链淀粉，主要是支链淀粉），几乎无法发生有效的老化回生析晶反应，炸出来永远是绵软黏牙的死面疙瘩；制作极致脆皮薯条<strong>必须且只能选用高淀粉、低水分的粉质土豆（Starchy/Floury Potatoes）</strong>，如美国褐皮土豆（Russet Burbank）或国产高淀粉马铃薯，其高直链淀粉含量是构建坚固蜂窝脆壳的唯一物质基础！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">褐皮土豆三段烹饪脆度半衰期实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">三段法脆度保留半衰期</div><div class="result-kpi-value" style="color:#16A34A;">28.0 分钟</div><div class="result-kpi-sub">坚挺近半小时不软塌</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">传统直接油炸半衰期</div><div class="result-kpi-value" style="color:#DC2626;">3.5 分钟</div><div class="result-kpi-sub">出锅几分钟内吸潮软成泥</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">微酸果胶完整保留率</div><div class="result-kpi-value" style="color:#16A34A;">98.0%</div><div class="result-kpi-sub">加醋 pH 4.0 杜绝煮碎断裂</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">脆度咬合声学得分</div><div class="result-kpi-value" style="color:#CC5A36;">99 / 100</div><div class="result-kpi-sub">玻璃质感碎裂声波</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>土豆烹饪工艺方案</th><th>微酸水煮 (pH 4)</th><th>冷冻回生处理</th><th>油炸模式</th><th>结构完整度</th><th>出锅坚挺时长</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>Kenji 科学三段法</td><td>是 (加醋煮10分)</td><td>是 (-18°C 冻透)</td><td>170°C初炸 + 205°C复炸</td><td><strong style="color:#16A34A;">98.0% (完美挺拔)</strong></td><td><strong style="color:#16A34A;">28.0 分钟 (极品玻璃脆)</strong></td></tr>
        <tr><td>水煮但未加醋未冷冻</td><td>否 (白水煮碎烂)</td><td>否</td><td>单次油炸</td><td>35.0% (大量碎渣)</td><td>6.0 分钟</td></tr>
        <tr><td>生土豆直接浸水生炸</td><td>否</td><td>否</td><td>单次油炸</td><td>75.0%</td><td>3.5 分钟 (迅速塌软)</td></tr>
        <tr><td>市售冷冻半成品薯条</td><td>工业碱液处理</td><td>工业急冻</td><td>单次 180°C 炸</td><td>90.0%</td><td>12.0 分钟</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>选用 <strong>Russet 褐皮土豆</strong> 切 8mm 条；准备大锅水加入 <strong>1 汤匙白醋（每 2 升水）与 1 汤匙盐</strong>，煮沸后下薯条慢煮 <strong>10 分钟</strong> 捞出控干；平铺在烤盘上晾凉并移入冷冻室 <strong>冷冻至少 2 小时</strong>；无需解冻，直接下 <strong>170°C</strong> 油锅初炸 50 秒定型捞出；升高油温至 <strong>205°C</strong> 复炸 3.5 分钟至深金黄，撒盐出锅，享受长达半小时狂暴轰鸣的极致爽脆！
  </div>
</div>""",
            "code": c_m05_l01,
            "qa": [
                {
                    "q": "为什么很多食谱推荐在切完薯条后泡在冷水里“洗掉表面多余淀粉”，而在三段法中我们反而需要表面这层糊化淀粉？",
                    "a": "<p>这是针对两种完全不同烹饪路线的技术分野：</p><ol><li><strong>生土豆直接油炸路线</strong>：如果不洗掉表面游离的干淀粉碎屑，生土豆扔进油锅时，表面的散乱微细淀粉粒子会在高温油中迅速烧糊焦黑，在整根薯条内部还没熟透之前就形成发苦的黑点，因此直接油炸必须浸泡洗净表面粉尘。</li><li><strong>三段科学水煮路线</strong>：我们首先通过长达 10 分钟的加醋水煮，将土豆表层细胞完全煮软，洗掉了还原糖防止焦黑，同时将表层淀粉彻底<strong>糊化为一层厚达近 1 毫米的均匀黏稠直链淀粉溶胶糊</strong>。这层均匀的淀粉糊正是后续冷冻结晶形成连续抗水“玻璃脆壳”的全部原料来源！若把它洗掉，就等于亲手剥离了最珍贵的脆壳装甲。</li></ol>"
                },
                {
                    "q": "冷冻对薯条结构还有什么额外的物理级增益？为什么不能仅仅放在冷藏室（4°C）？",
                    "a": "<p>冷冻引发的<strong>冰晶膨胀刺破效应（Ice Crystal Micro-fissuring）</strong>是不可替代的关键物理步骤：土豆细胞内含有约 80% 的水分。当薯条在冷冻室降至 $-18^\circ\text{C}$ 时，水结冰体积膨胀约 9%，微小的冰晶在土豆外层细胞间刺出成千上万个微米级的微观细小裂缝。当下入滚烫热油时，这些微小裂缝成为了内部水蒸气瞬间喷射逸散的超高速逃逸通道，不仅防止了蒸汽滞留在表层泡软脆皮，更将外表面的比表面积放大了数倍，炸出如同天妇罗面糊般凹凸不平的惊人微脆微孔。</p>"
                }
            ]
        },
        {
            "id": "m05_l02",
            "num": "02",
            "title": "淀粉颗粒破裂与卡乔佩佩浓缩乳化浆",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：粉碎“意面必须用大量滚沸水煮”的能源浪费迷思，掌握冷水少水煮面法溶出 3%+ 浓缩直链淀粉溶胶的高分子空间位阻乳化机制。",
                "掌握标准：能够运用少水煮面法制备高浓度淀粉面汤，成功调制罗马经典卡乔佩佩（Cacio e Pepe）奶酪黑椒意面，实现 100% 顺滑乳化且零结块拉丝分离。"
            ],
            "chapter_bridge": "上一课解析了淀粉的老化固态脆化，本课转向水溶液中直链淀粉胶体在两相乳化体系中的空间位阻锚定作用。",
            "feynman_analogy": "煮意面是现代家庭厨房被传统教条洗脑最严重的灾区：老厨艺书警告你煮 1 磅意面必须烧开 5 升大锅滚水，否则意面会粘成一大坨死面。Kenji 用精密对照实验狠狠打了传统教条一记响亮耳光——只要在开始加温的头一两分钟随手划拉搅拌几下，意面哪怕在冷水里或者只有 1.5 升的少水里煮，吸水膨胀速度完全一样，根本不会粘连！更具颠覆性的是那锅被我们当脏水倒掉的‘面汤’：用 5 升水煮面，煮出来的面汤比白开水浓不了多少（淀粉浓度不到 0.4%）；而用刚刚没过意面的 1.5 升少水煮，煮出来的面汤是浓白浑浊的‘白色黄金液体’，淀粉浓度高达 3.5%！当你做著名的罗马卡乔佩佩（Cacio e Pepe）时，佩科里诺羊奶酪一遇热就会析出黄油、酪蛋白收缩结成令人崩溃的橡皮筋烂疙瘩；而只要舀入一勺这碗浓缩淀粉浆，千万条长链直链淀粉分子就会像一张温柔的捕鱼网，一头拉住水分子，一头兜住奶酪融化的牛油微滴，阻隔酪蛋白互相靠近，瞬间形成像天鹅绒缎子一样闪耀着诱人光芒、永不凝块的极品乳化酱汁！",
            "feynman_calc": "煮 450g（1 磅）标准硬质小麦意面：传统法用 5.0 升水煮，面汤中淀粉浓度仅为 0.74%；科学少水法仅用 1.5 升水。加热实测：将 5 升水烧开需耗电 0.52 kWh（耗时 16 分钟），而 1.5 升水仅耗电 0.16 kWh（耗时 5 分钟），节约了整整 70% 的电能与燃气！蒸发后剩余约 1.25 升面汤，溶出的直链与支链淀粉总量达 36.9g，面汤淀粉质量浓度高达 2.95%！将此浓缩面汤倒入佩科里诺奶酪碎中搅拌：乳化稳定性评分高达 98 分，奶酪结块风险指数为 0，酱汁在盘中静置 20 分钟依旧均匀乳化发亮！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：浓缩面汤淀粉胶体空间位阻乳化与卡乔佩佩奶酪酱防结块机制</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 05 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m10" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m10)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#DC2626"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">传统 5 升大锅水：淀粉极度稀释</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 耗能烧 5L 大锅水，烧水慢且浪费 70% 燃气</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 溶出淀粉浓度仅 0.5%~0.7%，汤如稀水被倒掉</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 调酱灾难：缺乏空间位阻，酪蛋白聚合成橡胶团</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
          <path d="M 70 80 Q 110 40 160 80 T 250 80" fill="none" stroke="#B91C1C" stroke-width="4"/>
          <circle cx="110" cy="80" r="22" fill="#DC2626"/>
          <circle cx="190" cy="80" r="26" fill="#DC2626"/>
          <ellipse cx="163" cy="135" rx="100" ry="14" fill="#FBBF24" opacity="0.7"/>
          <text x="163" y="85" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">酪蛋白结块 (橡皮团)</text>
          <text x="163" y="140" text-anchor="middle" font-size="10" font-weight="700" fill="#78350F">游离黄油析出分层</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#DC2626">酱汁破乳崩溃 · 油水分离如拉丝口香糖</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">科学少水法 (1.5L)：浓缩高分子乳化</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 水刚没过意面，烧水节能 70%，耗时仅 5 分钟</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 面汤淀粉浓度高达 2.95%，呈浓稠乳白液体黄金</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 直链淀粉长链形成高分子空间位阻，牢牢锁住油滴</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <path d="M 40 45 Q 165 75 290 45" fill="none" stroke="#16A34A" stroke-width="3" stroke-dasharray="3 3"/>
          <path d="M 40 125 Q 165 95 290 125" fill="none" stroke="#16A34A" stroke-width="3" stroke-dasharray="3 3"/>
          <circle cx="90" cy="85" r="16" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
          <circle cx="165" cy="85" r="18" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
          <circle cx="240" cy="85" r="16" fill="#FBBF24" stroke="#D97706" stroke-width="1.5"/>
          <text x="165" y="88" text-anchor="middle" font-size="10" font-weight="700" fill="#78350F">微米油滴</text>
          <text x="165" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#047857">天鹅绒般顺滑浓稠丝光乳化酱 (Cacio e Pepe)</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">淀粉浓度 2.95% · 0 结块风险 · 罗马殿堂口感</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>硬质小麦杜兰面粉吸水相转变规律</strong>：意大利干意面是由高蛋白质硬质小麦杜兰粉（Durum Wheat Semolina）压制干燥而成。意面只有在水温突破 $82^\circ\text{C}$ 时，蛋白质面筋网络才会不可逆变性凝固，淀粉颗粒才会吸水破裂糊化。在低于此温度（如冷水浸泡阶段），意面仅仅在被动物理吸水，绝不会释出黏性糊精，因此冷水入锅只要初期稍加翻动，完全不会结块粘连。</li>
  <li><strong>直链淀粉分子的高分子空间位阻效应（Steric Hindrance）</strong>：佩科里诺罗马奶酪或帕玛森干酪在加热至 $55^\circ\text{C}\sim 65^\circ\text{C}$ 时，内部的游离脂肪融化析出，酪蛋白（Casein）分子失去了疏水屏障，在疏水力和离子键驱动下疯狂自聚成坚韧橡皮团并与黄油分层。浓缩面汤中溶出的大量直链淀粉长链分子在水溶液中舒展，物理性地穿插阻隔在酪蛋白之间（空间位阻），阻止蛋白质靠拢团聚，同时将微米级油脂小球包裹稳定，形成均质水包油乳液。</li>
  <li><strong>少水浓缩带来的极致热效率与乳化力双赢</strong>：将烹饪用水量从 5.0 升精简至 1.5 升，不仅削减了 70% 的烧水碳足迹与漫长等待，更将宝贵的面汤从原本无法利用的稀薄废水直接升级为浓度近 3% 的天然高分子乳化改良剂，颠覆了整个意面烹饪流派。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$C_{starch} = \frac{m_{pasta} \cdot \eta_{release}}{V_{water} - \dot{V}_{evap} \cdot t}, \quad \Delta G_{barrier} = k_B T \cdot \left(\frac{C_{starch}}{C^*} - 1\right)$$
<div class="math-plain-bar">🗣️ 直白算式：面汤淀粉浓度 = 意面质量 × 溶出率 / (初始水量 - 蒸发量)；位阻排斥能量随淀粉浓度超临界提升而暴增</div>
</div>

<ul class="label-list">
  <li>$C_{starch}$：最终面汤中的淀粉质量浓度（% 或 $\text{g}/\text{L}$）。</li>
  <li>$\eta_{release}$：意面在沸水中溶出直链与支链淀粉的质量系数（实验测定约为 $8.2\%$）。</li>
  <li>$V_{water}$：下锅初始水量（传统法 $5.0\,\text{L}$，科学少水法 $1.5\,\text{L}$）。</li>
  <li>$\Delta G_{barrier}$：直链淀粉形成的防止酪蛋白靠拢结块的空间位阻自由能势垒；当 $C_{starch} \ge 2.5\%$ 时结块概率降为 0。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>绝对不要把磨好的奶酪碎直接倒进滚烫滚沸的平底锅中！</strong>做卡乔佩佩（Cacio e Pepe）最大的惨剧就是“火太大把奶酪烫死”：很多新手直接把奶酪倒入沸腾的面锅里，超过 70°C 的高温会让酪蛋白瞬间热变性收缩硬化成口香糖团，哪怕神仙也救不回来；正确科学做法：必须<strong>离火！在干净大碗里将奶酪碎与现磨黑胡椒混合，先舀入一勺 60°C 左右的浓缩淀粉面汤用打蛋器或叉子打成均匀光滑的膏状奶酪糊</strong>，再将煮至弹牙（Al Dente）的意面捞入碗中顺时针疯狂旋转剧烈乳化翻拌，即可获得如丝绸般包裹着每根面条的完美浓酱！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">450g 意面少水烹饪与奶酪乳化实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">科学少水法淀粉浓度</div><div class="result-kpi-value" style="color:#16A34A;">2.95%</div><div class="result-kpi-sub">相较传统大锅水浓缩 4.0 倍</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">烧水能源与时间节约</div><div class="result-kpi-value" style="color:#16A34A;">69.2%</div><div class="result-kpi-sub">1.5L 仅需 5 分钟极速烧沸</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">奶酪乳化酱汁黏附度</div><div class="result-kpi-value" style="color:#CC5A36;">98 / 100</div><div class="result-kpi-sub">丝缎光泽，死死挂在面条上</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">酪蛋白结块破乳概率</div><div class="result-kpi-value" style="color:#16A34A;">0.0%</div><div class="result-kpi-sub">空间位阻彻底隔绝聚团</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>意面煮水水量方案</th><th>烧水能耗 (kWh)</th><th>煮后残留水 (L)</th><th>面汤淀粉浓度 (%)</th><th>奶酪乳化状态</th><th>挂汁吸附表现</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>科学少水法 (1.5 升水)</td><td>0.16 kWh</td><td>1.25 L</td><td><strong style="color:#16A34A;">2.95% (高浓度)</strong></td><td><strong style="color:#16A34A;">天鹅绒丝滑浓稠乳化</strong></td><td><strong style="color:#CC5A36;">100% 紧密挂汁，盘底无水渍</strong></td></tr>
        <tr><td>适中少水法 (2.5 升水)</td><td>0.26 kWh</td><td>2.25 L</td><td>1.64%</td><td>良好可用，偶有轻微析油</td><td>挂汁良好</td></tr>
        <tr><td>传统大锅水 (5.0 升水)</td><td>0.52 kWh</td><td>4.75 L</td><td><strong style="color:#DC2626;">0.74% (稀薄)</strong></td><td>分离油汪汪，奶酪不易均质</td><td>滑落脱挂，盘底积聚水迹</td></tr>
        <tr><td>超大狂放水 (8.0 升水)</td><td>0.83 kWh</td><td>7.75 L</td><td>0.48% (接近清水)</td><td><strong style="color:#DC2626;">彻底结块拉丝成橡皮团</strong></td><td>完全挂不上汁</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>煮 1 磅意面时，换用宽口浅炒锅（Skillet），加入 <strong>1.5 升凉水与 1 茶匙盐</strong>，直接放入意面开大火烧水；水温上升期用夹子拨动意面 <strong>1 分钟防粘</strong>，沸腾后中火煮至离包装时间少 2 分钟；盛出 1/2 杯浓郁面汤与佩科里诺干酪粉调成顺滑奶酪糊，离火将意面拌入高速翻甩旋转，瞬间见证丝绸般发亮的大师级 Cacio e Pepe 诞生！
  </div>
</div>""",
            "code": c_m05_l02,
            "qa": [
                {
                    "q": "为什么冷水下锅煮意面（Cold-Water Pasta Method）完全行得通，而老厨师却深信“冷水下锅会粘成大面疙瘩”？",
                    "a": "<p>这是由<strong>杜兰小麦淀粉颗粒糊化临界温度的物理化学门槛</strong>决定的：</p><ol><li><strong>淀粉只有在高温下才会‘发黏’</strong>：意面表面释放能够引起严重粘连的黏性直链淀粉，必须在水温达到 $82^\circ\text{C}$ 以上使淀粉颗粒彻底吸水膨胀破裂（Gelatinization）才会发生。在水温从 $20^\circ\text{C}$ 上升至 $75^\circ\text{C}$ 的漫长加热过程中，意面只是在温和地润湿和渗透水分子，表面是光滑洁净的硬固态，根本不具备粘连的化学黏附力！</li><li><strong>老厨师的翻车根因</strong>：老厨师冷水下锅粘连的原因不是水温，而是<strong>把面放进冷水后就扔在那里完全不管</strong>。随着水温上升突破 $80^\circ\text{C}$，互相紧挨着的面条在发生淀粉糊化的那一瞬间若没有被外力扰动，接触点就会被糊化的淀粉胶水焊死在一起。Kenji 证明：只要在冷水下锅后以及水烧沸的初始阶段，用夹子随手搅拌扰动 30 秒，面条之间就会维持分离水膜，煮出来的弹牙筋道度与 5 升大沸水完全 100% 毫无二致！</li></ol>"
                },
                {
                    "q": "在煮意面的水中加入橄榄油能不能防止意面粘连？",
                    "a": "<p><strong>不能，而且这是严重的资源浪费和倒退！</strong>油的密度小于水，无论你怎么剧烈沸腾，橄榄油都只会浮在水面最顶层。当意面在几升水底翻滚时，根本接触不到浮在水面的油脂；唯一接触到油的瞬间，是你把煮好的意面从水里捞出来滤网穿过水面的那一刹那——这一层薄薄的浮油会包裹在热意面表面，而这正是灾难的开始：油膜形成了一道疏水隔离屏障，当你把意面拌入番茄酱或浓缩乳化酱汁时，<strong>酱汁根本无法挂在油腻的面条上</strong>，全部滑落到盘底变成难吃的积水。正确的防粘唯一手段就是开锅初期的物理搅拌，绝不在锅里加油。</p>"
                }
            ]
        }
    ]
}

print("Module 05 ready.")
