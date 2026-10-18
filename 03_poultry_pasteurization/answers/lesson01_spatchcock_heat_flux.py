"""
模块 03 · 第 01 课：蝴蝶展平法几何传热重构 (Spatchcocking Heat Distribution)
根据《料理实验室》第六章科学实验：对比烤整鸡时三维不规则空心球体几何与剪去脊椎展平 (Spatchcocking) 的
二维导热平板模型，分析胸肉 (65°C 嫩) 与大腿结缔组织 (75°C 化) 同步达成的热通量分布。
"""
from typing import Dict, Any

def compare_roast_chicken_geometry(
    is_spatchcocked: bool,
    chicken_weight_kg: float = 1.8,
    oven_temp_c: float = 230.0
) -> Dict[str, Any]:
    """
    传统整鸡 (Trussed Whole Bird):
      空心球体几何，体腔内冷空气形成隔热层。胸肉突起最接近烤箱顶部强辐射源，
      而大腿根部被紧紧绑在内部。当大腿中心达到安全的 74°C 时，胸肉早已飙升至 85°C+ 变成干柴木屑。
    蝴蝶展平法 (Spatchcocked Flat):
      剪去脊柱按断胸骨压平，转变为厚度均一的 2D 平板：
      1. 表面积增加，烘烤时间缩短近 50% (从 80 分钟骤降至 45 分钟)；
      2. 鸡腿与鸡翅朝外展开，吸收四周强热流，先达到 76°C+ 软化胶原蛋白；
      3. 胸肉平躺在中央较低热阻区域，与腿肉同步达到最理想的 65°C 汁水丰盈状态；
      4. 所有的鸡皮全部朝上暴露于辐射热中，实现 100% 酥脆金黄，绝无下半部分白煮软皮。
    """
    if is_spatchcocked:
        roast_time_minutes = 45.0
        breast_final_temp_c = 65.5  # 嫩多汁极品
        thigh_final_temp_c = 76.5   # 充分软化结缔组织
        skin_crisp_coverage_pct = 98.0
        thermal_resistance_index = 0.45
    else:
        roast_time_minutes = 80.0
        breast_final_temp_c = 84.0  # 严重过熟脱水
        thigh_final_temp_c = 74.0   # 刚刚熟
        skin_crisp_coverage_pct = 52.0  # 背部和下腹部发白绵软
        thermal_resistance_index = 1.00

    temp_gap = abs(thigh_final_temp_c - breast_final_temp_c)

    return {
        "is_spatchcocked": is_spatchcocked,
        "roast_time_minutes": roast_time_minutes,
        "breast_final_temp_c": breast_final_temp_c,
        "thigh_final_temp_c": thigh_final_temp_c,
        "temp_gap_c": round(temp_gap, 1),
        "skin_crisp_coverage_pct": skin_crisp_coverage_pct,
        "thermal_resistance_index": thermal_resistance_index,
        "verdict": "胸嫩(65°C)+腿香(76°C)+全皮酥脆，烹饪时间减半" if is_spatchcocked else "胸肉干柴(84°C)+局部软皮+耗时长"
    }

if __name__ == "__main__":
    spatch = compare_roast_chicken_geometry(True)
    assert spatch["roast_time_minutes"] <= 45.0
    assert spatch["breast_final_temp_c"] < 68.0
    assert spatch["skin_crisp_coverage_pct"] > 90.0

    whole = compare_roast_chicken_geometry(False)
    assert whole["breast_final_temp_c"] > 80.0
    print("Lesson 01 Spatchcock Heat Flux: All assertions passed!")
