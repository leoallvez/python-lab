products = [['apples', 10, 0.30], ['pears', 12, 0.75], ['kiwis', 13, 1.7]]

for p in products:
    print('product: {}, amount: {}, price: {}'.format(*p))
