"""
模块 04 · 第 02 课：卵磷脂胶束网络与蛋黄酱水包油乳化相转变 (Mayo Emulsion & Lecithin Micelles)
根据《料理实验室》第十章科学实验：基于水包油 (O/W) 胶体化学与 Krieger-Dougherty 粘度方程，
模拟蛋黄低密度脂蛋白 (LDL) 与卵磷脂在不同油相体积分数 phi 下的乳化稳定性，并验证手持均质机 (Immersion Blender) 的两相流速剪切优势。
"""
from typing import Dict, Any

def calc_emulsion_stability(
    oil_ml: float,
    water_ml: float = 20.0,  # 约 1 个蛋黄 (含 10ml 水) + 10ml 柠檬汁/醋
    yolk_count: int = 1,
    shear_method: str = "immersion_blender"  # "whisk_slow", "whisk_fast", "immersion_blender"
) -> Dict[str, Any]:
    """
    蛋黄酱是一种热力学非平衡的水包油 (Oil-in-Water) 胶体分散系：
    分散相：植物油微滴 (直径 1~10 微米)
    连续相：水相 (蛋黄中的水分 + 醋/柠檬汁)
    乳化剂：蛋黄中的卵磷脂 (Lecithin) 和低密度脂蛋白 (LDL)
    单个蛋黄含有约 1.5g 卵磷脂，理论上可乳化多达 24 升油，但实际限制在于水相容积：
    油的体积分数 phi = V_oil / (V_oil + V_water)。
    当 phi 接近最大密堆积极限 phi_max ≈ 0.85 时，油滴互相紧贴挤压呈十四面体，粘度极大；
    若继续加油使得 phi > 0.88，或者单次注入大体积油缺少水相包裹，将发生“相反转 (Phase Inversion)”，破乳分层。
    Kenji 均质机法：将蛋、水、醋置于杯底，油浮于上部，均质机刀头紧贴底部高速旋转 (10,000 RPM)，
    高负压形成涡流将上层油以微米级细流自吸至底部剪切区，10 秒内 100% 完美乳化！
    """
    total_vol = oil_ml + water_ml
    phi = oil_ml / total_vol if total_vol > 0 else 0.0

    # 剪切微粒直径 (微米) 与剪切速率
    if shear_method == "immersion_blender":
        droplet_size_um = 1.8
        shear_power = 98.0
    elif shear_method == "whisk_fast":
        droplet_size_um = 6.5
        shear_power = 65.0
    else:  # whisk_slow
        droplet_size_um = 18.0
        shear_power = 30.0

    # 稳定性与破乳风险计算
    if phi < 0.50:
        state = "乳液偏稀 (Thin Emulsion)"
        break_risk = "极低 (稳态)"
        is_broken = False
        viscosity_cp = 1200.0
    elif phi <= 0.84:
        state = "稠厚丝滑标准蛋黄酱 (Rich Stable Mayo)"
        break_risk = "健康安全区"
        is_broken = False
        viscosity_cp = 45000.0 * (1.0 + (phi - 0.5) * 4.0)
    elif phi <= 0.88:
        state = "超浓稠高危区 (Critical Packing)"
        break_risk = "高度预警：需立即补加 1 茶匙水"
        is_broken = False
        viscosity_cp = 95000.0
    else:
        state = "破乳出油 (Phase Inversion / Broken)"
        break_risk = "已破乳：油相连续分层"
        is_broken = True
        viscosity_cp = 80.0

    # 缓慢手打若单次加油过快也会由于剪切不足破乳
    if shear_method == "whisk_slow" and oil_ml > 180.0:
        is_broken = True
        state = "手动剪切不足破乳 (Insufficient Shear)"

    return {
        "oil_ml": oil_ml,
        "water_ml": water_ml,
        "oil_fraction_phi": round(phi, 3),
        "droplet_size_um": droplet_size_um,
        "viscosity_cp": round(viscosity_cp, 1),
        "state": state,
        "break_risk": break_risk,
        "is_broken": is_broken,
        "rescue_instruction": "取 1 茶匙水入干净碗中，逐滴抽打搅拌旧破乳液即可复苏" if is_broken else "状态完美，无需干预"
    }

if __name__ == "__main__":
    # 经典配比：200ml 油 + 20ml 水相 (phi ≈ 0.90 临界，但在 200ml 油 + 30ml 水相下 phi = 0.87)
    res_blender = calc_emulsion_stability(oil_ml=180.0, water_ml=30.0, shear_method="immersion_blender")
    assert res_blender["is_broken"] is False
    assert res_blender["droplet_size_um"] < 3.0

    # 超出极限：350ml 油 + 20ml 水相 (phi > 0.94) 必破乳
    res_overflow = calc_emulsion_stability(oil_ml=350.0, water_ml=20.0, shear_method="immersion_blender")
    assert res_overflow["is_broken"] is True
    print("Lesson 02 Mayo Emulsion Stability: All assertions passed!")
