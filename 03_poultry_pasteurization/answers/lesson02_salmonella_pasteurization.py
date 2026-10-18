"""
模块 03 · 第 02 课：沙门氏菌 D 值对数灭菌与等效巴氏消毒 (Salmonella D-Value Pasteurization)
根据《料理实验室》第六章科学实验：解构 USDA 规定的 74°C (165°F) 瞬间灭菌法规神话，
基于微生物细菌热死亡动力学对数衰减公式 log10(N0/Nt) = t / D(T)，计算在 60°C~74°C 下达成 7-log10 灭菌所需的法定保持时间。
"""
from typing import Dict, Any
import math

def calc_salmonella_pasteurization(
    core_temp_c: float,
    target_log_reduction: float = 7.0,
    poultry_fat_pct: float = 12.0
) -> Dict[str, Any]:
    """
    沙门氏菌 (Salmonella spp.) 热失活符合一级动力学衰减：
    D 值定义为使微生物群落减少 90% (1-log10) 所需的时间 (分钟)。
    根据 USDA FSIS 研究，鸡肉中沙门氏菌参数：
    基准温度 T_ref = 60.0°C 时，D_60 ≈ 4.0 分钟 (7-D 对应 27.5 分钟)；
    温度敏感系数 z 值 ≈ 5.5°C。
    D(T) = D_ref * 10^((T_ref - T) / z)
    达到 7-D 安全消毒标准总时间 t_safe = 7.0 * D(T)
    """
    if core_temp_c < 55.0:
        return {
            "core_temp_c": core_temp_c,
            "is_effective_pasteurization": False,
            "required_seconds": float("inf"),
            "required_time_display": "温度低于 55°C，无法灭菌 (处于危险增殖温区)",
            "juiciness_rating": "极生危险",
            "usda_compliant": False
        }

    # 计算该温度下的 D 值 (分钟，USDA FSIS 12% 脂肪标准 D_60 ≈ 4.0 min)
    d_value_min = 4.0 * math.pow(10.0, (60.0 - core_temp_c) / 5.5)
    
    # 7-log10 灭菌总时间
    required_minutes = target_log_reduction * d_value_min
    required_seconds = required_minutes * 60.0

    # 格式化时间输出
    if required_seconds <= 1.0:
        time_display = "瞬间灭菌 (< 1 秒)"
    elif required_seconds < 60.0:
        time_display = f"{round(required_seconds, 1)} 秒"
    else:
        time_display = f"{round(required_minutes, 1)} 分钟"

    # 多汁口感评定
    if core_temp_c >= 73.9:
        juiciness = "干柴粗糙 (Dry & Stringy) - 蛋白质过度脱水"
    elif core_temp_c >= 68.0:
        juiciness = "偏干紧实 (Firm)"
    elif core_temp_c >= 65.0:
        juiciness = "极致多汁且安全 (Peak Juiciness) - 推荐 65.5°C 保持 2.7 分钟"
    else:
        juiciness = "极其嫩滑 (Tender Custard) - 需精确控温"

    return {
        "core_temp_c": core_temp_c,
        "is_effective_pasteurization": True,
        "d_value_minutes": round(d_value_min, 3),
        "required_seconds": round(required_seconds, 1),
        "required_time_display": time_display,
        "juiciness_rating": juiciness,
        "usda_compliant": True
    }

if __name__ == "__main__":
    # 73.9°C (165°F): 瞬间灭菌
    res_165f = calc_salmonella_pasteurization(73.9)
    assert res_165f["required_seconds"] <= 2.0

    # 65.6°C (150°F): 保持 ~2.7 分钟 (160~180 秒) 即可达到 100% 相同杀菌效果
    res_150f = calc_salmonella_pasteurization(65.6)
    assert 120.0 < res_150f["required_seconds"] < 200.0
    assert "Peak Juiciness" in res_150f["juiciness_rating"]

    # 50°C 危险温区
    res_danger = calc_salmonella_pasteurization(50.0)
    assert res_danger["is_effective_pasteurization"] is False
    print("Lesson 02 Salmonella Pasteurization: All assertions passed!")
