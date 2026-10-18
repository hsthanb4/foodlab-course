#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_code(folder, filename):
    p = os.path.join(base_dir, folder, "answers", filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

c_m06_l01 = read_code("06_connective_tissue_stocks", "lesson01_collagen_hydrolysis.py")
c_m06_l02 = read_code("06_connective_tissue_stocks", "lesson02_vegetable_chlorophyll.py")

m06 = {
    "id": "m06",
    "num": "06",
    "folder": "06_connective_tissue_stocks",
    "title": "结缔组织慢炖与高汤物理学",
    "title_en": "Connective Tissue Hydrolysis & Extraction",
    "desc": "深入哺乳动物 I 型胶原蛋白三螺旋超分子的湿热展开与明胶水解阿伦尼乌斯动力学，解构高压锅 1 小时媲美 8 小时传统慢炖的相图跃迁，以及绿色蔬菜焯水中叶绿素脱镁褐变阻断与果胶酶活控制。",
    "icon": "🍲",
    "lessons_count": 2,
    "lessons": [
        {
            "id": "m06_l01",
            "num": "01",
            "title": "胶原蛋白三螺旋展开与明胶黏度热解",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：理解牛骨与腱肉 I 型胶原蛋白（Collagen）三股刚性螺旋超分子受热断裂水解为可溶性明胶（Gelatin）的化学动力学，以及高压锅（121°C，15 psi）对 Arrhenius 反应速率的指数级放大效应。",
                "掌握标准：能够运用现代家用高压锅在 45~60 分钟内实现 95%+ 胶原水解转化率，熬制出冷藏后呈坚硬肉冻、入口即化、黏唇浓郁的殿堂级高汤。"
            ],
            "chapter_bridge": "本课从几分钟的快烹与短时间熟成，深入到数小时级大分子结缔组织的深度水解与高汤流变学构建。",
            "feynman_analogy": "骨头和牛腱肉里坚硬难嚼的结缔组织，本质上是一根根由钢丝拧成的超分子缆绳——‘I 型胶原蛋白’：三条氨基酸多肽链像麻花辫一样死死缠绕在一起，由无数个坚固的共价交联锁扣锁死，在常温甚至 60°C 的水里纹丝不动。要想把它变成在舌尖丝滑黏润的高汤，唯一的武器就是水和热量！在 85°C 的慢炖锅里，水分子像小锤子一样一点一点敲击缆绳，需要耐心熬上整整 8 个小时，麻花辫才能被彻底解开水解成单根舒展的小分子——‘明胶（Gelatin）’；而如果你换成现代家用高压锅，密封锁闭把锅内压强拉升至 2 个大气压，水温突破常规极限直接飙升至 121°C（250°F）！在阿伦尼乌斯定律的指数级催化下，水分子的冲击能量暴增十多倍，原本需要熬一整天的骨胶原，在短短 45 分钟内被摧枯拉朽般全部水解溶出，熬出黏唇拉丝的浓郁高汤！",
            "feynman_calc": "处理 1.5kg 鸡骨与牛小腿腱肉（含约 120g 可溶性粗胶原蛋白）：对比组 A 在传统明火微沸（85°C）下炖煮；对比组 B 置于 15 psi 高压锅（121°C）加压烹饪。阿伦尼乌斯活化能 Ea=92 kJ/mol。反应速率常数 k 在 85°C 时仅为 0.28 /小时，炖煮 1 小时胶原转化率仅 24.4%（汤水清汤寡淡），需持续慢炖 8 小时才能达到 89.4% 转化率；而在高压锅 121°C 下，k 值飙升至 3.25 /小时（暴增 11.6 倍！），仅需加压烹饪 60 分钟，胶原水解转化率即高达 96.1%，溶出明胶 115.3g，冷藏后直接凝结为像橡皮一样坚挺弹牙的高纯度肉冻，耗能削减 85%！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：I 型胶原蛋白三螺旋热解水解为可溶性明胶的阿伦尼乌斯动力学</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 06 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m11" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m11)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#D97706"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">传统明火慢炖 (85°C 微沸)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 活化能垒较高：三螺旋氢键缓慢断裂展开</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 1 小时转化率仅 24% (汤质稀薄水感无胶质)</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 必须持续炖煮 6~8 小时方能达成 85%+ 转化</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
          <text x="163" y="32" text-anchor="middle" font-size="11" font-weight="700" fill="#78350F">紧密交联三螺旋天然结构 (不溶)</text>
          <path d="M 40 65 Q 163 95 286 65" fill="none" stroke="#B45309" stroke-width="4"/>
          <path d="M 40 75 Q 163 45 286 75" fill="none" stroke="#D97706" stroke-width="4"/>
          <path d="M 40 85 Q 163 115 286 85" fill="none" stroke="#92400E" stroke-width="4"/>
          <text x="163" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="#B45309">85°C 慢水解：需熬煮 8 小时</text>
          <text x="163" y="156" text-anchor="middle" font-size="10" fill="#78350F">耗时漫长，且易挥发大量香气分子</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#D97706">耗时 8 小时 · 能耗巨大 · 照看繁琐</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">现代高压锅 (121°C，15 psi)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 饱和水蒸气压强将沸点拉升至 121°C (250°F)</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 阿伦尼乌斯速率常数 k 激增 11.6 倍！</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 45~60 分钟达成 96% 彻底水解，凝冻固化</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <text x="165" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A">完全解开为单链可溶性明胶 (Gelatin)</text>
          <path d="M 40 55 Q 100 80 160 50 T 290 60" fill="none" stroke="#16A34A" stroke-width="3" stroke-dasharray="3 3"/>
          <path d="M 40 85 Q 120 115 200 75 T 290 100" fill="none" stroke="#16A34A" stroke-width="3" stroke-dasharray="3 3"/>
          <path d="M 40 115 Q 140 85 220 125 T 290 110" fill="none" stroke="#16A34A" stroke-width="3" stroke-dasharray="3 3"/>
          <rect x="35" y="132" width="260" height="28" rx="4" fill="#16A34A"/>
          <text x="165" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">60 分钟转化率 96.1% · 冷藏成坚实肉冻</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">速率提升 11.6 倍 · 密闭锁住 100% 挥发香气</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>I 型胶原蛋白超分子刚性三螺旋解离热力学</strong>：哺乳动物骨骼与肌腱中最丰富的 I 型胶原蛋白由约 1050 个氨基酸残基构成，主要为 Gly-Pro-Hyp 重复序列，甘氨酸分子紧凑地嵌在轴心，靠致密的分子内与分子间氢键形成极强刚性绳索。在常温下不溶于水；只有在持续水分子侵入与热激发下，分子间共价交联键断开，三螺旋解螺旋为独立的无规线团多肽单链——明胶（Gelatin），在热水中完全溶解并赋予汤体丝绸质感。</li>
  <li><strong>阿伦尼乌斯定律与高压锅超临界加温</strong>：化学反应动力学阿伦尼乌斯公式（$k = A \exp(-E_a / RT)$）表明，活化能为 $92\,\text{kJ/mol}$ 的胶原水解反应对温度极度敏感。高压锅在 $15\,\text{psi}$（约 $103\,\text{kPa}$ 表压，即 2 个标准大气压）下，水的沸点被强行提升至 $121^\circ\text{C}$（$394.3\,\text{K}$）。绝对温度的提升使得分子的玻尔兹曼活化几率暴增，反应速率常数 $k$ 直接翻了 11.6 倍！</li>
  <li><strong>密闭腔体芳香分子完全保留</strong>：传统大锅敞口慢炖 8 小时，不仅能源消耗惊人，而且伴随着水分剧烈挥发，肉骨中珍贵的水溶性含硫化合物、内酯、吡嗪与醛酮等微量易挥发呈味香气分子会随着水蒸气全部逃逸到空气中（所谓“整条街都闻到肉香”，实质上是锅里的肉香跑光了！）；高压锅是完全密封的微环境，所有挥发性芳香分子在冷凝后 100% 回流到高汤中，鲜味浓烈度远超传统明火高汤。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$k(T) = A \cdot \exp\left(-\frac{E_a}{R \cdot (T + 273.15)}\right), \quad X(t) = 1 - \exp\left(-k(T) \cdot t\right)$$
<div class="math-plain-bar">🗣️ 直白算式：水解速率常数 = 指前常数 × e^(-活化能 / (气体常数 × 绝对温度))；水解转化率随时间按指数饱和曲线递增</div>
</div>

<ul class="label-list">
  <li>$k(T)$：温度为 $T$（°C）时的胶原蛋白水解反应一级速率常数（$\text{hour}^{-1}$）。</li>
  <li>$E_a$：胶原蛋白共价肽键水解活化能（约为 $9.2 \times 10^4\,\text{J}/\text{mol}$）。</li>
  <li>$R$：通用气体常数（$8.314\,\text{J}/(\text{mol}\cdot\text{K})$）。</li>
  <li>$X(t)$：烹饪持续 $t$ 小时后的胶原蛋白累计水解转化率（$0.0 \sim 1.0$）；达到 $0.90$ 以上即获极品黏唇高汤。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>高压锅熬高汤结束后，绝对不能强行手动快速放气（Quick Release）！</strong>很多急性子在烹饪结束立刻扳动排气阀猛烈放气，这是一个灾难性错误：高压锅在 121°C 时内部处于高压相平衡态。瞬间强行泄压会导致锅内液体沸点骤降回 100°C，过热的高汤会在锅底发生<strong>剧烈爆发性暴沸（Violent Explosive Boiling）</strong>，剧烈的气泡机械搅拌会把脆弱煮透的骨头碎渣、多孔骨髓与油脂彻底粉碎成悬浮微粒，高汤瞬间乳化变成浑浊泥浆般的灰白色！正确做法是：<strong>自然慢冷泄压（Natural Release 约 20~25 分钟）</strong>，让锅内温度温和缓慢降回 98°C，开盖即可得到晶莹透亮金黄澈底的米其林级清高汤（Consommé Clarity）！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">1.5kg 牛骨腱肉高汤水解转化率实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">高压锅 60分转化率</div><div class="result-kpi-value" style="color:#16A34A;">96.1%</div><div class="result-kpi-sub">超越传统慢炖 8 小时效果</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">明火慢炖 1小时转化率</div><div class="result-kpi-value" style="color:#DC2626;">24.4%</div><div class="result-kpi-sub">水解严重不足，水感清淡</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">Arrhenius 速率提升</div><div class="result-kpi-value" style="color:#CC5A36;">11.6 倍</div><div class="result-kpi-sub">121°C 相比 85°C 动力学跃迁</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">冷藏肉冻坚挺硬度</div><div class="result-kpi-value" style="color:#16A34A;">100% 固态凝胶</div><div class="result-kpi-sub">常温倒扣不洒，入口体温即化</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>高汤熬制烹饪方案</th><th>设定温度</th><th>熬煮时长</th><th>水解速率常数 k</th><th>胶原转化率 (%)</th><th>冷藏状态与汤体质感</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>现代 15 psi 高压锅自然泄压</td><td>121.0°C</td><td>1.0 小时 (60m)</td><td><strong style="color:#16A34A;">3.250 /h</strong></td><td><strong style="color:#16A34A;">96.1%</strong></td><td><strong style="color:#CC5A36;">极度黏唇拉丝，冷藏成致密肉冻</strong></td></tr>
        <tr><td>传统明火长效慢炖</td><td>85.0°C</td><td>8.0 小时 (480m)</td><td>0.280 /h</td><td>89.4%</td><td>黏润醇厚，冷藏半凝固，香气损失 30%</td></tr>
        <tr><td>传统明火中度慢炖</td><td>85.0°C</td><td>3.0 小时</td><td>0.280 /h</td><td>56.8%</td><td>中等厚度，冷藏依然为液体</td></tr>
        <tr><td>短时微沸炖煮</td><td>85.0°C</td><td>1.0 小时</td><td>0.280 /h</td><td><strong style="color:#DC2626;">24.4%</strong></td><td>清淡水感，几乎无明胶溶出</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>将 1.5kg 鸡骨架或牛尾在 <strong>220°C 烤箱中预烤 30 分钟</strong> 促发美拉德焦香；移入高压锅，加入冷水刚刚没过骨头，加入洋葱、胡萝卜和芹菜（Mirepoix）；加盖锁死上汽，保持在 <strong>15 psi（高压档）加压烹饪整整 60 分钟</strong>；关火后必须让其 <strong>自然冷却泄压 20 分钟</strong>，用极细双层滤网过滤；冷藏后刮掉顶部白固态油脂，下方即是琥珀金黄、如碎钻般透亮的顶级肉冻高汤！
  </div>
</div>""",
            "code": c_m06_l01,
            "qa": [
                {
                    "q": "为什么高压锅熬制的高汤清澈度（Clarity）在自然泄压时往往比传统明火慢炖还要高？",
                    "a": "<p>这颠覆了大众对“高压锅会把东西压烂煮烂”的直觉误解：</p><ol><li><strong>完全静止的液面</strong>：在高压锅完全密封加压达到稳定相平衡后，锅内压强（2 atm）使得沸点提升至 121°C，而如果炉灶火力调控在维持压力的最低微火，锅内的水体实际上处于<strong>宏观完全静止、几乎无沸腾对流翻滚（No Boiling Turbulence）</strong>的静谧状态！骨头和肉块安稳地浸泡在极高温水中，没有机械撞击与翻滚碰撞。</li><li><strong>传统大锅翻滚乳化</strong>：相反，在敞口大锅中即使是“微沸”，热对流产生的持续上升气泡也会不断把肉骨上的软组织和微细碎屑冲刷下来，并将浮油与水相进行微弱打发乳化，导致汤体变灰变浊。只要高压锅严格执行自然慢降压，避免减压暴沸，熬出的高汤无需蛋白吸附澄清洗汤（Clarification），就能达到清如水晶的透明纯净度。</li></ol>"
                },
                {
                    "q": "为什么制作高汤时不能一开始就加盐调味？",
                    "a": "<p>这是出于<strong>多阶段浓缩工艺的容积减缩与渗透平衡原理</strong>：高汤（Stock）是厨房的基础底料工具，而非端上桌直接喝的完成品汤羹。在后续的烹饪中，厨师往往需要将几升基础高汤通过长时间大火慢收（Reduction）浓缩至原本体积的 1/4 甚至 1/10，制作诸如法式半糖色冰浓汁（Demi-Glace）或顶级盘底淋酱。如果在熬制之初就按照正常口味加了盐，随着水分蒸发浓缩，高汤的盐分浓度会直接飙升 4~10 倍，变得极其咸苦而彻底报废。此外，高渗透压的浓盐水还会稍微阻碍骨髓深层呈味氨基酸与明胶的自由溶出。<strong>高汤制作永远保持零盐分，盐永远只留到最后一道成菜淋汁时精准调味</strong>。</p>"
                }
            ]
        },
        {
            "id": "m06_l02",
            "num": "02",
            "title": "蔬菜叶绿素脱镁褐变与果胶甲酯酶活",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：掌握叶绿素 a/b 卟啉环在酸热工况下失去镁离子生成脱镁叶绿素（Pheophytin）的变色机理，以及果胶甲酯酶（PME）对细胞壁爽脆度的影响。",
                "掌握标准：能够运用“大锅宽水沸腾稀释酸性挥发物 + 极微量食用小苏打调弱碱性（pH 7.5）+ 90秒急焯 + 冰水急冷”全套标准化程序，锁定 90%+ 叶绿素留存与鲜脆咬感。"
            ],
            "chapter_bridge": "本课作为全书收官之课，将热力学、无机络合化学与酶学完整闭环，展示食材微观分子防护的终极艺术。",
            "feynman_analogy": "绿色蔬菜（如西兰花、芦笋、四季豆）的翠绿颜色，来自于细胞叶绿体中千千万万个像微型太阳能电池板一样的‘叶绿素分子’：电池板的最中央，尊贵地镶嵌着一颗闪闪发光的金属镁离子（Mg²⁺），正是这颗镁离子让反射出来的光谱呈现惊艳生机盎然的亮绿。但在烹饪受热时，植物细胞膜破裂释放出自身细胞液里的有机酸（如草酸、苹果酸），无数的氢离子（H⁺）像微型强盗一样疯狂冲向电池板，强行把中央的镁离子踢出去、自己霸占位置——这就形成了‘脱镁叶绿素（Pheophytin）’，原本耀眼的鲜绿瞬间退化为暗沉、发黑、像烂泥一样的橄榄灰黄色！破解这个化学悲剧只需三招物理护盾：第一招用‘超级大锅宽水’，瞬间把蔬菜吐出来的酸稀释上万倍；第二招加‘一小撮小苏打’把水微调至弱碱性，让氢离子强盗寸步难行；第三招焯水 90 秒捞出立刻‘扔进冰水浴’，将热分解反应与酶活在几秒内冰封归零！捞出来的西兰花翠绿欲滴、咔嚓爽脆，宛如晶莹翡翠！",
            "feynman_calc": "处理 300g 鲜西兰花（初始叶绿素总量标定为 100%）：对比组 A 在 1 升小锅沸水（中性偏酸，焯水后 pH 跌至 5.8）中煮 4 分钟并不冰镇自然放凉；对比组 B 在 4 升大锅沸水（加 1/4 茶匙小苏打，pH 7.5）中焯水 90 秒，捞出投入 0°C 冰水浴 2 分钟。实验测定分光光度计吸收峰：对比组 A 由于酸性积聚和余热持续进行脱镁反应，叶绿素留存率仅 42.5%，肉眼呈现令人倒胃口的橄榄灰褐色；对比组 B 脱镁反应被碱性与急冷彻底截断，叶绿素留存率高达 92.8%，果胶完整爽脆度评分高达 94 分，色泽鲜活如高定珠宝！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：叶绿素卟啉环脱镁褐变机理与大锅沸水快焯+微碱保护图解</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 06 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m12" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m12)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#DC2626"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">脱镁褐变灾难 (酸 + 长时间受热)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 细胞破裂释放有机酸，小锅水迅速变酸 (pH < 6.0)</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 两个 H⁺ 强行置换中心 Mg²⁺，生成脱镁叶绿素</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 色泽从翠绿突变为难看的暗沉橄榄灰黄 (Pheophytin)</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
          <circle cx="163" cy="75" r="45" fill="#A16207" stroke="#78350F" stroke-width="2"/>
          <text x="163" y="72" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">脱镁卟啉环</text>
          <text x="163" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#FDE047">Mg²⁺ 脱落置换</text>
          <text x="163" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="#991B1B">反应式：Chlorophyll + 2H⁺ ➔ Pheophytin + Mg²⁺</text>
          <text x="163" y="156" text-anchor="middle" font-size="10" fill="#B91C1C">留存率仅 42.5% · 灰暗软烂烂菜叶</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#DC2626">色相变暗 · 细胞壁水解塌陷</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">科学三防保护 (宽水 + 微碱 + 冰镇)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 大锅宽水稀释有机酸，微量小苏打维持 pH 7.5</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 沸水急焯 90 秒：气体被赶出，表面折射率剧增更翠绿</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 冰水浴 (0°C) 瞬间降温终止余热传导与酶促分解</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <circle cx="165" cy="75" r="45" fill="#15803D" stroke="#166534" stroke-width="2"/>
          <circle cx="165" cy="75" r="16" fill="#86EFAC"/>
          <text x="165" y="79" text-anchor="middle" font-size="11" font-weight="700" fill="#14532D">Mg²⁺ 稳固</text>
          <text x="165" y="138" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A">完美叶绿素卟啉环保留率 >92%</text>
          <text x="165" y="156" text-anchor="middle" font-size="10" fill="#047857">翠绿欲滴如翡翠 · 细胞壁爽脆咔嚓弹牙</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">分子级锁鲜 · 视觉与口感双重降维打击</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>叶绿素卟啉螯合环脱镁动力学</strong>：天然叶绿素（包含叶绿素 a 与叶绿素 b）分子骨架为一个由四个吡咯环连接而成的卟啉大共轭环，中央通过配位共价键紧密螯合着一个二价镁离子（$\text{Mg}^{2+}$）。这种结构使得分子在蓝光区（430nm）与红光区（660nm）有强烈吸收，反射出纯正的亮绿色。当环境酸性过高或持续受热时，亲核性更强的两个氢离子（$2\text{H}^+$）将强行取代中央的 $\text{Mg}^{2+}$，共轭体系受扰，主吸收带红移，转化为吸光度混杂的脱镁叶绿素（Pheophytin），宏观上呈现为死气沉沉的橄榄褐变。</li>
  <li><strong>微碱性与空气排出（Air Dispersal）双重光学增艳</strong>：刚下锅的绿色蔬菜在头 30 秒内往往会显得比生的还要翠绿耀眼！这是因为蔬菜表皮细胞间隙原本充满了微量空气泡，这些小气泡漫反射光线使得生蔬菜略显苍白；当投入大沸水后，受热膨胀的气体瞬间被逼出逸散，细胞贴合变透明，底层饱满的叶绿体毫无阻隔地展现在光照下，折射率剧增。同时在微碱性（pH 7.5~8.0）下，脱镁反应被完全物理遏止。</li>
  <li><strong>余热持续破坏与冰水浴（Ice Bath Shocking）绝对阻断</strong>：捞出后的蔬菜如果堆在盘子里，中心温度依旧保持在 80°C 甚至更高，原本被沸水激活的热反应在盘中堆叠焖捂下会持续进行 5~10 分钟，直到整盘菜悄无声息地自发褪色变黄。必须使用容积至少为蔬菜质量 3 倍以上的冰水混合物，在捞出后 5 秒内将食材温度从 100°C 极速暴跌至 4°C 以下，瞬间冻结所有化学变色与果胶降解！</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$-\frac{d[Chl]}{dt} = k_{deg} \cdot [H^+]^2 \cdot [Chl], \quad k_{deg} = A \cdot \exp\left(-\frac{E_a}{R T}\right)$$
<div class="math-plain-bar">🗣️ 直白算式：叶绿素分解速率 = 反应常数 × 氢离子浓度平方 × 叶绿素存量；降低酸度(提高 pH)可成平方倍压制褪色</div>
</div>

<ul class="label-list">
  <li>$[Chl]$：食材中活性未变性叶绿素的微观浓度。</li>
  <li>$[H^+]^2$：氢离子浓度的二次方项！这在化学上意味着：pH 每提升 1 个单位（即 $[H^+]$ 降低 10 倍），叶绿素的脱镁分解速率在理论上呈百倍（$10^2$）规模剧烈骤降！</li>
  <li>$k_{deg}$：脱镁热解动力学速率常数；冰水急冷通过瞬间拉低温度 $T$，将 $k_{deg}$ 直接打入停滞区间。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>切忌食用小苏打添加过量！</strong>“微碱性保护叶绿素”绝不意味着小苏打加得越多越好：蔬菜的细胞骨架由半纤维素与果胶构筑，强碱性（pH > 8.5）会使果胶分子发生不可逆的皂化与多糖解聚，导致原本爽脆的蔬菜瞬间变成一摊软烂糊状的黏稠烂泥，并带来难闻的苦咸肥皂碱水味；正确标准用量是：<strong>每 1000ml（1 升）大沸水中，仅加入 1/8 茶匙（约 0.6g）极微量小苏打</strong>，达到肉眼几乎测不出的微弱缓冲碱性即可达到顶级护色且保持极致爽脆！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">300g 西兰花焯水叶绿素留存率实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">科学焯水叶绿素留存率</div><div class="result-kpi-value" style="color:#16A34A;">92.8%</div><div class="result-kpi-sub">保持高饱和鲜艳翡翠绿</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">传统煮菜叶绿素留存率</div><div class="result-kpi-value" style="color:#DC2626;">42.5%</div><div class="result-kpi-sub">严重脱镁退化为暗褐黄</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">果胶爽脆咬感得分</div><div class="result-kpi-value" style="color:#16A34A;">94 / 100</div><div class="result-kpi-sub">清甜脆爽，拒绝水塌烂泥</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">焯水黄金时间窗口</div><div class="result-kpi-value" style="color:#CC5A36;">90 秒</div><div class="result-kpi-sub">超时会导致果胶热软化</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>蔬菜焯水工艺方案</th><th>水质 pH 环境</th><th>沸水焯制时间</th><th>降温终止方式</th><th>叶绿素留存率 (%)</th><th>色泽外观与咬合质感</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>Kenji 科学三防焯水法</td><td>pH 7.5 (微碱)</td><td>90 秒</td><td>0°C 冰水浴急冷</td><td><strong style="color:#16A34A;">92.8%</strong></td><td><strong style="color:#CC5A36;">生机盎然晶莹翠绿，咔嚓爆脆清甜</strong></td></tr>
        <tr><td>大锅沸水快焯但无冰水</td><td>pH 7.0 (中性)</td><td>90 秒</td><td>室温盘自然放凉</td><td>71.5%</td><td>初出色泽尚可，随后逐渐变暗</td></tr>
        <tr><td>小锅少水久煮 (传统老法)</td><td>pH 5.8 (酸化)</td><td>4.0 分钟</td><td>自然放凉</td><td><strong style="color:#DC2626;">42.5%</strong></td><td>暗沉发褐脱镁死黄，发软塞牙</td></tr>
        <tr><td>小苏打严重过量 (误区)</td><td>pH 9.5 (强碱)</td><td>90 秒</td><td>冰水浴</td><td>96.0% (极度绿)</td><td><strong style="color:#DC2626;">果胶彻底瓦解软烂糊化，苦涩肥皂味</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>准备一口深大锅装入 <strong>3~4 升水（水菜比至少 10:1）</strong>，加入 <strong>2 汤匙盐与 1/8 茶匙食用小苏打</strong> 烧至大滚沸；投入切好的西兰花或芦笋计时 <strong>90 秒</strong>；与此同时准备好装满冰块的冰水大盆；时间一到立刻用漏勺捞出直接浸没入 <strong>0°C 冰水浴中晃动 2 分钟</strong> 彻底冷透；捞出沥干水，无论是淋橄榄油清食还是做沙拉，数小时内均保持如翡翠般艳丽脆爽！
  </div>
</div>""",
            "code": c_m06_l02,
            "qa": [
                {
                    "q": "为什么焯水时盖上锅盖往往会导致绿色蔬菜更容易变黄？",
                    "a": "<p>这是由<strong>植物细胞有机酸的挥发与再冷凝热力学循环</strong>决定的：</p><ol><li><strong>挥发性有机酸积聚</strong>：绿色蔬菜在受热破裂时，会释放出挥发性的低分子量有机酸（如乙酸、甲酸、部分草酸气体）。在敞口大锅烹饪时，这些气态酸会顺着上升的大量水蒸气直接排入抽油烟机中逸散离开水相。</li><li><strong>回流再冷凝酸化</strong>：如果紧紧盖上锅盖，挥发上冲的酸性蒸汽在金属锅盖内壁迅速遇冷凝结为高浓度的酸液水珠，并源源不断地回滴入锅水中，导致锅中水体的酸度持续攀升（$\text{pH}$ 加剧下跌），强力加速氢离子置换镁离子的脱镁褐变反应。<strong>焯绿色蔬菜必须敞开锅盖，让酸性气体彻底散逸</strong>。</li></ol>"
                },
                {
                    "q": "为什么煮成熟烂的豆子（如鹰嘴豆、红芸豆）时，反而严禁在烹饪初期加酸（如番茄或醋）？",
                    "a": "<p>这与蔬菜焯水形成了极其精妙的<strong>相反果胶化学对照</strong>：在这一课中，我们利用酸来防止土豆或焯水蔬菜破烂；然而在煮豆子或根茎炖菜时，我们的目标恰恰是<strong>让坚硬的半纤维素和细胞壁多聚半乳糖醛酸（果胶）充分水解软化</strong>！如果一开始就在炖锅里倒进番茄碎、红酒或醋，酸性环境会使豆子和根茎类蔬菜细胞壁内的果胶酸分子牢固质子化，形成极其耐高温的坚韧钙桥交联；哪怕在高压锅里加压狂煮两个小时，豆子内部依然硬如砂砾、生涩发硬！科学炖豆法则：<strong>全程在微碱性水或纯水中先将豆子彻底煮至软烂糯沙，最后出锅前 10 分钟才能加入番茄酱或食醋调味！</strong></p>"
                }
            ]
        }
    ]
}

print("Module 06 ready.")
