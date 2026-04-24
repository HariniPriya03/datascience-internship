from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

# Define the LP problem
model = LpProblem("Candle_Profit_Maximization", LpMaximize)

# Decision Variables
x = LpVariable("Scented_Candles", lowBound=0, cat='Integer')
y = LpVariable("Unscented_Candles", lowBound=0, cat='Integer')

# Objective Function
model += 5 * x + 3 * y, "Total_Profit"

# Constraints
model += 3 * x + 2 * y <= 60, "Wax_Constraint"
model += 2 * x + 1 * y <= 40, "Labor_Constraint"

# Solve the Model
model.solve()

# Output Results
print("Status:", LpStatus[model.status])
print("Optimal Scented Candles:", x.varValue)
print("Optimal Unscented Candles:", y.varValue)
print("Maximum Profit: ₹", value(model.objective))
