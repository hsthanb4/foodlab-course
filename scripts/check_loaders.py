#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_code(folder, filename):
    p = os.path.join(base_dir, folder, "answers", filename)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

# Load verified code from all 12 answers
c_m01_l01 = read_code("01_breakfast_eggs", "lesson01_boiled_egg_thermodynamics.py")
c_m01_l02 = read_code("01_breakfast_eggs", "lesson02_scrambled_egg_salting.py")
c_m02_l01 = read_code("02_meat_thermodynamics", "lesson01_reverse_sear_steak.py")
c_m02_l02 = read_code("02_meat_thermodynamics", "lesson02_meat_resting_physics.py")
c_m03_l01 = read_code("03_poultry_pasteurization", "lesson01_spatchcock_heat_flux.py")
c_m03_l02 = read_code("03_poultry_pasteurization", "lesson02_salmonella_pasteurization.py")
c_m04_l01 = read_code("04_ground_meat_emulsion", "lesson01_burger_salt_myosin.py")
c_m04_l02 = read_code("04_ground_meat_emulsion", "lesson02_mayo_emulsion_stability.py")
c_m05_l01 = read_code("05_starch_crisp_physics", "lesson01_triple_cooked_fries.py")
c_m05_l02 = read_code("05_starch_crisp_physics", "lesson02_pasta_starch_emulsion.py")
c_m06_l01 = read_code("06_connective_tissue_stocks", "lesson01_collagen_hydrolysis.py")
c_m06_l02 = read_code("06_connective_tissue_stocks", "lesson02_vegetable_chlorophyll.py")

print("All 12 code files loaded.")
