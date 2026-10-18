"""
模块 06 · 第 02 课：蔬菜叶绿素脱镁褐变与果胶甲酯酶活 (Vegetable Blanching & Chlorophyll Preservation)
根据《料理实验室》第四章科学实验：定量解析绿色蔬菜在沸水焯水中的叶绿素 a/b 卟啉环镁离子脱落动力学，
揭秘大锅宽水稀释酸性挥发物、微量小苏打调节 pH 与冰水浴急速终止酶活保留翠绿爽脆的科学原理。
"""
from typing import Dict, Any

def calc_blanching_chlorophyll(
    blanch_seconds: int,
    water_temp_c: float = 100.0,
    ph_level: float = 7.0,
    use_ice_bath: bool = True
) -> Dict[str, Any]:
    """
    绿色蔬菜焯水科学：
    叶绿素分子结构核心为一个卟啉环螯合着一个二价镁离子 (Mg2+)。
    1. 褪色机制：在酸性环境 (低 pH) 或长时间受热下，两个氢离子 (H+) 强行置换出中心镁离子，
       转化为“脱镁叶绿素 (Pheophytin)”，颜色从亮翠绿突变为暗沉的橄榄灰绿 (Olive Drab)。
    2. 大锅宽水作用：植物细胞受热破裂释放有机酸，小锅水会使水质快速酸化；大锅沸水能大幅稀释酸性物质，保持近中性。
    3. 微碱性增益：若水中加入极微量食用小苏打 (微弱提升 pH 至 7.5~8.0)，能极大抑制脱镁置换反应，使绿色极其鲜亮耀眼；
       但切忌过量，否则会过度溶解半纤维素导致蔬菜烂糊。
    4. 冰水浴 (Shocking) 作用：捞出后植物内部余热仍会持续驱动脱镁反应并使果胶软化，冰水急冷可将酶活与热反应瞬间归零！
    """
    # 脱镁反应速率受酸度和时间主导
    # pH 7.0 为中性，pH < 6.0 呈酸性迅速变暗，pH 7.5~8.0 保护绿色
    if ph_level < 5.5:
        acid_acceleration = 3.5
    elif ph_level <= 7.0:
        acid_acceleration = 1.0
    else:  # 微碱性
        acid_acceleration = 0.35

    # 基础热降解
    thermal_deg = (blanch_seconds / 60.0) * (water_temp_c / 100.0) * 12.0 * acid_acceleration

    # 捞出后无冰水浴导致余热继续缓慢降解
    carryover_deg = 0.0 if use_ice_bath else 22.0

    chlorophyll_retention = max(10.0, min(99.0, 100.0 - (thermal_deg + carryover_deg)))

    # 爽脆度保留 (Pectin 结构完整性)
    if blanch_seconds <= 90:
        crispness_score = 92.0
    elif blanch_seconds <= 180:
        crispness_score = 75.0
    else:
        crispness_score = 40.0

    if ph_level > 8.5:
        crispness_score -= 30.0  # 碱过大果胶崩解

    # 颜色描述
    if chlorophyll_retention >= 85.0:
        color_verdict = "鲜亮翠绿生机盎然 (Vibrant Emerald Green)"
    elif chlorophyll_retention >= 65.0:
        color_verdict = "标准煮熟绿 (Standard Green)"
    else:
        color_verdict = "暗沉灰黄脱镁褐变 (Dull Olive-Drab Pheophytin)"

    return {
        "blanch_seconds": blanch_seconds,
        "ph_level": ph_level,
        "use_ice_bath": use_ice_bath,
        "chlorophyll_retention_pct": round(chlorophyll_retention, 1),
        "crispness_score": round(crispness_score, 1),
        "color_verdict": color_verdict,
        "scientific_advice": (
            "沸水快焯 60~90s + 冰水急冷可锁死 90%+ 叶绿素"
            if chlorophyll_retention >= 80.0
            else "酸性环境或余热未散导致镁离子脱失形成脱镁叶绿素"
        )
    }

if __name__ == "__main__":
    # 科学焯水：90秒 + 冰水浴 + 中性
    res_opt = calc_blanching_chlorophyll(blanch_seconds=90, use_ice_bath=True)
    assert res_opt["chlorophyll_retention_pct"] > 80.0
    assert "Vibrant Emerald Green" in res_opt["color_verdict"]

    # 传统错误：久煮 300 秒且不冰镇
    res_bad = calc_blanching_chlorophyll(blanch_seconds=300, use_ice_bath=False)
    assert res_bad["chlorophyll_retention_pct"] < 60.0
    assert "Dull Olive-Drab" in res_bad["color_verdict"]
    print("Lesson 02 Vegetable Chlorophyll: All assertions passed!")
