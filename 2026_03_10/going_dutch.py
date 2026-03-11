# going dutch
num_of_ppl = 3
food_prices = [10000, 20000, 15000, 17000, 50000]

def going_dutch(food_prices: list, num_of_ppl: int):
    total = 0
    for food_price in food_prices:
        total += food_price
    print(f"Your total is {total}")
    return float(total) / num_of_ppl

bill = going_dutch(food_prices=food_prices, num_of_ppl=num_of_ppl)

print(bill)