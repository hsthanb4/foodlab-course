#!/usr/bin/env python3
"""
The Food Lab (料理实验室) - 全量课程参考答案自动化回归测试套件
遍历 6 大模块、12 门核心课 answers/ 目录中的食品科学仿真模型，
执行 100% 单元测试与热力学断言校验。
"""
import os
import sys
import importlib.util
import time

MODULE_DIRS = [
    "01_breakfast_eggs",
    "02_meat_thermodynamics",
    "03_poultry_pasteurization",
    "04_ground_meat_emulsion",
    "05_starch_crisp_physics",
    "06_connective_tissue_stocks",
]

def run_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    passed = 0
    failed = 0
    total = 0
    results = []

    print("=" * 72)
    print(" THE FOOD LAB 料理实验室科学烹饪研习平台 - 自动化回归测试套件")
    print("=" * 72)
    start_time = time.time()

    for mod in MODULE_DIRS:
        ans_dir = os.path.join(base_dir, mod, "answers")
        if not os.path.exists(ans_dir):
            continue
        py_files = sorted([f for f in os.listdir(ans_dir) if f.startswith("lesson") and f.endswith(".py")])
        for py_file in py_files:
            total += 1
            file_path = os.path.join(ans_dir, py_file)
            test_name = f"{mod}/answers/{py_file}"
            try:
                spec = importlib.util.spec_from_file_location("test_module", file_path)
                module = importlib.util.module_from_spec(spec)
                # Redirect stdout during module execution if needed or run directly
                spec.loader.exec_module(module)
                passed += 1
                results.append((test_name, "PASS", None))
                print(f"  [ PASS ] {test_name}")
            except Exception as e:
                failed += 1
                results.append((test_name, "FAIL", str(e)))
                print(f"  [ FAIL ] {test_name}: {e}")

    elapsed = time.time() - start_time
    print("-" * 72)
    print(f"测试汇总: 总计 {total} 门核心课 | 通过 {passed} | 失败 {failed} | 耗时 {elapsed:.2f}s")
    print("=" * 72)

    if failed > 0:
        print("❌ 部分测试未通过，请检查上述错误日志！")
        sys.exit(1)
    else:
        print("✅ 100% 测试全部通过！所有食品科学物理/化学模型验证达标！")
        sys.exit(0)

if __name__ == "__main__":
    run_tests()
