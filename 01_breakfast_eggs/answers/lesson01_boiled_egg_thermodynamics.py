"""
模块 01 · 第 01 课：水煮蛋热力学与剥壳机制 (Boiled Egg Thermodynamics & Shell Peeling)
根据《料理实验室》第一章科学实验：模拟 1D 径向热传导方程、蛋清与蛋黄变性温区，
以及 100°C 沸水入锅热休克与冷水下锅剥壳难易度及硫化铁 (FeS) 变绿反应动力学。
"""
from typing import Dict, Any
import math

def simulate_boiled_egg(
    water_temp_c: float,
    cooking_minutes: float,
    egg_initial_temp_c: float = 4.0,
    egg_mass_grams: float = 57.0
) -> Dict[str, Any]:
    """
    模拟鸡蛋在恒温水浴中的热传导：
    r_egg ≈ 2.2 cm, alpha ≈ 1.4e-7 m^2/s (热扩散系数)
    球对称非稳态热传导一阶特征本征值：
    蛋清外层衰减速率指数 ≈ -18.0 * Fo
    蛋黄核心衰减速率指数 ≈ -9.5 * Fo
    蛋清变性温区：60°C~65°C 凝固
    蛋黄变性温区：65°C 增稠，70°C 完全凝固，>77°C 且持续 11min+ 促发 FeS 变绿环
    沸水下锅热休克使壳下膜角蛋白瞬间破裂与壳分离，剥壳成功率 >95%；冷水下锅因温和加热使白蛋白与内膜紧密粘接，剥壳成功率 <35%。
    """
    time_seconds = cooking_minutes * 60.0
    r_outer = 0.022  # 2.2 cm
    alpha = 1.4e-7   # m^2/s

    # 一维球对称热扩散傅里叶数 (Fourier Number Fo = alpha * t / r^2)
    fo = (alpha * time_seconds) / (r_outer ** 2)

    # 蛋白外层与蛋黄中心基于本征值展开的温度解析解
    temp_white = water_temp_c - (water_temp_c - egg_initial_temp_c) * math.exp(-18.0 * fo)
    temp_yolk_core = water_temp_c - (water_temp_c - egg_initial_temp_c) * math.exp(-9.5 * fo)

    # 蛋黄表面温度
    temp_yolk_surface = (temp_white + temp_yolk_core) / 2.0

    # 硫化铁变绿判定：蛋黄表面 >= 77°C 且加热时长 >= 11 分钟
    green_ring = bool(temp_yolk_surface >= 77.0 and cooking_minutes >= 11.0)

    # 蛋黄状态分类
    if temp_yolk_core < 62.0:
        yolk_texture = "流心 (Runny)"
    elif temp_yolk_core < 71.0:
        yolk_texture = "溏心/果酱状 (Jammy)"
    elif temp_yolk_core < 82.0:
        yolk_texture = "全熟粉嫩 (Tender Hard)"
    else:
        yolk_texture = "过熟干噎 (Overcooked)"

    # 剥壳成功率：沸水 (>=98°C) 入锅产生膜层热休克，脱壳率高；冷水入锅 (<80°C 开始升温) 白蛋白附着
    if water_temp_c >= 98.0:
        peel_score = 96.0  # 96% 极易剥壳
        shock_effect = "热休克膜层分离 (Thermal Shock Detachment)"
    else:
        peel_score = 32.0  # 白蛋白渗透粘合
        shock_effect = "白蛋白与内膜变性粘连 (Membrane Adhesion)"

    return {
        "white_temp_c": round(temp_white, 1),
        "yolk_core_temp_c": round(temp_yolk_core, 1),
        "yolk_surface_temp_c": round(temp_yolk_surface, 1),
        "yolk_texture": yolk_texture,
        "green_ring_detected": green_ring,
        "peel_success_rate": peel_score,
        "shock_mechanism": shock_effect
    }

if __name__ == "__main__":
    # 实验 1: 100°C 沸水煮 6.5 分钟 (完美果酱溏心蛋)
    res_6min = simulate_boiled_egg(water_temp_c=100.0, cooking_minutes=6.5)
    assert res_6min["yolk_texture"] == "溏心/果酱状 (Jammy)"
    assert res_6min["green_ring_detected"] is False
    assert res_6min["peel_success_rate"] > 90.0

    # 实验 2: 100°C 沸水煮 15 分钟 (过熟发绿)
    res_15min = simulate_boiled_egg(water_temp_c=100.0, cooking_minutes=15.0)
    assert res_15min["green_ring_detected"] is True
    assert res_15min["yolk_texture"] == "过熟干噎 (Overcooked)"

    # 实验 3: 75°C 低温入锅 (难剥壳)
    res_cold = simulate_boiled_egg(water_temp_c=75.0, cooking_minutes=10.0)
    assert res_cold["peel_success_rate"] < 40.0
    print("Lesson 01 Boiled Egg Thermodynamics: All assertions passed!")
