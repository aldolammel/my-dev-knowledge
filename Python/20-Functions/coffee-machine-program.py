from time import sleep

# COLORS ---------------------------------------------------------------------------------------------------------------
corG = '\033[1;32m'  # color in, green
corR = '\033[1;31m'  # color in, red
corY = '\033[1;33m'  # color in, yellow
corX = '\033[m'  # color out

# DEBUGGER -------------------------------------------------------------------------------------------------------------
is_on_debug = False
debug_header = '[DEBUGGING]:'
is_working = True

# DICTS AND LISTS ------------------------------------------------------------------------------------------------------
products = {
    # index: [product name, price, sold, {ingredients}]
    1: ['Espresso', 1.5, 0, {'ingred':
        {
            'Water': 100,
            'Coffee': 76
        }
    }],
    2: ['Latte', 1.5, 0, {'ingred':
        {
            'Water': 20,
            'Powdered milk': 80
        }
    }],
    3: ['Cappuccino', 3, 0, {'ingred':
        {
            'Water': 100,
            'Powdered milk': 50,
            'Coffee': 76
        }
    }]
}
storage_ingreds = {
    # Ingredient: [amount of this ingredient, its measurement unit]
    'Water': [5000, 'ml'],
    'Powdered milk': [10000, 'g'],
    'Coffee': [5000, 'g']
}
storage_money = {
    # coin accepted: [how many coins, coin name]
    1: [20, 'golden'],
    0.5: [50, 'half'],
    0.25: [100, 'quarter'],
    0.10: [100, 'dime'],
    0.05: [100, 'nickle'],
    0.01: [200, 'penny']
}


# FUNCTIONS ------------------------------------------------------------------------------------------------------------
def logo():
    """
    Just the app logotype;
    :return: None;
    """
    print('''
     ██████  ██████  ███████ ███████ ███████ ███████        
    ██      ██    ██ ██      ██      ██      ██             
    ██      ██    ██ █████   █████   █████   █████          
    ██      ██    ██ ██      ██      ██      ██             
     ██████  ██████  ██      ██      ███████ ███████        
                                                            
                                                            
    ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
    ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
    ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
    ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
    ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
    by @aldolammel                                         
                                                        
    ''')
    return None


def should_work(is_report=False, is_turned_off=False):
    """
    This function starts the app. It will check if the machine has enough ingredients to run and if any admin command
    has been requested
    :param is_report: Bool. If admin requests this command, it will show up the machine sale numbers and storage status.
    :param is_turned_off: Bool. If admin requests this command, the machine will be turned off.
    :return: if returning isWorking (False), the machine will turn off. If everything's fine, returns what_u_want().
    """
    global is_working
    sleep(1)

    # Checking all machine storage:
    if is_report:
        print(corY, end='')

        print(f'\nCURRENT INGREDIENTS\' STORAGE:')
        for key, value in storage_ingreds.items():
            print(f'{key} = {value[0]}{value[1]}')

        print(f'\nCURRENT MONEY\'S STORAGE:')
        total_money = 0
        for key, value in storage_money.items():
            print(f'{value[0]}x {value[1]} coin (${key}) = ${value[0] * key:.2f}')
            total_money += (value[0] * key)
        print(f'Total = ${total_money:.2f}')

        print(f'\nPRODUCTS SOLD:')
        for value in products.values():
            print(f'{value[0]} = {value[2]}x = ${value[1] * value[2]:.2f}')

        print(corX)
        sleep(1)

    # Turning the machine off:
    if is_turned_off:
        print(f'\n{corR}This machine will turned off.{corX}')
        sleep(2)
        is_working = False
        return is_working

    # Informing the customer that basic-ingred is missing:
    if storage_ingreds['Water'][0] == 0 or storage_ingreds['Coffee'][0] == 0:
        print(f'\n{corR}This machine\'s storage is dry. Temporally Not working.{corX}')

        if is_on_debug:
            print(f'\n{corY}{debug_header}\n')
            for key, value in storage_ingreds.items():
                print(f'{key} = {value[0]}{value[1]}')
            print(corX)

        is_working = False
        return is_working
    else:
        return what_u_want()


def what_u_want(is_first=True):
    """
    It's called right next the machine is turned on, and when the app will show the product options to the customer;
    :param is_first: Bool. If is the first time the current customer is facing the product menu. Important to check this
    if some product is not available anymore after the customer gives a go (sorry message, for example);
    :return: should_work() if the admin tries an admin command, or check_ingreds() after the customer choices;
    """
    if is_first:
        print('\n\nAVAILABLE HOT DRINKS:')
    else:
        print('\n\nYOU CAN TASTE OUR OTHER HOT DRINKS:')
    for key, value in products.items():
        print(f'{key}. {value[0]}  (${value[1]})')
    print()
    while True:
        try:
            ask_prod_index = str(input(f'\n{corG}What would you like? [use the index number]: {corX}'))

            # checking if the admin is inputting some command:
            if ask_prod_index == 'report':
                return should_work(is_report=True)
            if ask_prod_index == 'off':
                return should_work(is_turned_off=True)

            # checking if a customer is using the product index:
            if ask_prod_index.isnumeric():
                ask_prod_index = int(ask_prod_index)
                if 1 <= ask_prod_index <= len(products):
                    return check_ingreds(ask_prod_index)
                else:
                    print(f'{corR}"{ask_prod_index}" is NOT a product index. Try again!{corX}')
                    continue

            if is_on_debug:
                print(f'{corY}\n{debug_header}\n'
                      f'The user typed "{ask_prod_index}" that\'s = {type(ask_prod_index)}{corX}')

        except (ValueError, TypeError):
            print(f'{corR}An unknown error happened. Sorry. Please, try again!{corX}')


def check_ingreds(prod_index):
    """
    After the customer gives a go in a product, this function will check if the product ingredients are enough to the
    next step;
    :param prod_index: Int. The index number (key) of the products dictionary;
    :return: if everything is fine, it's called to_pay(), otherwise what_u_want(False);
    """
    prod_name = products[prod_index][0]
    prod_ingreds = products[prod_index][3]['ingred']  # e.g: {'Water': 100, 'Coffee': 76}

    if is_on_debug:
        print(f'{corY}Ingredients needed to the {prod_name}: {prod_ingreds}{corX}\n')

    sleep(1)
    print('Checking the ingredients:')
    sleep(0.5)

    for key1 in prod_ingreds:
        print(f'{prod_name}\'s {key1}...')
        sleep(0.5)
        for key2, value in storage_ingreds.items():
            if key1 == key2:
                if prod_ingreds[key1] <= storage_ingreds[key2][0]:
                    if is_on_debug:
                        print(f'{corY}\n{debug_header}\n'
                              f'Available in storage before: {key2} {value[0]}{value[1]}.')

                    # calculating how many of this ingredient goes be available from here:
                    storage_ingreds[key2][0] = storage_ingreds[key2][0] - prod_ingreds[key1]

                    if is_on_debug:
                        print(f'Available in storage now: {key2} {storage_ingreds[key2][0]}{value[1]}.{corX}\n')

                else:
                    print(f'{corR}Unforgettably, one or more ingredients are missing. So sorry!{corX}\n')
                    sleep(1)
                    return what_u_want(False)

    return to_pay(prod_index)


def to_pay(prod_index):
    """
    Product payment management. The function will check the available coins in the money storage and the product
    prices. The machine will request coins until the customer pays the price and, just in case, return their change;
    :param prod_index: Int. The index number (key) of the products dictionary;
    :return: next the payment (and change when needed), it calls preparing();
    """
    prod_name = products[prod_index][0]
    prod_price = products[prod_index][1]
    acceptable_coins = list()
    customer_money = 0
    sleep(1)
    for coin in storage_money.keys():
        acceptable_coins.append(coin)

    # Calculating how many coins to buy:
    # TODO gives an option to the customer cancel their order.
    while customer_money < prod_price:
        print(f'\nAcceptable coins: {acceptable_coins}')
        try:
            ask_money = float(input(f'{corG}Please, insert ${prod_price - customer_money:.2f} in coins: {corX}'))
        except (ValueError, TypeError):
            print(f'{corR}Use only integer or float numbers to insert your coins.{corX}')
        else:
            if ask_money not in acceptable_coins:
                sleep(1)
                print(f'\n{corR}This coin is not accept in this machine. Take it back!{corX}\n')
                sleep(1)
                continue
            else:
                customer_money += ask_money
                for key in storage_money.keys():
                    if key == ask_money:
                        storage_money[key][0] = storage_money[key][0] + 1

                if is_on_debug:
                    print(f'\n{corY}{debug_header}\n'
                          f'Product price: ${prod_price}\n'
                          f'Customer already inserted a total of ${customer_money:.2f}{corX}.\n')

    # Calculating the customer change:
    # TODO if not enough specific coin, try another one. If not coins to change the customer, gives back customer...
    # TODO ...money, cancel the order, say sorry and turn the machine off.
    if customer_money > prod_price:
        customer_change = customer_money - prod_price
        print(f'{corG}Please, take your change: ${customer_change:.2f}{corX}\n')

        # Calculating which coins the machine will return to the customer:
        print(corG, end='')
        print(f'You\'ve took back', end='    ')
        while customer_change != 0:
            if customer_change >= 1:
                print('$1', end='    ')
                storage_money[1][0] = storage_money[1][0] - 1
                customer_change -= 1
                sleep(0.2)
            if 0.5 <= customer_change < 1:
                print('$0.50', end='    ')
                storage_money[0.5][0] = storage_money[0.5][0] - 1
                customer_change -= 0.5
                sleep(0.2)
            if 0.25 <= customer_change < 0.5:
                print('$0.25', end='    ')
                storage_money[0.25][0] = storage_money[0.25][0] - 1
                customer_change -= 0.25
                sleep(0.2)
            if 0.1 <= customer_change < 0.25:
                print('$0.10', end='    ')
                storage_money[0.1][0] = storage_money[0.1][0] - 1
                customer_change -= 0.1
                sleep(0.2)
            if 0.05 <= customer_change < 0.1:
                print('$0.05', end='    ')
                storage_money[0.05][0] = storage_money[0.05][0] - 1
                customer_change -= 0.05
                sleep(0.2)
            if 0.01 <= customer_change < 0.05:
                print('$0.01', end='    ')
                storage_money[0.01][0] = storage_money[0.01][0] - 1
                customer_change -= 0.01
                sleep(0.2)
            # Avoiding huge float results, e.g. 0.00000005 that isn't zero and would bring a bug calc:
            customer_change = float(f'{customer_change:.2f}')
        print(corX)
        sleep(2)
    return preparing(prod_index, prod_name)


def preparing(prod_index, prod_name):
    """
    Right next to payment, this function will prepare the requested drink;
    :param prod_index: Int. The index number (key) of the products dictionary;
    :param prod_name: Str. The commercial name of the product from products dictionary;
    :return: calls delivery() if everything is okay with preparation stage;
    """
    sleep(1)
    print(f'\nPreparing your hot drink...')
    sleep(4)
    is_ready = True
    return delivery(prod_index, prod_name, is_ready)


def delivery(prod_index, prod_name, is_ready):
    """
    When the drink is ready, this function is called;
    :param prod_index: Int. The index number (key) of the products dictionary;
    :param prod_name: Str. The commercial name of the product from products dictionary;
    :param is_ready: Bool. If the drink is ready or not to delivery;
    :return: an okay message or a not okay one;
    """
    if is_ready:
        # counting how many of this product has been sold:
        products[prod_index][2] = products[prod_index][2] + 1
        return print(f'\n{corG}Have a good {prod_name}!{corX}\n\n')
    else:
        return print(f'{corR}Something goes wrong! I\'m so sorry!\nTake back your cash.\nCan you try again?{corX}')


# APP RUNNING ----------------------------------------------------------------------------------------------------------
while is_working:
    logo()
    if is_on_debug:
        print(f'{corY}\n{debug_header}\n'
              f'How many products: {len(products)}.\n'
              f'Secret words to the admin:\n'
              f'>> report = shows the ingredient\'s storage available.\n'
              f'>> off = turn this machine off to maintenance.{corX}\n\n')
    should_work()

print(f'{corR}This machine is off!{corX}')
