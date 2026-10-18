"""
模块 01 · 第 02 课：炒蛋加盐时机与水合电荷屏蔽 (Scrambled Egg Salting & Moisture Retention)
根据《料理实验室》第一章科学实验：对比提前 15 分钟加盐 vs 出锅前撒盐 vs 不加盐
对卵清蛋白加热凝固时“脱水收缩 (Syneresis)”渗水率与质感嫩度的影响。
"""
from typing import Dict, Any

def calc_scrambled_egg_moisture(
    salt_percent: float,
    pre_salt_minutes: float,
    cooking_temp_c: float = 120.0
) -> Dict[str, Any]:
    """
    计算炒蛋保水性模型：
    最佳加盐比例：1.0% ~ 1.5% (相对蛋液质量)
    机理：提前 15 分钟加盐，Na+ 和 Cl- 离子进入卵清蛋白胶束，中和多肽链表面正负电荷，
    形成离子溶剂化层（Hydration Shell），阻碍高温下蛋白分子过度紧密交联，阻止将结合水挤出。
    若临下锅才撒盐或出锅前撒盐：离子未渗透水合，蛋白快速硬化网格挤压，渗水率激增 3~4 倍。
    """
    # 离子扩散与电荷屏蔽指数 (0.0 ~ 1.0)
    diffusion_factor = min(1.0, pre_salt_minutes / 15.0)
    
    # 盐浓度有效度 (1.0%~1.2% 为最佳平衡点)
    if salt_percent <= 0:
        charge_shielding = 0.0
    else:
        charge_shielding = min(1.0, salt_percent / 1.0) * diffusion_factor

    # 渗水率计算 (基准 12% 游离水分渗出)
    base_syneresis = 14.5  # %
    # 离子屏蔽有效降低脱水收缩
    actual_water_loss = max(1.8, base_syneresis * (1.0 - 0.78 * charge_shielding))

    # 质地软嫩度评分 (0 ~ 100)
    tenderness = 55.0 + charge_shielding * 40.0
    if salt_percent > 2.5:
        tenderness -= (salt_percent - 2.5) * 15.0  # 盐过多导致盐析硬化

    curd_texture = (
        "丝滑嫩水润 (Silky & Custardy)" if actual_water_loss < 4.0
        else "标准松软 (Standard Soft)" if actual_water_loss < 8.0
        else "干柴出汤 (Rubber & Watery)"
    )

    return {
        "salt_percent": salt_percent,
        "pre_salt_minutes": pre_salt_minutes,
        "charge_shielding_index": round(charge_shielding, 3),
        "water_loss_percent": round(actual_water_loss, 2),
        "tenderness_score": round(tenderness, 1),
        "texture_verdict": curd_texture
    }

if __name__ == "__main__":
    # 实验 A: 提前 15 分钟加 1.0% 盐 (完美科学炒蛋)
    res_kenji = calc_scrambled_egg_moisture(salt_percent=1.0, pre_salt_minutes=15.0)
    assert res_kenji["water_loss_percent"] < 4.5
    assert res_kenji["texture_verdict"] == "丝滑嫩水润 (Silky & Custardy)"

    # 实验 B: 临下锅撒盐 (0 分钟)
    res_instant = calc_scrambled_egg_moisture(salt_percent=1.0, pre_salt_minutes=0.0)
    assert res_instant["water_loss_percent"] > 12.0

    # 实验 C: 不加盐
    res_nosalt = calc_scrambled_egg_moisture(salt_percent=0.0, pre_salt_minutes=0.0)
    assert res_nosalt["water_loss_percent"] >= 14.0
    print("Lesson 02 Scrambled Egg Salting: All assertions passed!")
