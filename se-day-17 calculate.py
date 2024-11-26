original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the allowable discount_percent: "))

def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        print(f'Sorry, enter a valid discount')
    elif discount_percent >= 20:
        discount = original_price * discount_percent / 100
        final_price = original_price - discount
        print(f'The final price after discount is: {final_price}')
    else:
        print (f'The final price is {original_price}')

calculate_discount(original_price, discount_percent)
