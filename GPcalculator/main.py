from unilorin_gp_calculator import *

total = calculator(table)
total_unit = unit_cal(table)
gp = total / total_unit
print(f"Your final GP is: {gp:3}")