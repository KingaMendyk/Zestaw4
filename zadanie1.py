import math


# Zadanie1
def panel_calc(floor_length, floor_width, panel_length, panel_width, panel_amount):
    packages = 0
    floor_area = floor_length * floor_width
    floor_area = floor_area * 1.1
    panel_area = panel_length * panel_width
    packages = math.ceil((floor_area / panel_area) / panel_amount)
    return packages


print("Potrzeba : " + str(panel_calc(4, 4, 0.250, 1, 10)))
