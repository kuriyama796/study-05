import csv
import datetime

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master

    def check_item_code(self, item_code):
        for s_item in self.item_master:
            if item_code == s_item.item_code:
                return s_item.item_name, s_item.price
        return False

        
    def write_receipt(self, receipt_array):
        total_price = 0
        # 現在時刻の取得
        now = datetime.datetime.now()
        # テキストファイルのパス
        path = 'receipt/{}.txt'.format(now.strftime('%Y%m%d_%H%M%S'))
        with open(path, mode='w', encoding='utf-8') as f:
            for item in receipt_array:
                f.write(item + "\n")
