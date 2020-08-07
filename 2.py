import sys
import time
import pymysql
from prettytable import PrettyTable


class GoodsManage:
    def show(self):
        print('\n' + '- ' * 7, '商品管理系统', ' -' * 7, '\n1: 添加商品\n2: 查询所有\n', '- ' * 20)
        s = input('请输入功能对应的序号:')
        self.hand_request(s)

    def hand_request(self, s):
        if s == '1':
            self.toadd()
        elif s == '2':
            self.toshow()
        else:
            print('输入错误 请从新输入')

    def toadd(self):
        data_name = input('请输入商品的名称:')
        data_price = input('请输入商品的价格:')
        mysql = pymysql.connect(host='192.168.111.131',
                                port=3306,
                                user='root',
                                password='mysql',
                                database='heima',
                                charset='utf8'
                                )

        cursor = mysql.cursor()
        try:
            sql = "insert into goods values(null, " + data_name + ',' + data_price + ")"
            cursor.execute(sql)
        except Exception as e:
            print('商品已存在 请重新输入')
            mysql.rollback()
        else:
            print('添加成功')
            mysql.commit()
        finally:
            cursor.close()
            mysql.close()

    def toshow(self):
        mysql = pymysql.connect(host='192.168.111.131',
                                port=3306,
                                user='root',
                                password='mysql',
                                database='heima',
                                charset='utf8'
                                )
        cursor = mysql.cursor()
        try:
            sql = "select * from goods"
            cursor.execute(sql)
            rel = cursor.fetchall()
        except Exception as e:
            print('查询错误 请重新输入')
        else:
            table = PrettyTable(["商品序号", "商品名称", "商品价格"])
            for i in rel:
                table.add_row([i[0], i[1], i[2]])
            print(table)
        finally:
            cursor.close()
            mysql.close()

    def run(self):

        def progress_bar():
            for i in range(1, 101):
                print("\r", end="")
                print("商品管理系统正在加载中: {}%: ".format(i), "▋" * (i // 2), end="")
                sys.stdout.flush()
                time.sleep(0.05)

        progress_bar()
        while True:
            self.show()


hand = GoodsManage()
if __name__ == '__main__':
    hand.run()
