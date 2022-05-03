from datetime import datetime

name = input('Enter your name: ')

lists = '''
rice    rs 40/kg
sugar   rs 30/kg
salt    rs 10/kg
oil     rs 120/litre
panner  rs 140/kg
maggi   rs 40/packet
boost   rs 90/kg
colgate rs 50/each
'''

# declaration
price = 0
price_list = []
total_price = 0
final_price = 0
item_list = []
quantity_list = []
p_list = []


items = {
    'rice': 40,
    'sugar': 30,
    'salt': 10,
    'oil': 120,
    'panner': 140,
    'maggi': 40,
    'boost': 90,
    'colgate': 50
}

option = int(input('for list of items press 1: '))
if option == 1:
    print(lists)

for i in range(len(items)):
    choose = int(input('if you want to buy press 1 or 2 for exit: '))
    if choose == 2:
        break
    if choose == 1:
        item = input('enter your item: ')
        quantity = int(input('enter quantity in numbers: '))
        if item in items.keys():
            price = quantity * items[item]
            price_list.append((item,quantity,price))
            total_price += price
            item_list.append(item)
            quantity_list.append(quantity)
            p_list.append(price)
            gst = (total_price*5)/100
            final_price = gst + total_price
        else:
            print("sorry you entered item is not available")
    else:
        print('You entered wrong number')
    
    bill = input('can i bill the items, yes or no: ')
    if bill == 'yes':
        pass
        if final_price != 0:
            print(25*"=","Kirana supermarket",25*"=")
            print(28*" ","Hyderabad")
            print("Name:",name,30*" ","Date",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","Quanity",3*" ",'price')
            for i in range(len(price_list)):
                print(i,10*" ",item_list[i],8*" ",quantity_list[i],9*" ",p_list[i])
            print(75*'-')
            print(50*' ',"TotalAmount",'Rs',total_price)
            print('gst amount:',50*" ",'Rs',gst)
            print(75*'-')
            print(50*' ',"FinalAmount:",'Rs',final_price)
            print(75*'-')
            print(20*' ',"Thanks for visiting")
            print(75*'-')