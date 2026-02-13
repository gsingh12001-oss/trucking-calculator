print("=== Trucking Profit Calculator===\n")
#Get revenue 
revenue = float (input("Enter monthly revenue: $"))
#Fixed Costs 
print ("\n--- Fixed expenses ---")
truck_payment = float(input("Truck Payment: $"))
trailer_payment = float(input("Trailer payment: $"))
insurance_payment = float(input("Insurance payment: $"))
#Variable Costs 
print("\n--- Variable Expenses ---")
fuel = float(input("Fuel: $"))
driver_pay = float(input("Driver pay: $"))
repair = float(input("Repair: $"))
tolls = float (input("Tolls: $"))
other_costs = float (input("Other costs: $"))
factoring_percent = float (input("Factoring percentage(e.g., 3 for 3%):"))
dispatch_percent = float (input("Dispatch percentage (e.g., 4 for 4%)"))

# calculate expenses 
factoring_cost = revenue*(factoring_percent/100)
dispatch_cost= revenue*(dispatch_percent/100)
fixed_expenses = truck_payment+trailer_payment+insurance_payment
variable_expenses = fuel+driver_pay+repair+tolls+other_costs+dispatch_cost+factoring_cost
total_expenses = fixed_expenses+variable_expenses
#calculate profit 
profit = revenue-total_expenses
#display results 
print("\n RESULTS")
print (f"Total Revenue: ${revenue:,.2f}")
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"\n Total Profit: ${profit:,.2f}")




