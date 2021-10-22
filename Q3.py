
from __future__ import print_function
import shop

def shopSmart(orderList, fruitShops):

    shop1 = fruitShops[0]
    shop2 = fruitShops[1]
    shop1_Cost = shop1.getPriceOfOrder(orderList)
    shop2_Cost = shop2.getPriceOfOrder(orderList)
    if (shop1_Cost > shop2_Cost):
        shop=shop2
    else:
        shop=shop1
    return shop 

if __name__ == '__main__':
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())

