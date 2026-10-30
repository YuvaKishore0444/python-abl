catalogue = [
    ("P101", 10.50, 25),
    ("P102", 5.00, 5),
    ("P103", 20.00, 8)
]

reorder_threshold = 10

print("--- Product Catalogue Inventory Audit ---")

for prod_id, price, stock in catalogue:
    total_inventory_value = price * stock

    if stock < reorder_threshold:
        reorder_flag = "ATTENTION: REORDER NEEDED"
    else:
        reorder_flag = "STATUS: OK"

    print(f"Product ID: {prod_id} | Price: ${price:.2f} | Stock: {stock} | Inventory Value: ${total_inventory_value:.2f} | {reorder_flag}")