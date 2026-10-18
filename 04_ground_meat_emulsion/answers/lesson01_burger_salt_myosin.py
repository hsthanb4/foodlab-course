"""
模块 04 · 第 01 课：肌球蛋白盐溶抽提与汉堡质感解耦 (Myosin Extraction & Burger Salt Timing)
根据《料理实验室》第五章科学实验：深入肌球蛋白 (Myosin) 在食盐 (NaCl) 与机械搅拌下的交联机制，
量化对比“肉馅预混盐”与“成型后单面现撒盐”对汉堡肉饼弹性、硬度与汁水饱满度的本质区别。
"""
from typing import Dict, Any

def simulate_burger_patty_texture(
    salt_timing: str,
    mix_time_seconds: int = 30,
    fat_ratio_pct: float = 20.0  # 80/20 经典肥瘦比
) -> Dict[str, Any]:
    """
    肌球蛋白 (Myosin) 具有盐溶性特性：
    当在绞肉馅中直接加入食盐并揉捏搅拌时：
    1. 盐离子溶解肌原纤维表面的肌球蛋白；
    2. 机械剪切使得游离肌球蛋白分子末端互相交织缠绕，形成连续密集的交联蛋白质凝胶网络；
    3. 煎熟后形成类似热狗、香肠、贡丸的“弹性橡胶”口感 (Elastic Sausage Texture)；
    4. 紧密的蛋白质网络受热强烈收缩，将包覆的牛油挤出流失，肉饼干瘪发韧。
    正确汉堡法则 (Kenji's Law of Burgers):
    绞肉完全不加盐轻轻捏合成形，仅在入锅煎制前 30 秒于肉饼外表面撒粗盐与黑胡椒。
    内部肌原纤维保持离散独立微孔结构，咬下去松散多汁，牛油在微孔隙中融化爆发。
    """
    if salt_timing == "pre_mixed":
        # 预先混入肉馅搅拌
        myosin_crosslink_pct = min(95.0, 35.0 + mix_time_seconds * 1.5)
        patty_hardness_kpa = 185.0
        patty_springiness_score = 92.0  # 像热狗丸子一样 Q 弹
        chew_texture = "紧韧弹牙如香肠热狗 (Rubbery & Springy)"
        juice_retention_pct = 68.0
    elif salt_timing == "surface_only":
        # 成型后仅表面现撒盐
        myosin_crosslink_pct = 8.0
        patty_hardness_kpa = 42.0
        patty_springiness_score = 15.0
        chew_texture = "松散酥嫩一咬爆汁 (Tender & Crumbly Melt-in-Mouth)"
        juice_retention_pct = 88.0
    else:
        raise ValueError("Unknown salt timing: " + salt_timing)

    return {
        "salt_timing": salt_timing,
        "fat_ratio_pct": fat_ratio_pct,
        "myosin_crosslink_pct": round(myosin_crosslink_pct, 1),
        "patty_hardness_kpa": round(patty_hardness_kpa, 1),
        "patty_springiness_score": round(patty_springiness_score, 1),
        "juice_retention_pct": round(juice_retention_pct, 1),
        "chew_texture": chew_texture,
        "scientific_verdict": (
            "表面撒盐保留肌纤维离散微孔，锁住牛油融滴"
            if salt_timing == "surface_only"
            else "预拌盐抽提肌球蛋白交联，形成致密香肠凝胶"
        )
    }

if __name__ == "__main__":
    surf = simulate_burger_patty_texture("surface_only")
    assert surf["patty_hardness_kpa"] < 50.0
    assert surf["juice_retention_pct"] > 85.0
    assert "松散酥嫩" in surf["chew_texture"]

    prem = simulate_burger_patty_texture("pre_mixed", mix_time_seconds=30)
    assert prem["patty_hardness_kpa"] > 150.0
    assert prem["myosin_crosslink_pct"] > 70.0
    print("Lesson 01 Burger Salt Myosin: All assertions passed!")
