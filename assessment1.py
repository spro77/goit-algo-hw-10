import pulp

# Create the LP problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Variables: x = lemonade, y = fruit juice
x = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Objective: maximize total products
prob += x + y, "Total_Products"

# Constraints
prob += 2 * x + 1 * y <= 100, "Water"
prob += 1 * x <= 50, "Sugar"
prob += 1 * x <= 30, "Lemon_Juice"
prob += 2 * y <= 40, "Fruit_Puree"

# Solve the problem
prob.solve()

# Output results
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Lemonade: {int(x.value())}")
print(f"Fruit Juice: {int(y.value())}")
print(f"Total Products: {int(x.value() + y.value())}")