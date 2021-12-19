total_items=0
total_spent=0
for x in range(50):
    quantity_from_form = 1
    price_from_form = 10.99
    print("---------")
    total_items += quantity_from_form
    print("total_items",total_items)
    total_charge = quantity_from_form * price_from_form
    print("total_charge",total_charge)
    total_charge = round(total_charge,2)
    print("total_charge rounded",total_charge)
    total_spent+=total_charge
    print("total_spent",total_spent)
    total_spent = round(total_spent,2)
    print("total_spent rounded",total_spent)
