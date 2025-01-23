# Elise Henry (Driver) U57226177
# Adam Bricha (Navigator) U92335585
# Assignment 7: Retail Items
# A program where we used a class method that included data with a specific item, quantity of
# the item and the price of it. The program then displayed, based on the input given by the user, an array
# of information describing the items wanted by the user.


class RetailItem:
    def __init__(self, item_type, amount, price):
        self._item_type = item_type
        self._amount = amount
        self._price = price

    def __str__(self):
        output = '{:<20}{:<10}${:<10.2f}'.format(self._item_type, str(self._amount), self._price)
        return output


def main():
    name = input('Name of item 1: ')
    amount = int(input('Count of item 1: '))
    price = float(input('Price of item 1 ($): '))
    item1 = RetailItem(name, amount, price)
    print()
    name = input('Name of item 2: ')
    amount = int(input('Count of item 2: '))
    price = float(input('Price of item 2 ($): '))

    item2 = RetailItem(name, amount, price)
    print()
    print('Here is a summary of the items you added:')
    print('{:<20}{:<10}{:<10}'.format('Item', 'Amount', 'Price'))
    print('-------------------------------------')

    print(item1)
    print(item2)


main()