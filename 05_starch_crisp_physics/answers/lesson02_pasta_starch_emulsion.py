"""
模块 05 · 第 02 课：淀粉颗粒破裂与卡乔佩佩浓缩乳化浆 (Pasta Water Emulsion & Cacio e Pepe)
根据《料理实验室》第九章科学实验：粉碎“意面必须用大量滚水煮”的传统迷思，
定量计算少水煮面法溶出淀粉浓度，并验证富直链淀粉面汤与佩科里诺奶酪油脂发生稳定乳化的相界面动力学。
"""
from typing import Dict, Any

def calc_pasta_water_starch(
    pasta_grams: float = 450.0,   # 1 磅标准意面
    water_liters: float = 1.5,    # 少水法 1.5L vs 传统法 5.0L
    cooking_minutes: int = 10
) -> Dict[str, Any]:
    """
    传统大锅水神话破灭：
    传统厨艺教条声称必须用 5~6 升大锅滚水煮 1 磅意面，否则会粘连。
    Kenji 严格对照实验证明：
    1. 意面在任何 >82°C 的水中吸水速率完全相同；冷水下锅只要在开始加温阶段轻微搅拌几下，绝不会粘连；
    2. 传统 5.0 升大锅水，溶出的淀粉被极度稀释，淀粉浓度仅有 0.3%~0.5%，倒掉浪费大量热能；
    3. 少水法 (1.5 升水)：水面刚好没过意面，煮出的面汤浓稠发白，淀粉浓度高达 2.8%~3.6%！
    意面酱汁乳化圣杯 (Cacio e Pepe & Carbonara):
    佩科里诺 (Pecorino Romano) 奶酪是由脂肪与酪蛋白组成的固体胶体。
    直接加水加热会使酪蛋白团聚收缩成橡胶口香糖状硬块并析出黄油 (Broken Clumpy Mess)。
    当加入高浓度 (>=2.5%) 淀粉面汤时，溶出的直链淀粉分子网格作为高分子空间位阻剂，
    将熔融油脂微滴与游离水牢牢锚定，形成如天鹅绒般顺滑光亮、永不凝结成块的极品乳化奶酪酱！
    """
    # 意面烹饪过程中约释放自身质量 7%~9% 的直链/支链淀粉
    starch_released_grams = pasta_grams * 0.082

    # 水分蒸发量约 0.25 升
    remaining_water_liters = max(0.5, water_liters - 0.25)
    starch_concentration_pct = (starch_released_grams / (remaining_water_liters * 1000.0)) * 100.0

    # 奶酪酱乳化成功度评分 (0 ~ 100)
    if starch_concentration_pct >= 2.5:
        emulsion_quality = "天鹅绒般丝滑稳定 (Velvety Glossy Emulsion)"
        clumping_risk = "零结块风险 (Zero Clumping)"
        emulsion_score = 98.0
    elif starch_concentration_pct >= 1.2:
        emulsion_quality = "良好可用 (Acceptable)"
        clumping_risk = "低风险"
        emulsion_score = 75.0
    else:
        emulsion_quality = "稀薄分离，油脂浮面 (Broken & Greasy)"
        clumping_risk = "极高风险：奶酪凝集成橡皮筋团"
        emulsion_score = 30.0

    # 能耗节约：将 5L 水烧开需 1.8 MJ，1.5L 水仅需 0.54 MJ
    energy_saved_pct = round(((5.0 - water_liters) / 5.0) * 100.0, 1)

    return {
        "pasta_grams": pasta_grams,
        "water_liters": water_liters,
        "starch_concentration_pct": round(starch_concentration_pct, 2),
        "emulsion_quality": emulsion_quality,
        "clumping_risk": clumping_risk,
        "emulsion_score": emulsion_score,
        "energy_saved_pct": energy_saved_pct,
        "scientific_conclusion": (
            "浓缩面汤淀粉胶体充当空间位阻乳化剂，锁住奶酪油脂"
            if emulsion_score > 90
            else "面汤过于稀薄，无法阻止酪蛋白硬化成团"
        )
    }

if __name__ == "__main__":
    low_water = calc_pasta_water_starch(water_liters=1.5)
    assert low_water["starch_concentration_pct"] > 2.5
    assert low_water["emulsion_score"] > 90.0
    assert low_water["energy_saved_pct"] >= 70.0

    trad_water = calc_pasta_water_starch(water_liters=5.0)
    assert trad_water["starch_concentration_pct"] < 0.9
    assert trad_water["emulsion_score"] < 40.0
    print("Lesson 02 Pasta Starch Emulsion: All assertions passed!")
