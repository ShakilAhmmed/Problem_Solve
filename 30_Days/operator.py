meal_cost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip_calculation = (meal_cost) * (tipPercent/100)
tax_calculation = (meal_cost) * (taxPercent/100)
total_calculation = meal_cost + tip_calculation + tax_calculation
print(round(total_calculation))
