from time import sleep
import os
from random import randint
from foods import food_list

class FoodOrderManagement:
    def __init__(self):
        self.food_list = food_list
        self.staff_passwords = ['john354', 'david173', 'sam968']
        self.orders = []

    def print_options(self):
        print('-' * 20)
        print('1. View available foods')
        print('2. Order your food')
        print('3. Track your order')
        print('4. View Staff menu')
        print('5. Exit')
        print('-' * 20)

    def print_staff_options(self):
        print('-' * 20)
        print('1. Check orders')
        print('2. Mark order as prepared')
        print('3. Back')
        print('-' * 20)

    def add_order(self, order):
        self.orders.append(order)


if __name__ == '__main__':
    fom = FoodOrderManagement()
    os.system('cls')
    print('Welcome to the Food Order Management System')
    while True:
        sleep(1)
        fom.print_options()
        option = input('Choose an option: ')
        if option == '1':
            print('\nAvailable foods:\n')
            print('\n'.join(list(map(lambda x: f"{fom.food_list.index(x) + 1}. {x['name']} [Price: {x['price']}]\n", fom.food_list))))
        elif option == '2':
            customer_name = input('\nEnter your name: ')
            item_no = int(input('Enter your item no: '))
            while item_no == 0 or item_no > len(fom.food_list):
                item_no = int(input("That's not a valid item no.\nEnter a valid item no: "))
            quantity = int(input('Enter the quantity you want to buy: '))
            customer_order_id = randint(1000, 2000)
            item = fom.food_list[item_no - 1]['name']

            print('\nOrder details:')
            print('-' * 20)
            print(f'Name: {customer_name}')
            print(f"Item: {item}")
            print(f'Quantity: {quantity}')
            print('-' * 20)

            decision = input('\nAre you sure you want to place your order with the above details? (yes/no): ')
            if decision == 'yes':
                fom.add_order({
                    "name": customer_name,
                    "item": item,
                    "quantity": quantity,
                    "order_id": customer_order_id,
                    "status": "cooking"
                })
                print('\nThank you for placing your order. You will be notified once your order is ready.')
                print(f'Here is your Order ID: {customer_order_id}')
                print('Note: Keep your Order ID safe to track your order.\n')
            elif decision == 'no':
                print('\nCancelled your order.\n')
        elif option == '3':
            order_id = int(input("\nEnter your Order ID: "))
            order = None
            for i in fom.orders:
                if i['order_id'] == order_id:
                    order = i

            if order is not None:
                print('\nOrder details:')
                print('-' * 20)
                print(f"Name: {order['name']}")
                print(f"Item: {order['item']}")
                print(f"Quantity: {order['quantity']}")
                print(f"Order ID: {order['order_id']}")
                print(f"Status: {order['status']}")
                print('-' * 20)
                print('\n')
            else:
                print('\nNo valid orders found with the given Order ID.\n')
        elif option == '4':
            password = input('\nEnter your staff password: ')
            if password not in fom.staff_passwords:
                print('Incorrect password. Access denied.\n')
            else:
                print('\nWelcome staff')
                while True:
                    sleep(1)
                    fom.print_staff_options()
                    staff_option = input('Choose an option: ')
                    if staff_option == '1':
                        if len(fom.orders) > 0:
                            print('\nAvailable orders:')
                            print('\n'.join(list(map(lambda x: f"{'-' * 20}\nName: {x['name']}\nItem: {x['item']}\nQuantity: {x['quantity']}\nOrder ID: {x['order_id']}", fom.orders))))
                            print('-' * 20)
                            print('\n')
                        else:
                            print('\nNo orders are available right now.\n')
                    elif staff_option == '2':
                        done_order_id = int(input("Enter the order id that you want to mark as prepared: "))
                        while done_order_id < 1000 or done_order_id > 2000:
                            done_order_id = int(input("That's not a valid order id.\nEnter a valid order id: "))
                        order_update = None
                        for i in fom.orders:
                            if i['order_id'] == done_order_id:
                                order_update = i
                        if order_update is None:
                            print('No valid orders found with the given order id.')
                        else:
                            pos = fom.orders.index(order_update)
                            modified = {
                                "name": order_update['name'],
                                "item": order_update['item'],
                                "quantity": order_update['quantity'],
                                "order_id": order_update['order_id'],
                                "status": 'Prepared'
                            }
                            fom.orders[pos] = modified
                            print(f'\nTo: {modified["name"]}\nMessage: Hello {modified["name"]}, Your order for {modified["quantity"]} {modified["item"]} have been {modified["status"]} and you can get it delivered.\n')
                            print('The user has been notified with the order delivery message.\n')
                    elif staff_option == '3':
                        print('\nGoing back to regular options...\n')
                        break
                    else:
                        print('Invalid option.')
        elif option == '5':
            print('Exiting...')
            break
        else:
            print('Invalid option.')
