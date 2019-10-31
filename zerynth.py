def findLowestPrice(products, discounts):
    sales_dict = {x[0]: (x[1], x[2]) for x in discounts}
    lower_prices = 0
    prod_cach = {}
    for product in products:
        prices = []
        for i, sale in enumerate(product):
            if i == 0:
                init_price = int(sale)
                prices.append(init_price)
                price = init_price
            else:
                if sale in sales_dict.keys():
                    if (init_price, sale) in prod_cach.keys():
                        price = prod_cach[(init_price, sale)]
                        prices.append(price)
                    else:

                        if sales_dict[sale][0] == '1':
                            maybe = (round(init_price * (100 - int(sales_dict[sale][1])) / 100))

                            prod_cach[(init_price, sale)] = maybe
                        if sales_dict[sale][0] == '2':
                            maybe = (init_price - int(sales_dict[sale][1]))

                            prod_cach[(init_price, sale)] = maybe
                        if sales_dict[sale][0] == '0':
                            maybe = int(sales_dict[sale][1])
                            prod_cach[(init_price, sale)] = maybe


                        if maybe < price:
                            prices.append(maybe)

        print(prices)
        lower_prices += min(prices)
    return lower_prices





#print(findLowestPrice([['10', 'sale', 'january-sale'], ['200', 'sale', 'EMPTY']], [['sale', '0', '10'], ['january-sale', '1', '10']]))
print(findLowestPrice([['10', 'd0', 'd1'], ['15', 'EMPTY'], ['10', 'd1', 'EMPTY']], [['d0', '1', '10'], ['d1', '2', '5']]))