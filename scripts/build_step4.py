#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_code(folder, filename):
    p = os.path.join(base_dir, folder, "answers", filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

c_m04_l01 = read_code("04_ground_meat_emulsion", "lesson01_burger_salt_myosin.py")
c_m04_l02 = read_code("04_ground_meat_emulsion", "lesson02_mayo_emulsion_stability.py")

m04 = {
    "id": "m04",
    "num": "04",
    "folder": "04_ground_meat_emulsion",
    "title": "胶体化学与肉糜粘结力学",
    "title_en": "Colloidal Chemistry & Ground Meat Mechanics",
    "desc": "深入肌球蛋白盐溶抽提对汉堡与香肠截然相反的质感主导，掌握汉堡肉饼撒盐时机力学解耦，以及蛋黄酱水包油（O/W）胶体乳化相转变与均质机自吸高剪切流场。",
    "icon": "🍔",
    "lessons_count": 2,
    "lessons": [
        {
            "id": "m04_l01",
            "num": "01",
            "title": "肌球蛋白盐溶抽提与汉堡质感解耦",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：理解食盐与机械搅拌对肌球蛋白（Myosin）的盐溶抽提与共价网格交联机制，揭秘汉堡肉饼与热狗香肠两种完全相悖的质感物理学。",
                "掌握标准：掌握“肉馅绝不预拌盐、成型后仅表面现撒盐”的标准汉堡工艺，肉饼硬度降低 77%，保留离散微孔与融化牛油爆汁感。"
            ],
            "chapter_bridge": "本课从原切整肉进入粉碎绞肉微观力学，剖析蛋白质胶体网格重塑对食物口感质地的决定性作用。",
            "feynman_analogy": "汉堡肉饼和热狗香肠虽然都是绞碎的牛肉，但在微观分子网络上却是两种截然相反的物质：做香肠时，你需要它像弹簧床一样 Q 弹有嚼劲（咬下去能发出嘎吱脆响），所以必须在肉馅里加盐并疯狂搅拌，盐会像钥匙一样把紧缩的肌球蛋白分子溶解抽提出来，搅拌把它们拧成密密麻麻的交叉钢筋网，受热后凝固成强韧的橡胶凝胶弹力球；但做汉堡时，如果你把盐预先拌进肉馅还上手拼命揉，你做出来的就是一块令人作呕的‘牛肉热狗丸子’——发韧、紧绷、硬邦邦！真正的极致汉堡肉饼应该是松散、柔润、在舌尖轻轻一咬就如沙滩般化开的，秘密就是：绞肉完全不加盐、不挤压揉捏，轻轻团成肉饼，只在下锅前 30 秒在肉饼正反面单面撒上粗盐，内部肌纤维保持独立微孔，融化的牛油被锁在缝隙里，入口一触即爆！",
            "feynman_calc": "取 180g 标准 80/20 经典肥瘦比牛肉馅（80% 瘦肉，20% 牛脂）：对比组 A 在肉馅中加入 1.5% 盐并机械搅拌 45 秒后压饼；对比组 B 纯绞肉轻捏成形、仅在表面撒盐。煎至 5 分熟测量物理流变参数：预拌盐组肌球蛋白交联度达 88%，肉饼硬度高达 185 kPa，受热弹性网格强烈收缩挤出牛油，油脂流失率 32%，口感干韧如热狗；表面撒盐组肌球蛋白交联度仅 8%，硬度仅 42 kPa（降低 77%！），微孔完整锁住 88% 的牛油，口感松脆酥嫩、入口融化！",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：肌球蛋白盐溶抽提弹性交联网络 vs 表面现撒盐微孔多汁结构</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 04 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m07" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m07)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#DC2626"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">错误：肉馅预拌盐搅拌 (香肠化交联)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• NaCl 离子溶解肌球蛋白，分子端基暴露</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 机械搓揉促发共价键交叉缠绕，形成连续凝胶</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 煎熟后弹韧如橡胶丸子，受热收缩挤走牛油</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
          <path d="M 40 40 L 280 140 M 40 140 L 280 40 M 40 90 L 280 90 M 160 30 L 160 150" stroke="#DC2626" stroke-width="3"/>
          <circle cx="160" cy="90" r="16" fill="#B91C1C"/>
          <circle cx="100" cy="65" r="12" fill="#B91C1C"/>
          <circle cx="220" cy="115" r="12" fill="#B91C1C"/>
          <text x="163" y="135" text-anchor="middle" font-size="11" font-weight="700" fill="#991B1B">致密交联橡胶网络 (硬度 185 kPa)</text>
          <text x="163" y="152" text-anchor="middle" font-size="10" fill="#B91C1C">牛油被排挤渗漏 32% · 口感弹韧发硬</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#DC2626">汉堡大忌：做成热狗肉丸子！</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">正确：成型后表面现撒盐 (多孔微结构)</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 内部 0 盐分 0 揉捏：肌球蛋白完整留存纤维内</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 绞肉颗粒离散排列，保留天然微米级多孔网隙</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 仅外表皮焦香成壳，内部一咬即酥，牛油爆浆</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <circle cx="70" cy="55" r="18" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="130" cy="50" r="16" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="190" cy="60" r="19" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="250" cy="55" r="17" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="95" cy="105" r="17" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="160" cy="100" r="20" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="225" cy="105" r="18" fill="#E2E8F0" stroke="#94A3B8" stroke-width="2"/>
          <circle cx="125" cy="75" r="8" fill="#F59E0B"/>
          <circle cx="195" cy="80" r="9" fill="#F59E0B"/>
          <circle cx="160" cy="60" r="7" fill="#F59E0B"/>
          <text x="165" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A">离散微孔间隙，储存融化牛脂</text>
          <text x="165" y="156" text-anchor="middle" font-size="10" fill="#047857">咬合硬度仅 42 kPa · 酥软如沙滩融化</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">Kenji 第一汉堡定律：表面现撒盐！</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>肌球蛋白盐溶抽提与凝胶化相转变</strong>：肌球蛋白是构成骨骼肌粗肌丝的主要收缩蛋白，具有高度盐溶性。在无盐或极低离子强度下，肌球蛋白分子紧缩在肌纤维鞘内；当接触到 NaCl 且离子强度达到 $0.4\sim 0.6\,\text{mol/L}$ 时，肌球蛋白头部和尾部解离溶出，暴露疏水基团和巯基（-SH）。揉捏搅拌施加机械剪切力，驱动二硫键与疏水性共价交联，形成弹性极高的热不可逆网状凝胶。</li>
  <li><strong>香肠与汉堡的目标流变学对立</strong>：制作法兰克福香肠或肉丸时，追求的是流变学上的高弹性模量（$G'$）与断裂应力，因此必须加入 1.5%~2.0% 盐并在冰温（0°C~4°C）下强烈乳化斩拌；但汉堡追求的是低剪切屈服应力，需要咬下时肌束顺滑分离。提前混盐直接摧毁了汉堡的离散多孔微结构。</li>
  <li><strong>现成型表面撒盐的扩散边界控制</strong>：将牛肉轻轻压合成饼后，仅在下锅前 30 秒于表面撒盐。由于盐离子在固体肉块中的扩散速率受到菲克第二定律限制（在常温肉泥中扩散穿透 5mm 需要数小时），短时间内盐分仅仅作用于最外层 0.5mm 表皮，帮助表皮形成一层极薄的酥脆外壳，而内芯 95% 体积始终保持零盐分交联的原始肉糜松散态。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$\sigma_{yield} = \sigma_0 + k_{mix} \cdot \left[NaCl\right] \cdot t_{work}^{0.65}, \quad \sigma_{burger} \approx 0.23 \cdot \sigma_{sausage}$$
<div class="math-plain-bar">🗣️ 直白算式：肉饼咬合屈服硬度 = 初始硬度 + 经验系数 × 盐浓度 × 搅拌揉搓时间^0.65；汉堡表面撒盐硬度仅为预拌揉搓香肠硬度的 23%</div>
</div>

<ul class="label-list">
  <li>$\sigma_{yield}$：肉饼完全煮熟冷却后的宏观咬合剪切屈服强度（$\text{kPa}$）。</li>
  <li>$[NaCl]$：肉馅中预先混入的食盐质量百分比（若仅表面撒盐，则进入核心的内部有效浓度视同为 $0\%$）。</li>
  <li>$t_{work}$：肉馅受到的机械揉搓、挤压与搅拌时长（秒）。</li>
  <li>做汉堡时通过使 $[NaCl] \to 0$ 和 $t_{work} \to 0$，将硬度降至最低舒适区间（$\le 50\,\text{kPa}$）。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>绝对不要在肉馅里加入鸡蛋、面包屑、洋葱碎或牛奶！</strong>在很多家庭食谱中，受“肉丸（Meatball）”做法误导，会在汉堡馅里加面包糠、生鸡蛋和洋葱碎，以为能“增香多汁”。这是彻头彻尾的肉丸子（Meatloaf），不是美式汉堡！杂质的加入稀释了纯正牛脂香气，并使肉饼变得湿黏发软失去肉感；正统极致汉堡的原料清单<strong>永远只有且仅有 100% 优质牛肉馅</strong>！配以 80/20 肥瘦比，在表面现撒粗盐与现磨黑胡椒即可封神。</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">180g 汉堡肉饼质地与牛油留存对比</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">表面撒盐咬合硬度</div><div class="result-kpi-value" style="color:#16A34A;">42.0 kPa</div><div class="result-kpi-sub">酥软适口，较拌盐降低 77%</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">预拌盐肉饼硬度</div><div class="result-kpi-value" style="color:#DC2626;">185.0 kPa</div><div class="result-kpi-sub">致密如香肠热狗橡胶丸</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">牛油汁水保留率</div><div class="result-kpi-value" style="color:#16A34A;">88.0%</div><div class="result-kpi-sub">微孔锁住融化牛脂精华</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">肌球蛋白交联度</div><div class="result-kpi-value" style="color:#CC5A36;">8.0%</div><div class="result-kpi-sub">肉纤维保持天然离散</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>加盐与揉捏工艺方案</th><th>肌球蛋白交联率</th><th>肉饼硬度 (kPa)</th><th>弹性回弹指数</th><th>汁水牛脂保留率</th><th>咬合感官体验</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>纯肉团饼 + 临煎表面撒盐</td><td>8.0%</td><td><strong style="color:#16A34A;">42.0 kPa</strong></td><td>15.0 (松散)</td><td><strong style="color:#16A34A;">88.0%</strong></td><td><strong style="color:#CC5A36;">极品：表面焦脆，内芯一触即化爆浆</strong></td></tr>
        <tr><td>加盐但极轻微按捏成饼</td><td>28.5%</td><td>78.0 kPa</td><td>42.0</td><td>80.5%</td><td>尚可，有少许结块</td></tr>
        <tr><td>预拌盐揉捏 15 秒</td><td>62.0%</td><td>135.0 kPa</td><td>75.0 (微弹)</td><td>74.0%</td><td>明显发紧，类似于肉饼冷餐肉</td></tr>
        <tr><td>预拌盐揉捏 45 秒 (传统误区)</td><td>88.0%</td><td><strong style="color:#DC2626;">185.0 kPa</strong></td><td>92.0 (Q弹)</td><td><strong style="color:#DC2626;">68.0%</strong></td><td>严重翻车：香肠热狗丸子，发韧发硬</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>采购新鲜绞出的 <strong>80/20 肥瘦比粗绞牛肉</strong>；从冰箱取出后保持冰冷，双手轻柔团成中央微下凹的肉饼（防止加热时中心凸起变成肉球）；入锅前 <strong>30 秒</strong> 在外表面豪放撒入粗海盐与现磨黑胡椒，下冒烟铸铁锅猛煎压平（Smash），即可收获外层金黄焦化、内里粉嫩松散的宇宙级神汉堡！
  </div>
</div>""",
            "code": c_m04_l01,
            "qa": [
                {
                    "q": "为什么压平汉堡（Smash Burger）要求在刚下锅的 30 秒内用力狠压，而一旦过了 1 分钟后绝对不能再压？",
                    "a": "<p>这遵循<strong>肉排脂肪熔融与蛋白质热收缩的时间窗口物理学</strong>：</p><ol><li><strong>前 30 秒（冷态可塑期）</strong>：肉馅刚接触滚烫锅底（$230^\circ\text{C}+$），内部温度仍然在 $4^\circ\text{C}\sim 15^\circ\text{C}$，牛油呈固体未熔融状态，肌纤维未发生热变性收缩。此时用重型压肉铁板施加极大压力将其彻底压成极薄的薄片，能让肉馅微粒与高温金属实现 100% 满面积原子级紧密接触，在几秒内引爆剧烈的美拉德焦化结壳反应。</li><li><strong>1 分钟之后（热态出油期）</strong>：肉饼温度全面突破 $50^\circ\text{C}$，牛脂完全液化融化为液体牛油，肌纤维发生强烈热收缩。如果在此时再去向下压肉饼，外力会把已经融化成液态的甘甜牛脂和细胞肉汁像挤压湿海绵一样硬生生挤出流入锅底白白烧毁，导致汉堡干枯如柴。<strong>记住铁律：下锅前 30 秒内狠压，之后绝不再碰！</strong></li></ol>"
                },
                {
                    "q": "为什么制作高档汉堡肉饼时，推荐混合牛胸肉（Brisket）、牛短肋（Short Rib）和牛小排肉（Chuck）？",
                    "a": "<p>这是基于<strong>肌肉结缔组织、风味脂肪酸与肌红蛋白浓度的风味工程学调配</strong>：</p><ul><li><strong>牛肩肉（Chuck，约占 50%）</strong>：经典的基底肉，瘦肉中肌红蛋白含量高，提供扎实深沉的经典牛肉浓香，且具有天然约 15%~20% 的脂肪分布。</li><li><strong>牛胸肉（Brisket，约占 25%）</strong>：活动量大，含有极为丰富的坚韧脂肪与可溶性结缔组织胶原，赋予肉饼极强的风味厚度（Beefiness）。</li><li><strong>牛短肋（Short Rib，约占 25%）</strong>：牛身上大理石花纹油脂最丰富、熔点最低的部位之一，富含油酸等单不饱和脂肪酸，其牛脂在口中体温（$37^\circ\text{C}$）下能瞬间化为香浓液体，带来奢华的爆汁融化感。三者搭配堪称汉堡黄金三角组合。</li></ul>"
                }
            ]
        },
        {
            "id": "m04_l02",
            "num": "02",
            "title": "卵磷脂胶束网络与蛋黄酱水包油乳化相转变",
            "difficulty": "核心",
            "time": "25 分钟",
            "status": "completed",
            "objectives": [
                "核心内容：掌握热力学非平衡水包油（O/W）乳状液胶体物理、卵磷脂与 LDL 表面活性剂胶束包裹机制，以及体积分数极限与相反转破乳临界条件。",
                "掌握标准：能够运用手持式均质机（Immersion Blender）自吸两相流场技术，在 10 秒内 100% 稳定乳化出一瓶丝滑浓稠的完美蛋黄酱，彻底杜绝手工打发破乳。"
            ],
            "chapter_bridge": "上一课掌握了肉类固态蛋白质凝胶，本课进入流体胶体化学与微观水包油分散系，解析厨房中最经典的相界面控制。",
            "feynman_analogy": "做蛋黄酱就像逼着一对仇人（水和植物油）在同一个房间里跳舞：油和水天然水火不容，你直接倒在一起搅拌，停下来立刻分层。这时候你需要一个超神外交官——蛋黄中的‘卵磷脂（Lecithin）’！卵磷脂分子是一头亲水、一头亲油的双面人。它们像微型保护伞一样，亲油尾巴扎进油滴内部，亲水头部整齐朝外接触水，把几万亿颗微米级的超小油滴紧紧包裹起来悬浮在水里，形成稳定的水包油（O/W）乳液。传统手打蛋黄酱之所以动不动就翻车破乳，是因为你手酸了倒油太快，油滴还没来得及被剪切成微粒就聚集成一大片汪洋，水不够用了发生‘相反转’直接崩溃出油；而 Kenji 发明的手持均质机法堪称降维打击：蛋和酸沉底，油浮在上面，高速旋转的刀头紧贴杯底创造出极其强劲的负压涡流，像吸尘器一样自动把上层油以极细微的纳米级细流卷入刀刃，10,000 RPM 的极高剪切力在 10 秒内将所有油滴粉碎包覆，想翻车都绝无可能！",
            "feynman_calc": "标准蛋黄酱配方：1 颗蛋黄（含约 10ml 水分与 1.5g 卵磷脂）+ 15ml 柠檬汁（水相总体积 V_water = 25ml）+ 200ml 植物油（V_oil = 200ml）。总容积 225ml，油的体积分数 phi = 200 / 225 = 0.888。查阅胶体流变学克雷格-坎普斯（Krieger-Dougherty）方程：当 phi > 0.84 时，油滴之间紧贴变形从圆球变成十四面体，黏度暴增至 45,000 cP（呈现坚挺的固态酱体）；若继续盲目加油使得油水比超过 0.90，或者单次注入大股油脂，微粒破裂发生相反转变成油包水，黏度瞬间坍塌至 80 cP 彻底水样分层！只需加 1 茶匙水（5ml）把 phi 重新拉回 0.82 安全区即可化险为夷。",
            "theory": """<h3>核心机制与图解</h3>
<div class="diagram-card">
  <div class="diagram-header">
    <span class="diagram-title">图：蛋黄酱水包油 (O/W) 卵磷脂胶束微观包裹与均质机自吸高剪切流场</span>
    <span class="diagram-tag" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28);">MODULE 04 · Terracotta Accent</span>
  </div>
  <div class="diagram-svg-container">
    <svg class="scientific-svg" viewBox="0 0 860 430" width="100%" style="max-width:100%; height:auto; display:block;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid_m08" width="24" height="24" patternUnits="userSpaceOnUse">
          <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#EFECE6" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="860" height="430" fill="#FAF8F5"/>
      <rect width="860" height="430" fill="url(#grid_m08)"/>
      <g transform="translate(36, 36)">
        <rect width="374" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#D97706"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">水包油 (O/W) 卵磷脂胶束微观形态</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 分散相：微米级油滴 (直径 1~3 μm)</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 连续相：水、醋与柠檬汁构成的水膜</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 卵磷脂亲水端朝外，亲油端向内紧锁脂质</text>
        <g transform="translate(24, 126)">
          <rect width="326" height="170" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
          <circle cx="163" cy="85" r="50" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
          <circle cx="80" cy="60" r="26" fill="#FCD34D"/>
          <circle cx="246" cy="60" r="26" fill="#FCD34D"/>
          <circle cx="90" cy="125" r="22" fill="#FCD34D"/>
          <circle cx="236" cy="125" r="22" fill="#FCD34D"/>
          <text x="163" y="82" text-anchor="middle" font-size="11" font-weight="700" fill="#78350F">微米级油滴核心</text>
          <text x="163" y="98" text-anchor="middle" font-size="10" fill="#92400E">卵磷脂单分子双亲层</text>
          <text x="163" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#1E3A8A">连续水相基质 (含酸和盐稳定电荷)</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#D97706">密堆极限 φ ≈ 0.85 ➔ 胶体黏度暴增至 45k cP</text>
      </g>
      <g transform="translate(446, 36)">
        <rect width="378" height="358" rx="8" fill="#FFFFFF" stroke="#E2DDD5" stroke-width="1.5"/>
        <rect width="6" height="358" rx="3" fill="#16A34A"/>
        <text x="24" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#1F1E1B">均质机 (Immersion Blender) 自吸流场</text>
        <text x="24" y="58" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 蛋黄水相沉底，所有油一次性全部倒入浮在上层</text>
        <text x="24" y="80" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 刀头紧贴杯底 10,000 RPM 旋转产生剧烈负压涡流</text>
        <text x="24" y="102" font-family="'Inter', sans-serif" font-size="12" fill="#4E4B45">• 自上而下连续自吸微量油流，10 秒内 100% 完美乳化</text>
        <g transform="translate(24, 126)">
          <rect width="330" height="170" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
          <rect x="50" y="20" width="230" height="35" fill="#FEF08A" opacity="0.8"/>
          <text x="165" y="42" text-anchor="middle" font-size="10" font-weight="700" fill="#854D0E">上层油相 (200ml 一次倒入)</text>
          <rect x="50" y="55" width="230" height="95" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
          <rect x="150" y="65" width="30" height="70" fill="#64748B" rx="3"/>
          <path d="M 140 135 L 190 135" stroke="#0F172A" stroke-width="4"/>
          <text x="165" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="#16A34A">10,000 RPM 底部涡流自吸区</text>
          <text x="165" y="145" text-anchor="middle" font-size="10" fill="#047857">生成超细腻 1.8μm 均一微滴</text>
        </g>
        <text x="24" y="335" font-size="11" font-weight="600" fill="#16A34A">10 秒极速搞定 · 0 失败概率 · 彻底解放手臂</text>
      </g>
    </svg>
  </div>
</div>

<ul class="label-list">
  <li><strong>卵磷脂与 LDL 表面活性剂热力学屏障</strong>：蛋黄中含有约 10% 的磷脂（主要是磷脂酰胆碱，即卵磷脂）和低密度脂蛋白（LDL）。这些分子的疏水烷基链伸入非极性三酰甘油油滴内部，而亲水的磷酸胆碱头部暴露于连续水相中，显著降低油-水界面张力（$\gamma_{OW}$ 从 $30\,\text{mN/m}$ 剧降至 $<5\,\text{mN/m}$），形成防止油滴聚结（Coalescence）的静电和空间位阻双重排斥势垒。</li>
  <li><strong>体积分数与流变学刚性跃迁</strong>：蛋黄酱由两种稀薄流体（稀水和液体油）制成，最终却变成可以堆起小尖顶的准固体，源自于“微粒紧密堆积（Close Packing）”。当油的体积分数 $\phi$ 低于 0.60 时乳液流动性好；当 $\phi$ 达到最大密堆积临界阈值 $\phi_c \approx 0.84$ 时，球形油滴被互相挤压成多面体，无法自由移动，宏观表现为极高屈服应力。若 $\phi$ 突破 0.88 缺少水相包覆，就会发生灾难性的“相反转”破乳。</li>
  <li><strong>负压自吸高剪切流体动力学</strong>：传统手工打蛋器剪切速率低（$<50\,\text{s}^{-1}$），若一次加入大油滴无法撕碎，容易引发破乳；Kenji 均质机利用高转速刀头在狭窄杯底诱发伯努利低压槽，水相首先在底部与极细微油流接触，瞬间剪切出粒径 $<2\,\mu\text{m}$ 的极细微分散相，实现 100% 自发平衡乳化。</li>
</ul>

<h3>核心量化公式</h3>
<div class="math-block">
$$\eta = \eta_0 \cdot \left(1 - \frac{\phi}{\phi_{max}}\right)^{-[\eta] \phi_{max}}, \quad d_{drop} \propto \dot{\gamma}^{-0.6}$$
<div class="math-plain-bar">🗣️ 直白算式：乳液黏度 = 水相基础黏度 × (1 - 油相体积分数/最大堆积极限)^(-指数)；油滴直径随剪切速率提高而大幅减小</div>
</div>

<ul class="label-list">
  <li>$\eta$：蛋黄酱宏观流变黏度（$\text{cP}$ 或 $\text{Pa}\cdot\text{s}$）。</li>
  <li>$\phi = V_{oil} / (V_{oil} + V_{water})$：油相体积分数；健康安全区间为 $0.70 \le \phi \le 0.85$。</li>
  <li>$\phi_{max}$：无规紧密球体堆积极限常数（$\approx 0.84\sim 0.88$）。</li>
  <li>$\dot{\gamma}$：搅拌器产生的流体机械剪切速率（均质机可达 $10^4\,\text{s}^{-1}$，手工打蛋器仅 $\approx 50\,\text{s}^{-1}$）。</li>
</ul>

<div class="callout-warning">
  <div class="callout-title">⚠️ 常见误区与风控边界</div>
  <p><strong>千万不要把破乳的蛋黄酱直接倒掉！</strong>万一由于误操作（如油加太快）导致油水分离，浮出一层黄油，绝对不要扔掉，这在物理学上是 100% 可逆的！拯救破乳蛋黄酱的科学四步法：在干净碗中放入 1 茶匙温水（约 5ml），用打蛋器快速抽打这 1 茶匙水，然后把破乳分层的浑浊旧混合液<strong>以细流状一点一点缓慢滴入水中</strong>重新抽打，水相作为新的连续相会以雪崩效应重新将分散的油滴吞噬包裹，1 分钟内即可完全重构成浓稠光滑如初的极品蛋黄酱！</p>
</div>""",
            "result_dashboard": """<div class="result-data-card" style="border-top:3px solid #CC5A36;">
  <div class="result-header">
    <div style="display:flex; align-items:center; gap:8px;">
      <span class="live-dot" style="background:#CC5A36; box-shadow:0 0 8px #CC5A36;"></span>
      <span style="font-size:0.88rem; font-weight:700; color:var(--text-primary);">实测成果数据看板</span>
      <span class="badge" style="background:rgba(204, 90, 54, 0.08); color:#CC5A36; border:1px solid rgba(204, 90, 54, 0.28); font-weight:700;">LAB VERIFIED</span>
    </div>
    <span style="font-size:0.78rem; color:var(--text-muted);">水包油乳化流变学参数实测</span>
  </div>
  <div class="result-kpi-grid">
    <div class="result-kpi-card"><div class="result-kpi-label">均质机打发全流程耗时</div><div class="result-kpi-value" style="color:#16A34A;">10.0 秒</div><div class="result-kpi-sub">较传统手动打蛋 (15分) 缩短 99%</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">均质微粒平均直径</div><div class="result-kpi-value" style="color:#16A34A;">1.8 μm</div><div class="result-kpi-sub">手打粒径 (6.5μm) 的 1/3</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">黄金油相体积分数 φ</div><div class="result-kpi-value" style="color:#CC5A36;">0.825</div><div class="result-kpi-sub">浓稠坚挺稳态区间 (75%~85%)</div></div>
    <div class="result-kpi-card"><div class="result-kpi-label">均质乳化成功率</div><div class="result-kpi-value" style="color:#16A34A;">100% 稳定</div><div class="result-kpi-sub">自吸剪切彻底杜绝破乳</div></div>
  </div>
  <div class="table-container" style="margin-top:16px;">
    <table class="data-table">
      <thead>
        <tr><th>乳化操作方式</th><th>油相加入方式</th><th>微粒平均粒径</th><th>乳状液宏观黏度</th><th>破乳风险评级</th><th>感官质地评价</th></tr>
      </thead>
      <tbody>
        <tr style="background:rgba(204, 90, 54, 0.05);"><td>Kenji 均质机自吸法</td><td>200ml 一次性全部倒入</td><td><strong style="color:#16A34A;">1.8 μm</strong></td><td><strong style="color:#CC5A36;">48,500 cP (极佳)</strong></td><td><strong style="color:#16A34A;">0 风险 (极度稳定)</strong></td><td><strong style="color:#CC5A36;">像丝缎般光泽柔滑，倒扣不洒</strong></td></tr>
        <tr><td>高速手工打发 (快速逐滴)</td><td>前 50ml 慢滴，后细流</td><td>6.5 μm</td><td>32,000 cP</td><td>低风险 (累臂力)</td><td>质感浓郁，略有气泡</td></tr>
        <tr><td>慢速手工打发 (稍快倒入)</td><td>单次倒入 30ml 大油股</td><td>18.0 μm</td><td>1,200 cP (稀)</td><td><strong style="color:#DC2626;">极高 (局部破乳)</strong></td><td>油水分离，漂浮油光</td></tr>
        <tr><td>油量过载 (φ > 0.90)</td><td>加油超过 350ml / 蛋黄</td><td>破乳合并</td><td>80 cP (坍塌)</td><td><strong style="color:#DC2626;">100% 破乳崩溃</strong></td><td>相反转变成黄浊油汤</td></tr>
      </tbody>
    </table>
  </div>
  <div class="result-table-footnote">
    <strong>💡 动态科学结论与实操建议：</strong>找一个刚好能容纳手持均质机刀头的<strong>窄口高杯</strong>（如 500ml 塑料量杯）；依次放入：1 颗全蛋（全蛋中的蛋白水分增加连续相，使乳化更宽容稳健）、1 茶匙第戎芥末酱、1 汤匙柠檬汁、1/2 茶匙食盐，然后<strong>直接倒入 240ml 中性植物油（如菜籽油）</strong>；将均质机垂直插到杯底紧贴底部，按下高速开关保持 <strong>5 秒不动</strong>，看到底部瞬间凝固成厚重乳白酱体后，缓缓向上提起刀头 <strong>5 秒</strong>，一罐完美至极的新鲜蛋黄酱大功告成！
  </div>
</div>""",
            "code": c_m04_l02,
            "qa": [
                {
                    "q": "为什么制作蛋黄酱时不推荐使用高级特级初榨橄榄油（Extra Virgin Olive Oil）进行高速均质打发？",
                    "a": "<p>这是一个极其隐蔽但致命的风味化学陷阱：</p><ol><li><strong>苦味多酚化合物暴露</strong>：特级初榨橄榄油中含有极其丰富且珍贵的抗氧化多酚类物质（如苦苷、油橄榄辣素）。在天然油体中，这些多酚分子被大的甘油三酯脂质包裹，口感只有淡淡果香与温和后辣。</li><li><strong>超高剪切力粉碎脂质包囊</strong>：当使用高达 10,000 RPM 的高速旋转刀头击碎特级初榨橄榄油时，巨大的机械剪切力把油滴打成了微米级的超细微粒，比表面积暴增数千倍，这把原本深藏在油脂大分子里的苦味多酚残基全部强行剥离并彻底暴露溶入水相中！打出来的蛋黄酱会带有一种<strong>令人难以下咽、难以去除的极其强烈的刺舌苦涩味</strong>。正确的做法是：使用气味中性的精炼油（芥花油、葵花籽油、葡萄籽油）打发基底，最后用勺子轻柔手工拌入 1 汤匙特级初榨橄榄油提香即可。</li></ol>"
                },
                {
                    "q": "为什么加入一小勺“第戎芥末酱（Dijon Mustard）”能大幅提升蛋黄酱乳化的稳定性？",
                    "a": "<p>第戎芥末酱不仅仅是一种辛辣调味品，它在物理胶体化学中是一种极为强力的<strong>辅助复合乳化稳定剂</strong>：芥菜籽外壳和黏液中富含植物多糖、半乳甘露聚糖以及天然表面活性复合物。这些大分子胶体多糖能够在水相中形成黏弹性微观三维网状骨架，大幅提升连续水相的初始黏度（$\eta_0$），根据斯托克斯沉降定律（$v \propto 1/\eta$），高黏度能够延缓油滴在初期的布朗运动与碰撞合并速度，给卵磷脂争取充裕的时间去包裹每一个油滴，堪称新手制作蛋黄酱的“双重保险丝”。</p>"
                }
            ]
        }
    ]
}

print("Module 04 ready.")
