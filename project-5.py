venue_cost = 500.0
equipment_cost = 200.0
catering_cost = 300.0
ticket_price = 25.0

total_expenses = venue_cost + equipment_cost + catering_cost
break_even_participants = total_expenses / ticket_price

print("--- Event Budget Summary ---")
print(f"Venue Expense:     ${venue_cost:.2f}")
print(f"Equipment Expense: ${equipment_cost:.2f}")
print(f"Catering Expense:  ${catering_cost:.2f}")
print(f"Total Budget Needed: ${total_expenses:.2f}")
print("----------------------------")
print(f"Minimum Registrations Needed (@ ${ticket_price:.2f}/person): {int(break_even_participants)}")