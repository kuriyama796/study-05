import eel
import desktop
from pos_system import Item
from pos_system import Order
import csv
import os.path

app_name="html"
end_point="index.html"
size=(700,600)

item_master = []

@ eel.expose
def csv_exists(file_name):
    if os.path.isfile(file_name + '.csv'):
        register_master(file_name + '.csv')
        return True
    else:
        return False

# マスタ登録
@ eel.expose
def register_master(file_name):
    with open(file_name, 'r', encoding="utf-8_sig") as f:
        reader = csv.reader(f)
        for line in reader:
            item_master.append(Item(line[0], line[1], line[2]))

@ eel.expose
def check_item_code(item_code):
    order = Order(item_master)
    return order.check_item_code(item_code)

@ eel.expose
def write_text(receipt_array):
    order = Order(item_master)
    order.write_receipt(receipt_array)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)