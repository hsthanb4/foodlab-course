"""
模块 05 · 第 01 课：三段热解法与直链淀粉结晶硬化 (Triple-Cooked Ultra-Crisp Fries & Retrogradation)
根据《料理实验室》第九章科学实验：解构 Heston Blumenthal 与 Kenji 的“三段烹饪极致酥脆薯条”：
1. 微酸沸水预煮 (加醋 pH 4.0 保护果胶) 糊化表面淀粉；
2. 彻底风干冷冻促发淀粉老化回生 (Retrogradation) 析出直链淀粉微晶；
3. 低温初炸 (170°C) 排油定型 + 极温复炸 (205°C) 蒸汽发泡产生万千蜂窝微脆泡。
"""
from typing import Dict, Any

def simulate_french_fry_process(
    vinegar_added: bool,
    parboil_minutes: int,
    freeze_step: bool,
    double_fry: bool
) -> Dict[str, Any]:
    """
    薯条酥脆物理学：
    普通做法痛点：直接油炸会导致外部迅速烧焦但内部未熟；或者刚炸出脆 2 分钟，内部水分快速向外迁移使表皮软塌成烂泥。
    科学三段法：
    第一阶段微酸预煮 (加醋醋酸维持 pH ≈ 4.0)：
      原果胶 (Protopectin) 在碱性或中性下迅速水解成易碎水溶性果胶；而在 pH 4.0 微酸环境下果胶耐热性大幅增强！
      使土豆条猛煮 10 分钟仍能保持完整不碎裂，表面充分糊化形成一层富含直链淀粉 (Amylose) 的厚凝胶层。
    第二阶段冷冻回生 (Retrogradation)：
      糊化的直链淀粉在冷冻降温下分子链紧密平行排列形成高度规整的微晶束结构，极大增强脆壳刚性。
    第三阶段双温油炸：
      170°C 初炸：温和排出游离水，建立坚固外壳架构；
      205°C 复炸：剧烈汽化微量水分形成微孔气泡，赋予薯条超长 30 分钟不塌软的持久玻璃脆感！
    """
    # 完整性得分 (0 ~ 100)
    if not vinegar_added and parboil_minutes > 7:
        structural_integrity = 35.0  # 果胶崩解碎裂
    else:
        structural_integrity = 98.0

    # 淀粉微晶回生指数 (0.0 ~ 1.0)
    retrogradation_index = 0.95 if freeze_step else 0.20

    # 脆度保留半衰期 (分钟)
    if not double_fry:
        crisp_half_life_min = 3.5
        crisp_sound_score = 40.0
    elif double_fry and freeze_step and vinegar_added:
        crisp_half_life_min = 28.0   # 坚挺半小时！
        crisp_sound_score = 99.0
    else:
        crisp_half_life_min = 10.0
        crisp_sound_score = 75.0

    return {
        "vinegar_added": vinegar_added,
        "parboil_minutes": parboil_minutes,
        "freeze_step": freeze_step,
        "double_fry": double_fry,
        "structural_integrity_pct": structural_integrity,
        "retrogradation_index": retrogradation_index,
        "crisp_half_life_minutes": crisp_half_life_min,
        "crisp_score": crisp_sound_score,
        "verdict": (
            "极致玻璃脆皮薯条：长效坚挺 25min+ 不塌软"
            if crisp_sound_score > 90
            else "普通薯条：出锅数分钟内吸潮软塌"
        )
    }

if __name__ == "__main__":
    kenji_style = simulate_french_fry_process(
        vinegar_added=True, parboil_minutes=10, freeze_step=True, double_fry=True
    )
    assert kenji_style["crisp_score"] > 95.0
    assert kenji_style["crisp_half_life_minutes"] > 20.0
    assert kenji_style["structural_integrity_pct"] > 90.0

    bad_style = simulate_french_fry_process(
        vinegar_added=False, parboil_minutes=12, freeze_step=False, double_fry=False
    )
    assert bad_style["crisp_score"] < 50.0
    print("Lesson 01 Triple Cooked Fries: All assertions passed!")
