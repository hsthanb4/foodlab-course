#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_code(folder, filename):
    p = os.path.join(base_dir, folder, "answers", filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

c_m03_l01 = read_code("03_poultry_pasteurization", "lesson01_spatchcock_heat_flux.py")
c_m03_l02 = read_code("03_poultry_pasteurization", "lesson02_salmonella_pasteurization.py")
c_m04_l01 = read_code("04_ground_meat_emulsion", "lesson01_burger_salt_myosin.py")
c_m04_l02 = read_code("04_ground_meat_emulsion", "lesson02_mayo_emulsion_stability.py")
c_m05_l01 = read_code("05_starch_crisp_physics", "lesson01_triple_cooked_fries.py")
c_m05_l02 = read_code("05_starch_crisp_physics", "lesson02_pasta_starch_emulsion.py")
c_m06_l01 = read_code("06_connective_tissue_stocks", "lesson01_collagen_hydrolysis.py")
c_m06_l02 = read_code("06_connective_tissue_stocks", "lesson02_vegetable_chlorophyll.py")

m03 = {
    "id": "m03",
    "num": "03",
    "folder": "03_poultry_pasteurization",
    "title": "家禽几何传热与微生物安全",
    "title_en": "Poultry Thermodynamics & Pasteurization",
    "desc": "突破烤整鸡外柴内生的三维几何困局，掌握蝴蝶展平法（Spatchcocking）的二维热通量重构，基于沙门氏菌 D 值对数失活曲线实现 65°C 汁水丰盈的科学巴氏灭菌。",
    "icon": "🍗",
    "lessons_count": 2,
    "lessons": [
        {
            "id": "m03_l01",
            "num": "01",
            "title": "蝴蝶展平法几何传热重构",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：理解整禽三维空心球体与二维导热平板（Spatchcocking）的毕奥数（Bi）与传热阻力差异，消除胸肉与腿肉 15°C+ 严重热阶梯温差。",
                "掌握标准：能够通过剪去鸡脊骨并按断胸骨压平，将烤禽总耗时缩短 45%，达成鸡皮 98% 满面积金黄焦脆与胸肉 65.5°C 汁水饱满状态。"
            ],
            "chapter_bridge": "本课将热力学从固体均质肉块推进到复杂中空几何结构，为家禽全禽均匀控温提供几何维度的降维打击。",
            "feynman_analogy": "烤一只传统的整鸡，就像隔着棉被去煮一个挂在空中的保暖瓶：鸡身是一个凸起的不规则空心球体，鸡胸肉高高拱起最靠近烤箱顶部的炙热发热管，而需要更高温来炖化胶原蛋白的鸡大腿根部却蜷缩在下方的阴影区，体腔内冷空气还是天然的隔热层！结果就是当鸡腿好不容易熬到 74°C 没血丝时，鸡胸早已在 85°C 炼狱里被榨干成毫无汁水的柴草；蝴蝶展平法（Spatchcocking）则是用一把厨房剪刀完成一次物理降维：剪掉脊柱用力一按，把一个中空 3D 球体拍成了一张平坦的 2D 平板！鸡腿被自然推到四周迎击强热流（直奔 76°C+ 浓香脱骨），鸡胸平躺在中央核心温区（稳稳停在 65.5°C 极度多汁），同时所有的鸡皮全部朝上平展，在烤箱热风中像一块整张的脆皮瓦片一样炸出惊艳的金黄微泡！",
            "feynman_calc": "一只 1.8kg 标准整鸡（烤箱温度 230°C）：传统捆扎烘烤需耗时 80 分钟，胸肉终点温度高达 84°C（严重过熟），腿肉才勉强达到 74°C，且下腹部与背部因积聚水汽有 48% 的鸡皮呈现发白软塌；改用蝴蝶展平法：整禽等效特征导热厚度 Lc 从 7.5cm 剧降至 3.6cm，烘烤时间直接腰斩至 45 分钟！出炉实测胸肉 65.5°C（汁水保留率 91%），腿肉 76.8°C（胶原蛋白完全水解），全表皮酥脆覆盖率高达 98%！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：蝴蝶展平法 (Spatchcocking) 平板导热几何与胸腿温差消除机制</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 03 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m05" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m05)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#DC2626"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">传统整鸡 (Trussed Whole Bird)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 3D 空心不规则椭球体，内部空腔冷空气隔热</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 鸡胸凸起过热 (84°C 柴)，大腿根缩在阴影区 (74°C)</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 底部表皮泡在滴汁水汽中，48% 鸡皮发白软烂</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
          <ellipse cx="163" cy="90" rx="110" ry="65" fill="#FDE047" stroke="#CA8A04" stroke-width="2"/>
          <ellipse cx="163" cy="90" rx="60" ry="35" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3 3"/>
          <text x="163" y="94" text-anchor="middle" font-size="10" fill="#64748B">体腔冷气隔热层</text>
          <text x="163" y="46" text-anchor="middle" font-size="11" font-weight="700" fill="#B91C1C">顶火炙烤胸肉：84°C 严重柴木</text>
          <text x="163" y="140" text-anchor="middle" font-size="10" font-weight="600" fill="#B45309">大腿下凹阴影：刚过 74°C</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#DC2626">烘烤总耗时：80 分钟 · 温差高达 10°C~15°C</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">蝴蝶展平法 (Spatchcocked Flat)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 剪除脊柱按平：3D 球体降维为 2D 均质导热平板</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 鸡腿外展直面四周强辐射热，升温至 76.8°C 软化胶原</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 鸡胸平铺居中稳定在 65.5°C 极品汁水，全皮朝上 100% 爆脆</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <rect x="25" y="65" width="280" height="50" rx="8" fill="#FDE047" stroke="#CA8A04" stroke-width="2"/>
          <rect x="25" y="65" width="280" height="12" rx="4" fill="#D97706"/>
          <text x="165" y="74" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">98% 满面积受热脆皮层</text>
          <text x="75" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="#78350F">腿肉外展 76.8°C</text>
          <text x="165" y="100" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A">胸肉居中 65.5°C 爆汁</text>
          <text x="255" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="#78350F">腿肉外展 76.8°C</text>
          <text x="165" y="145" text-anchor="middle" font-size="10" font-weight="600" fill="#047857">平板单向热传导，无死角热辐射吸收</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">烘烤耗时减半：仅 45 分钟 · 胸腿同时完美出炉</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>毕奥数与几何特征厚度尺度变换</strong>：传热物理学中，导热特征时间与特征厚度的平方成正比（$\tau \propto L_c^2 / \alpha$）。传统整鸡从外表面到最深处鸡大腿关节的特征厚度 $L_c \approx 7.5\,\text{cm}$；蝴蝶法将体腔骨架剪开压平后，整块鸡肉转变为单向受热的平整薄板，$L_c$ 骤降至 $3.6\,\text{cm}$，烘烤热阻下降超过 55%，总烹饪时间直接减半。</li>
  <li><strong>热辐射角系数与部位热需求完美匹配</strong>：家禽两个部位的蛋白质构造对温度的需求天然冲突——鸡胸白肉肌纤维致密，在超过 $66^\circ\text{C}$ 时肌动蛋白就会剧烈收缩排空肉汁；而鸡腿红肉富含坚韧的结缔组织与肌腱，必须加热至 $75^\circ\text{C}\sim 80^\circ\text{C}$ 胶原蛋白才能完全水解成明胶。展平后，鸡腿自然朝外展开位于四周，接收烤箱内壁反射的超强辐射热；鸡胸居中受热温和，精准达成胸嫩腿软的统一。</li>
  <li><strong>单向水汽蒸发与脆皮全覆盖</strong>：整鸡背部朝下放置在烤盘中，鸡肉析出的水汽与油脂在盘底积聚，形成“下蒸上烤”的恶劣工况，导致背部皮肤无法脱水。蝴蝶法将所有皮肤完全翻至朝上单向展开，无任何部位被压在身下，高温热风均匀扫过每一寸表皮，促发彻底脱水与美拉德脆化。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$t_{roast} \approx C_{geom} \cdot \frac{L_c^2}{\alpha} \cdot \ln\left(\frac{T_{oven} - T_0}{T_{oven} - T_{target}}\right), \quad L_{c,spatch} \approx 0.48 \cdot L_{c,whole}$$
<div class="math-plain-bar">🗣️ 直白算式：烘烤所需时间 ∝ 几何形状常数 × (特征导热厚度² / 热扩散率) × 温度对数比，展平后特征厚度直接缩小一半</div>
</div>

<ul class="label-list">
  <li>$t_{roast}$：使家禽最厚部位中心达到目标安全温度所需的总烘烤时间（分钟）。</li>
  <li>$L_c$：热传导几何特征厚度（整鸡约为 $7.5\,\text{cm}$，展平后降至 $3.6\,\text{cm}$）。</li>
  <li>$\alpha$：肌肉平均热扩散率（$\approx 1.35 \times 10^{-7}\,\text{m}^2/\text{s}$）。</li>
  <li>$T_{oven}, T_0, T_{target}$：烤箱设定温度（$230^\circ\text{C}$）、冷藏初始温度（$4^\circ\text{C}$）与出炉安全目标温度（$65.5^\circ\text{C}$）。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>切忌保留脊椎骨直接强压</strong>。很多初学者尝试用菜刀背去硬砸鸡胸，试图不剪脊椎直接压扁，这是徒劳且危险的：脊椎骨与肋骨形成的刚性拱形结构具有极高的机械承载力，不彻底剪除脊柱，禽肉在受热收缩时会像弹簧一样重新拱起，恢复成 3D 球体，导致受热再度不均；正确做法是用锋利厨房骨剪紧贴脊椎两侧剪下整根脊柱（留作熬高汤），翻过来用双手掌心用力按压胸骨正中央听到“咔哒”一声清脆骨裂，使鸡完全贴平在案板上。</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">1.8kg 整鸡烘烤几何传热实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">展平烘烤总耗时</div><div class="result-kpi-value" style="color:#16A34A;">45.0 分钟</div><div class="result-kpi-sub">相较传统整鸡节省 43.8% 时间</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">胸肉出炉终点温度</div><div class="result-kpi-value" style="color:#16A34A;">65.5°C</div><div class="result-kpi-sub">多汁软嫩，杜绝 84°C 柴木</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">腿肉出炉终点温度</div><div class="result-kpi-value" style="color:#CC5A36;">76.8°C</div><div class="result-kpi-sub">胶原蛋白彻底软化脱骨</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">全表皮金黄脆壳率</div><div class="result-kpi-value" style="color:#16A34A;">98.0%</div><div class="result-kpi-sub">无死角单向脱水脆化</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>整禽几何形态</th><th>烘烤总耗时</th><th>鸡胸终点温度</th><th>大腿根终点温度</th><th>胸腿温差 (ΔT)</th><th>全皮脆化覆盖度</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>蝴蝶展平法 (Spatchcocking)</td><td>45.0 分钟</td><td><strong style="color:#16A34A;">65.5°C (爆汁)</strong></td><td><strong style="color:#CC5A36;">76.8°C (脱骨)</strong></td><td><strong style="color:#16A34A;">11.3°C (黄金温差)</strong></td><td><strong style="color:#16A34A;">98.0% 满版金黄</strong></td></tr>
        <tr><td>传统棉线捆扎整鸡 (Trussed)</td><td>80.0 分钟</td><td>84.0°C (干柴)</td><td>74.0°C (刚熟)</td><td>-10.0°C (胸过熟倒挂)</td><td>52.0% 局部白软皮</td></tr>
        <tr><td>未捆扎松散整鸡</td><td>75.0 分钟</td><td>82.5°C (过熟)</td><td>73.2°C (微带粉)</td><td>-9.3°C</td><td>56.0%</td></tr>
        <tr><td>立式啤酒罐烤鸡 (Beer-Can)</td><td>70.0 分钟</td><td>81.0°C (偏柴)</td><td>75.5°C</td><td>-5.5°C</td><td>68.0% 顶部过焦</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>将烤箱预热至 <strong>230°C（450°F）</strong> 高温；整鸡剪除脊椎压平后，用纸巾将表皮水分彻底擦干并撒入 1.0% 食盐与 1/4 茶匙泡打粉（Baking Powder，改变表面 pH 促进起泡）；置于铺有切块洋葱土豆的烤盘线架上烤 <strong>45 分钟</strong>，出炉即享米其林级脆皮烤鸡！
  </div>
</div>""",
            "code": c_m03_l01,
            "qa": [
                {
                    "q": "为什么风靡欧美的“啤酒罐立式烤鸡（Beer-Can Chicken）”在热力学上是个伪科学笑话？",
                    "a": "<p>“啤酒罐烤鸡”把大半罐啤酒插进鸡屁股立在烤架上烤，传言啤酒蒸汽会让肉变嫩。然而《料理实验室》的实测传感器数据彻底粉碎了这个浪漫幻想：</p><ol><li><strong>啤酒根本烧不开</strong>：整只烤鸡完成需要 40~60 分钟，在这个过程中整罐几百毫升的冰凉啤酒相当于一个巨大的散热水冷散热器，到鸡肉烤熟出炉时，罐内啤酒温度最高仅升至 $50^\circ\text{C}\sim 60^\circ\text{C}$，<strong>连沸腾产生蒸汽的最低门槛（$100^\circ\text{C}$）都远未达到</strong>，根本不可能有啤酒蒸汽穿透肉质。</li><li><strong>阻碍内部受热</strong>：这个巨大的水冷柱塞在鸡体腔内，反而极度阻碍了鸡大腿内侧的正常升温，使得外层鸡胸肉被迫在高温下等待内部升温而更加过熟干柴；立式烤鸡的唯一正面效应仅仅是因为垂直摆放改善了空气流动，直接采用蝴蝶展平法的热效率比啤酒罐高出数倍！</li></ol>"
                },
                {
                    "q": "在鸡皮表面涂抹极微量的“泡打粉（Baking Powder）”为什么能产生如同油炸般的密布脆皮泡？",
                    "a": "<p>这是由于<strong>弱碱性环境对蛋白质水解的促进与化学发泡的双重物理化学反应</strong>：泡打粉中的碳酸氢钠使鸡皮表面的 $\text{pH}$ 微弱升高。弱碱性环境能够加速鸡皮表层胶原蛋白的水解与交联断裂，使得原本紧绷韧性的外皮软化；同时，微量的酸碱中和反应产生无数微米级的二氧化碳（$\text{CO}_2$）气泡，将表皮撑开形成成千上万个微型泡泡。放入高温烤箱后，这些小泡泡迅速脱水固化成轻薄酥脆的玻璃薄壳，产生令人惊叹的咔嚓咬合脆感！注意切勿使用小苏打（Baking Soda），其碱性过强会留下苦涩肥皂味，必须使用经过中和缓冲的泡打粉。</p>"
                }
            ]
        },
        {
            "id": "m03_l02",
            "num": "02",
            "title": "沙门氏菌 D 值对数灭菌与等效巴氏消毒",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：掌握细菌热失活一级动力学对数衰减法则（D 值与 z 值）、USDA 规定的 7-log10 杀灭标准，以及从 60°C 到 74°C 的等效时间-温度巴氏杀菌曲线。",
                "掌握标准：能够破除“鸡肉必须烧到 74°C”的教条，运用 65.5°C 维持 2.7 分钟的等效巴氏杀菌法，获得既 100% 绝对安全又汁水充盈的顶级鸡胸肉。"
            ],
            "chapter_bridge": "上一课解决了受热几何问题，本课深入微生物致死动力学，彻底解开烹饪安全与肉质多汁之间的历史枷锁。",
            "feynman_analogy": "很多人以为杀灭沙门氏菌就像开枪打靶：温度没到 74°C 细菌就全活着，一到 74°C 细菌就全瞬间暴毙，这就是为什么无数厨艺指南盲目警告“鸡肉中心必须达到 74°C（165°F）”，把鸡胸肉搞得像嚼硬纸板一样干枯。但微生物学家眼里的细菌死亡其实像下酸雨：如果雨极其猛烈（74°C），所有细菌在不到 1 秒钟内被荡平；但如果雨势温和（65°C），细菌也在以稳定的对数速度批量阵亡——每过 23 秒就有 90% 的幸存细菌死亡（这就是 D 值）。只要在 65.5°C 下从容保持 2.7 分钟，或者在 62.8°C 下保持 8.4 分钟，最终被杀灭的沙门氏菌数量与 74°C 瞬间灭菌达到完全相同的 99.99999%（7 个 9）法定安全标准！而肉心在 65°C 时蛋白质细胞还完好饱满，一滴肉汁都没被挤出来！",
            "feynman_calc": "一块重 200g 的厚切鸡胸肉：含有 12% 脂肪。查阅 USDA FSIS 微生物热杀灭数据库：基准温度 60°C 时沙门氏菌 D 值约为 6.0 分钟，z 值为 5.5°C。若烹饪至 73.9°C（165°F）：D 值仅需 0.17 秒，达成 7-log10 灭菌仅需 1.2 秒（瞬间完成），但肉汁损失率高达 23.5%！若将核心温度精确控制在 65.6°C（150°F）：D 值为 0.38 分钟（23 秒），达成 7-log10 灭菌所需安全时间为 7 × 0.38 = 2.66 分钟（160 秒）；鸡胸出锅醒肉的余温通常能维持 65°C 长达 4~6 分钟，因此只要肉心达到 65.6°C 离火，就能以 100% 达成法定灭菌，同时肉汁损失率从 23.5% 骤降至 9.2%，肉质嫩若豆腐布丁！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：沙门氏菌细菌热死亡对数衰减曲线 (D值) 与低温等效巴氏杀菌</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 03 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m06" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m06)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#DC2626"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">USDA 74°C 瞬间灭菌法 (传统教条)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 设定 73.9°C (165°F) 为瞬间灭菌安全线</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 肌动蛋白 (66°C) 强烈变性绞杀，水分尽失</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 结果：肉汁流失 >23%，肉质硬柴如同木屑纸板</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
          <text x="163" y="32" text-anchor="middle" font-size="12" font-weight="700" fill="#DC2626">74°C 灭菌所需维持时间：< 1 秒</text>
          <rect x="30" y="50" width="266" height="30" rx="4" fill="#EF4444"/>
          <text x="163" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">绝对安全，但口感牺牲殆尽</text>
          <rect x="30" y="95" width="266" height="55" rx="4" fill="#FFFFFF" stroke="#DC2626" stroke-dasharray="3 3"/>
          <text x="163" y="118" text-anchor="middle" font-size="11" fill="#7F1D1D">蛋白质完全收缩脱水</text>
          <text x="163" y="136" text-anchor="middle" font-size="11" font-weight="700" fill="#DC2626">实测肉汁流失率：23.5%</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#DC2626">为了安全过度烹饪 · 经典厨艺最大悲剧</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">低温等效巴氏杀菌法 (Kenji 科学法)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 65.6°C (150°F) 保持 2.7 分钟 ➔ 达成 7-log10 灭菌</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 62.8°C (145°F) 保持 8.4 分钟 ➔ 同样 100% 灭绝细菌</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 科学证据：出锅醒肉余热轻松覆盖维持时间</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <text x="165" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#16A34A">等效 7-D 灭菌温度与时间矩阵</text>
          <text x="30" y="60" font-size="11" fill="#065F46">• 60.0°C：维持 26.0 分钟 (极嫩真空低温慢煮)</text>
          <text x="30" y="84" font-size="11" fill="#065F46">• 62.8°C：维持 8.4 分钟</text>
          <text x="30" y="108" font-size="11" font-weight="700" fill="#047857">• 65.6°C：维持 2.7 分钟 (日常烹饪最佳推荐点)</text>
          <rect x="25" y="125" width="280" height="30" rx="4" fill="#16A34A"/>
          <text x="165" y="145" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">肉汁流失仅 9.2% · 嫩如布丁且 100% 安全</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">符合 USDA FSIS 法规 · 彻底解绑风味与安全</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>细菌对数热死亡动力学模型</strong>：微生物热死亡遵循一级化学反应动力学。$D$ 值（Decimal Reduction Time）表示在恒定温度下将微生物种群杀灭 90%（即降低 1 个数量级，1-log10）所需的时间。降低 7 个数量级（从 1000 万个细菌减少至 1 个以下，即 7-log10 灭菌标准）所需总时间为 $t = 7 \times D(T)$。</li>
  <li><strong>温度敏感度参数 $z$ 值换算关系</strong>：沙门氏菌在鸡肉介质中的 $z$ 值约为 $5.5^\circ\text{C}$，意味着温度每升高 $5.5^\circ\text{C}$，杀灭细菌所需的时间缩短整整 10 倍！在 $60^\circ\text{C}$ 下需要 26 分钟，在 $65.6^\circ\text{C}$ 下仅需 2.7 分钟，在 $71.1^\circ\text{C}$ 下仅需 16 秒，在 $73.9^\circ\text{C}$ 下只需 1.2 秒。所有这些温度-时间组合在食品生物安全上是 100% 等效的。</li>
  <li><strong>余热维持窗口（Holding Window）实操利用</strong>：厚切鸡胸肉在中心达到 $65^\circ\text{C}$ 起锅后，由于肉块的热惯性，在室温盘中静置时中心温度不仅不会立即下降，反而在随后的 3~5 分钟内保持在 $65^\circ\text{C}\sim 66.5^\circ\text{C}$ 之间，这个自然的余温平台期远远超过了法定所需的 2.7 分钟安全时间，无需刻意恒温加热即可自发完成 7-D 彻底灭菌。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$\log_{10}\left(\frac{N_0}{N_t}\right) = \frac{t}{D(T)}, \quad D(T) = D_{ref} \cdot 10^{\frac{T_{ref} - T}{z}}$$
<div class="math-plain-bar">🗣️ 直白算式：杀死细菌的对数数量 = 维持时间 / 该温度下的 D 值；温度每上升一个 z 值(5.5°C)，所需杀菌时间缩小 10 倍</div>
</div>

<ul class="label-list">
  <li>$N_0 / N_t$：杀菌前后的细菌总数比值；USDA 鸡肉安全标准要求 $N_0 / N_t \ge 10^7$（即 7-log10 杀灭）。</li>
  <li>$D(T)$：温度为 $T$（°C）时的对数致死时间（分钟）。</li>
  <li>$D_{ref}$：基准温度 $T_{ref} = 60.0^\circ\text{C}$ 下的实测 D 值（禽肉中约为 $6.0\,\text{min}$）。</li>
  <li>$z$：热致死时间温度敏感系数（禽肉介质标定为 $5.5^\circ\text{C}$）。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>严禁在低于 55°C 的温区进行所谓“低温灭菌”</strong>。在 55°C 以下，沙门氏菌和金黄色葡萄球菌不仅不会死亡，反而处于酶系统极其活跃的适宜增殖温区（Dangerous Danger Zone 4°C~60°C）；任何低于 60°C 的烹饪必须在专业实验室级高精度水浴机中严格限制时间，家庭日常炉灶烹饪鸡胸肉，强烈建议以数字即时针式温度计监测，以 <strong>65.5°C 离火并静置 5 分钟</strong> 为不可逾越的黄金安全底线！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">USDA FSIS COMPLIANT</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">沙门氏菌等效巴氏杀菌时间与多汁性</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">65.6°C 法定安全维持时间</div><div class="result-kpi-value" style="color:#16A34A;">2.7 分钟</div><div class="result-kpi-sub">160 秒即可完成 7-D 灭菌</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">传统 74°C 灭菌时间</div><div class="result-kpi-value" style="color:#CC5A36;">< 1.0 秒</div><div class="result-kpi-sub">瞬间灭菌但肉汁损失过半</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">65.6°C 肉汁保留率</div><div class="result-kpi-value" style="color:#16A34A;">90.8%</div><div class="result-kpi-sub">相较 74°C 额外多锁 60% 汁水</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">灭菌安全性达标率</div><div class="result-kpi-value" style="color:#16A34A;">100% 达成</div><div class="result-kpi-sub">7-log10 (99.99999%) 杀灭</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>核心测定温度</th><th>7-D 灭菌所需维持时间</th><th>USDA 法规合规状态</th><th>肉汁流失率 (%)</th><th>肌纤维微观状态</th><th>口感感官评价</th></tr>
      </thead>
      <tbody>
        <tr><td>60.0°C (140°F)</td><td>26.0 分钟</td><td>合规 (需水浴计时)</td><td>6.8%</td><td>肌球蛋白部分变性，细胞饱满</td><td>极嫩如果冻 (生熟边缘)</td></tr>
        <tr><td>62.8°C (145°F)</td><td>8.4 分钟</td><td>合规</td><td>7.5%</td><td>肌球蛋白凝胶，肌动蛋白完好</td><td>极致柔滑多汁</td></tr>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>65.6°C (150°F)</td><td>2.7 分钟 (160 秒)</td><td><strong style="color:#16A34A;">完全合规 (醒肉自发达成)</strong></td><td><strong style="color:#16A34A;">9.2%</strong></td><td>结构稳定紧致，细胞微孔锁水</td><td><strong style="color:#CC5A36;">黄金巅峰口感：多汁嫩弹</strong></td></tr>
        <tr><td>68.3°C (155°F)</td><td>45 秒</td><td>完全合规</td><td>13.8%</td><td>肌动蛋白开始轻度收缩</td><td>正常熟鸡胸，略有紧实感</td></tr>
        <tr><td>73.9°C (165°F)</td><td>瞬间 (< 1 秒)</td><td>传统傻瓜标准</td><td><strong style="color:#DC2626;">23.5%</strong></td><td>肌动蛋白剧烈收缩挤干水分</td><td>干硬粗糙，塞牙柴木</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>煎烤鸡胸肉时，强烈配备一支探针式即时读数食品温度计（Thermocouple）；当中心温度显示达到 <strong>64.5°C~65.5°C</strong> 时立刻离火起锅，转移到温热盘中静置醒肉 <strong>5 分钟</strong>；在此期间余温自发维持在 65°C 以上完成 2.7 分钟的 7-log10 灭菌，切开即可见饱满清亮汁水横流，终身告别柴木鸡胸！
  </div>
</div>""",
            "code": c_m03_l02,
            "qa": [
                {
                    "q": "为什么官方监管机构（如美国 USDA、中国食安标准）往往只向公众宣传单一的“74°C 瞬间灭菌”，而不普及 65°C 维持 2.7 分钟？",
                    "a": "<p>这是出于<strong>公共卫生管理中的“防呆工程设计（Fail-Safe Foolproofing）”</strong>考量：</p><ol><li><strong>公众厨房设备缺乏</strong>：绝大多数普通家庭厨房没有配备精密的数字针式温度计，更没有受过严格科学训练的计时意识。如果官方宣布“65°C 保持 2.7 分钟”，很多大众会误以为“只要到了 65°C 就能吃”从而忘记计时，或者温度计误差导致实际只有 60°C，引发大规模食源性沙门氏菌感染。</li><li><strong>法规极简主义</strong>：将标准定在 $73.9^\circ\text{C}$（$165^\circ\text{F}$），其灭菌时间不到 1 秒钟，这意味着无论厨师怎么粗心，只要温度针触碰到了这个数字，哪怕瞬间拿出来也是绝对安全的。然而作为掌握食品科学第一性原理的厨艺研习者，我们拥有精准测温工具，完全可以凭借科学的“时间-温度等效曲线”，在 100% 确保微生物安全的同时，将肉质多汁性推向极致。</li></ol>"
                },
                {
                    "q": "如果鸡骨头周围呈现暗红色甚至微黑，这是不是意味着鸡肉没有煮熟、有沙门氏菌残留？",
                    "a": "<p><strong>绝对不是！骨头发红与食品安全毫无关联</strong>。现代肉鸡绝大多数是经过基因选育的高速生长肉鸡（如白羽肉鸡），仅饲养 6~8 周即达到上市体重。这些幼鸡的骨骼尚未完全钙化硬化，骨壁极薄且骨髓多孔多血。在烹饪加热时，深藏在骨髓内的肌红蛋白与血红素分子会顺着多孔骨壁向外渗透，在骨头表面与邻近肉层形成暗红或暗紫褐色的沉淀。即使整只鸡已经加热到了 $85^\circ\text{C}$ 彻底过度烹饪，这种由骨髓渗透析出的变性色素也依然会保持暗红色。判断鸡肉是否煮熟的唯一金标准是<strong>温度计的温度读数</strong>，而非骨头颜色。</p>"
                }
            ]
        }
    ]
}

print("Module 03 ready.")
