import random

# Define parameters
order_cost = 100
holding_cost = 5
total_order_cost = 0
total_holding_cost = 0
demand_cumulative_probability = [0, 20, 70, 85, 95, 100]
demand_lst = [0, 1, 2, 3, 4]
lead_time_probability = [0, 10, 35, 85, 95, 100]
lead_time = [1, 2, 3, 4, 5]
inventory = 8
n = 30  # Number of periods to simulate
sell = 0  # Total sales fulfilled
lost = 0  # Total lost sales
reorder_point = 3
order_quantity = 5

# Function to determine lead time based on random number
def lead_time_func():
    rn = random.randint(1, 100)
    for i in range(len(lead_time_probability) - 1):
        if lead_time_probability[i] < rn <= lead_time_probability[i + 1]:
            return lead_time[i]

# Simulation variables
order_in_progress = False
count = -1

# Run simulation for n periods
for _ in range(n):
    # Determine demand based on random number
    demand = 0
    rn = random.randint(1, 100)
    for i in range(len(demand_cumulative_probability) - 1):
        if demand_cumulative_probability[i] < rn <= demand_cumulative_probability[i + 1]:
            demand = demand_lst[i]

    # Fulfill demand and track sales/lost sales
    if inventory >= demand:
        inventory -= demand
        sell += demand
    else:
        lost += demand - inventory
        inventory = 0

    # Check for reorder condition
    if inventory <= reorder_point and not order_in_progress:
        order_in_progress = True
        count = lead_time_func()
        total_order_cost += order_cost

    # Calculate holding cost for the period
    total_holding_cost += inventory * holding_cost

    # Manage order arrival timing
    if count > 0:
        count -= 1
    if count == 0 and order_in_progress:
        order_in_progress = False
        inventory += order_quantity

# Display simulation results
print(f"Inventory System Simulation Summary:\n"
      f"Total Order Cost: {total_order_cost}\n"
      f"Total Holding Cost: {total_holding_cost}\n"
      f"Total Lost Sales: {lost}\n"
      f"Total Sales Fulfilled: {sell}")



# order_cost: Cost of placing an order (100 units). Added when inventory reaches reorder point.
# holding_cost: Cost of holding each inventory unit per period (5 units), calculated based on end-period inventory.
# total_order_cost: Cumulative cost of all orders placed during simulation.
# total_holding_cost: Accumulated holding cost over all periods.
# demand_cumulative_probability: Cumulative probability list for demand levels (%), defining the likelihood of each demand level.
# demand_lst: List of possible demand values; used with demand_cumulative_probability to determine demand each period.
# lead_time_probability: Cumulative probability distribution for order lead times (%), representing different lead time probabilities.
# lead_time: List of lead times (periods), used with lead_time_probability to determine each order’s lead time.
# inventory: Starting inventory level (8 units), tracking stock available each period.
# n: Number of periods to simulate (30), representing each cycle of inventory check, demand fulfillment, and ordering.
# sell: Total units of demand fulfilled in the simulation.
# lost: Total unmet demand (lost sales) due to insufficient inventory.
# reorder_point: Inventory threshold (3 units) at which a new order is triggered.
# order_quantity: Units ordered when reorder is triggered (5 units), added to inventory after lead time.
