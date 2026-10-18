"""
模块 06 · 第 01 课：胶原蛋白三螺旋展开与明胶黏度热解 (Collagen-to-Gelatin Hydrolysis Kinetics)
根据《料理实验室》第二章科学实验：深入哺乳动物骨骼与结缔组织 I 型胶原蛋白 (Collagen) 刚性三螺旋分子结构，
基于阿伦尼乌斯 (Arrhenius) 反应速率方程对比传统慢炖与现代高压锅 (121°C, 15 psi) 的明胶转化效率与高汤醇厚度。
"""
from typing import Dict, Any
import math

def calc_collagen_conversion(
    temp_c: float,
    cooking_hours: float,
    initial_collagen_grams: float = 120.0
) -> Dict[str, Any]:
    """
    胶原蛋白水解动力学：
    胶原蛋白是由甘氨酸-脯氨酸-羟脯氨酸重复序列构成的致密刚性三螺旋结构超分子绳索，不溶于常温水。
    在湿热环境下，分子间共价交联与氢键逐渐断裂，展开为单个多肽链——可溶性明胶 (Gelatin)。
    水解速率常数遵循 Arrhenius 方程：
    k(T) = A * exp(-E_a / (R * T))
    在 60°C 时水解几乎停滞；
    在 85°C (慢炖微沸)：k 显著提高，但需炖煮 6~8 小时才能达成 85% 转化率；
    在高压锅 (121°C / 250°F，15 psi)：反应速率常数 k 激增 12 倍以上！仅需 45~60 分钟即可完成 95%+ 彻底水解。
    明胶赋予汤汁独特的黏唇触感与凝胶能力（冷藏成肉冻），并能在口中体温下融化释放鲜味。
    """
    temp_k = temp_c + 273.15
    R = 8.314  # J/(mol·K)
    E_a = 92000.0  # 活化能 J/mol
    A = 1.8e10     # 指前因子 (1/hour)

    if temp_c < 55.0:
        k = 0.0
    else:
        k = A * math.exp(-E_a / (R * temp_k))

    # 一级反应转化率 X = 1 - exp(-k * t)
    conversion_pct = (1.0 - math.exp(-k * cooking_hours)) * 100.0
    conversion_pct = min(99.0, max(0.0, conversion_pct))

    gelatin_yield_grams = initial_collagen_grams * (conversion_pct / 100.0)

    # 汤体丰厚度评分
    if conversion_pct >= 90.0:
        body_texture = "极度醇厚黏唇 (Rich Lip-Smacking Gelatinous Stock)"
        gel_in_fridge = "冷藏后凝固为坚挺肉冻 (Solid Jelly)"
    elif conversion_pct >= 60.0:
        body_texture = "标准柔滑高汤 (Medium Body)"
        gel_in_fridge = "冷藏后半凝固软冻"
    else:
        body_texture = "清淡水感缺乏厚度 (Thin & Watery)"
        gel_in_fridge = "冷藏后依然呈液态水状"

    return {
        "temp_c": temp_c,
        "cooking_hours": cooking_hours,
        "rate_constant_k": round(k, 4),
        "conversion_pct": round(conversion_pct, 1),
        "gelatin_yield_grams": round(gelatin_yield_grams, 1),
        "body_texture": body_texture,
        "gel_in_fridge": gel_in_fridge,
        "recommendation": (
            "高压锅 121°C 耗时仅 1 小时即可媲美传统 8 小时慢炖"
            if temp_c >= 115.0
            else "传统微沸需保持 6 小时以上以彻底水解骨胶原"
        )
    }

if __name__ == "__main__":
    # 高压锅 121°C 煮 1 小时
    res_pc = calc_collagen_conversion(temp_c=121.0, cooking_hours=1.0)
    assert res_pc["conversion_pct"] > 90.0
    assert "Rich Lip-Smacking" in res_pc["body_texture"]

    # 传统微沸 85°C 煮 1 小时 (转化严重不足)
    res_slow_short = calc_collagen_conversion(temp_c=85.0, cooking_hours=1.0)
    assert res_slow_short["conversion_pct"] < 35.0

    # 传统微沸 85°C 煮 8 小时 (充分转化)
    res_slow_long = calc_collagen_conversion(temp_c=85.0, cooking_hours=8.0)
    assert res_slow_long["conversion_pct"] > 85.0
    print("Lesson 01 Collagen Hydrolysis: All assertions passed!")
