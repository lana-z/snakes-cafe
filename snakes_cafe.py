print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

def cafe_guest():
    order = {}
    while True:
        guest_input = input("> ")
        if guest_input.lower() == 'quit':
            print(f"""
************************************
** Your order will be ready soon. **
** Here's what's coming up:       **
                  
{order}

************************************""")
            break
        order[guest_input] = order.get(guest_input, 0) + 1
        order_count = order[guest_input]
        print(f"** {order_count} order{'s' if order_count > 1 else ''} of {guest_input} {'have' if order_count > 1 else 'has'} been added to your meal **")

cafe_guest()