"""
模块 02 · 第 02 课：肌肉蛋白热收缩与醒肉毛细张力再平衡 (Meat Resting Thermodynamics & Moisture Retention)
根据《料理实验室》第三章科学实验：模拟出锅牛排肌球蛋白与肌动蛋白热收缩产生的内部高压，
定量推演醒肉时间 (Resting Time) 对温度梯度均化、明胶黏度增加与切肉汁液流失率的抑制曲线。
"""
from typing import Dict, Any
import math

def calc_resting_juice_loss(
    resting_minutes: float,
    steak_thickness_cm: float = 3.5,
    pull_temp_c: float = 52.0
) -> Dict[str, Any]:
    """
    肉块刚出锅时：
    1. 外层肌肉因承受 200°C+ 炙烤，肌球蛋白 (50°C) 和肌动蛋白 (66°C) 强烈轴向收缩，像拧毛巾一样将游离水分挤向中心，
       使中心区域产生高静水压 (Hydrostatic Pressure)。
    2. 若此时立即切开，由于压力差驱动，中心游离水瞬间喷涌而出，案板上一滩血水，损失高达 10%~14% 汁液。
    3. 醒肉过程：余热使温度梯度拉平，中心与外围压力差 ΔP 按指数衰减 ΔP(t) = P0 * exp(-t / tau)；
       同时肉汁中溶解的明胶随着降温黏度提升 3~5 倍，毛细管阻力骤增，切开流失降至 <2%。
    """
    # 醒肉时间特征常数 tau (厚度越大需要越久)
    tau = max(3.0, steak_thickness_cm * 2.2)

    # 内部静水压力梯度衰减 (基准初始 100 kPa)
    pressure_gradient_kpa = 100.0 * math.exp(-resting_minutes / tau)

    # 切开汁液流失率 (%)
    # 立即切开 ~12.5%，充分醒肉 (8~10min) 降至 ~1.8%
    juice_loss_pct = 1.8 + 10.7 * math.exp(-resting_minutes / (tau * 0.9))

    # 中心温度余热回升峰值 (Carryover Cooking)
    carryover_rise = 3.8 * (1.0 - math.exp(-resting_minutes / 4.0))
    current_core_temp = pull_temp_c + carryover_rise

    # 醒肉状态结论
    if resting_minutes < 2.0:
        verdict = "严重不足：立即切开导致肉汁灾难性喷涌"
    elif resting_minutes < 6.0:
        verdict = "部分醒肉：仍有明显肉汁渗出"
    elif resting_minutes <= 12.0:
        verdict = "黄金醒肉：毛细管与明胶锁水最饱满状态"
    else:
        verdict = "过度冷却：表面温度偏凉需复热表面"

    return {
        "resting_minutes": resting_minutes,
        "pull_temp_c": pull_temp_c,
        "peak_core_temp_c": round(current_core_temp, 1),
        "pressure_gradient_kpa": round(pressure_gradient_kpa, 1),
        "juice_loss_pct": round(juice_loss_pct, 2),
        "moisture_retained_pct": round(100.0 - juice_loss_pct, 2),
        "verdict": verdict
    }

if __name__ == "__main__":
    # 立即切开 (0 分钟)
    res_0 = calc_resting_juice_loss(resting_minutes=0.0)
    assert res_0["juice_loss_pct"] > 11.5

    # 醒肉 8 分钟
    res_8 = calc_resting_juice_loss(resting_minutes=8.0)
    assert res_8["juice_loss_pct"] < 3.5
    assert "黄金醒肉" in res_8["verdict"]

    print("Lesson 02 Meat Resting Physics: All assertions passed!")
