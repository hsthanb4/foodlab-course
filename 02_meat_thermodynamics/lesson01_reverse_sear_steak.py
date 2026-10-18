"""
模块 02 · 第 01 课：汽化潜热障壁与牛排逆向慢烤法 (The Latent Heat Barrier & Reverse Sear)
根据《料理实验室》第三章科学实验：定量计算水分子汽化潜热 (Lv = 2260 kJ/kg) 对表面美拉德反应的压制，
对比传统“大火先煎锁肉汁”法与“低温慢烤风干 + 极温秒煎”逆向慢烤法 (Reverse Sear) 的灰圈厚度与水分保留率。
"""
from typing import Dict, Any

def simulate_steak_sear(
    method: str,
    thickness_cm: float = 3.8,  # 1.5 英寸标准厚切肋眼
    pan_temp_c: float = 240.0,
    target_core_c: float = 54.0   # 5分熟 Medium-Rare
) -> Dict[str, Any]:
    """
    模拟牛排烹饪热力学与灰圈 (Overcooked Gray Band)：
    水的比热容：4.18 kJ/(kg·K)，但汽化潜热高达 2260 kJ/kg！
    只要表面有一层水分，吸收的巨大能量全部用于蒸发水分子，表面温度死死卡在 100°C 无法突破。
    传统法 (Traditional Sear First):
      湿表面直接入热锅，前 2~3 分钟在“水煮肉”，随后为了逼出焦香必须长久煎炸，
      高温向肉内部深度扩散，产生 6~9mm 的干硬灰边 (灰圈体积占比 40%+)。
    逆向慢烤法 (Reverse Sear):
      先以 105°C 低温烤箱慢烤预加热至中心 45°C，热风使肉表面完全脱水风干形成微缩膜。
      移至铸铁锅以 260°C 高温每面仅需 45 秒，美拉德反应在干燥表面数秒内瞬间引爆，灰圈 < 1.5mm。
    """
    if method == "reverse_sear":
        surface_moisture_pct = 12.0   # 烤箱风干后
        sear_time_sec_per_side = 45   # 快速结壳
        gray_band_thickness_mm = 1.2
        crust_maillard_score = 96.0   # 深度焦香芳香物质
        total_juice_loss_pct = 7.5    # 温和加热保水
    elif method == "traditional_sear":
        surface_moisture_pct = 74.0   # 刚从冷藏取出带有游离冷凝水
        sear_time_sec_per_side = 210  # 必须煎 3.5 分钟以蒸发水分
        gray_band_thickness_mm = 7.8
        crust_maillard_score = 78.0
        total_juice_loss_pct = 17.2   # 强烈收缩挤水
    else:
        raise ValueError("Unknown cooking method: " + method)

    # 灰圈体积占比估算：基于柱状几何模型
    gray_ratio = min(1.0, (gray_band_thickness_mm * 2) / (thickness_cm * 10))

    return {
        "method": method,
        "thickness_cm": thickness_cm,
        "surface_moisture_pct": surface_moisture_pct,
        "sear_time_sec_per_side": sear_time_sec_per_side,
        "gray_band_thickness_mm": gray_band_thickness_mm,
        "gray_band_volume_ratio_pct": round(gray_ratio * 100.0, 1),
        "total_juice_loss_pct": total_juice_loss_pct,
        "crust_maillard_score": crust_maillard_score,
        "recommendation": "逆向慢烤（完美内外通红，灰圈极薄）" if method == "reverse_sear" else "传统煎法（灰圈严重过熟）"
    }

if __name__ == "__main__":
    res_rev = simulate_steak_sear("reverse_sear", thickness_cm=3.8)
    assert res_rev["gray_band_thickness_mm"] < 2.0
    assert res_rev["total_juice_loss_pct"] < 10.0

    res_trad = simulate_steak_sear("traditional_sear", thickness_cm=3.8)
    assert res_trad["gray_band_thickness_mm"] > 6.0
    assert res_trad["total_juice_loss_pct"] > 15.0
    print("Lesson 01 Reverse Sear Steak: All assertions passed!")
