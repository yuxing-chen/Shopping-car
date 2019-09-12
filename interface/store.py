from db import db_handler



shopping_car = dict()
price = [0]

def goods():
    with open('E:\python folder\正式班\day20\ATM架构\goods.txt','r',encoding='utf8') as fr:
        goods_list = fr.read()
        goods_list = eval(goods_list)

        return goods_list

goods_list = goods()


# 购物接口
def shopping_interface(username):
    user_dic = db_handler.read_json(username)
    while True:
        for i ,goods in enumerate(goods_list):
            print(f'商品编号:{i}:{goods}')

        choice = input('请输入商品编号(q-->break):')
        if choice == 'q':
            break

        if choice != 'q' and choice.isalpha():
            print('傻逼，商品编号是数字，滚回去重新输入。。。。')
            continue

        choice = int(choice)
        goods =goods_list[choice]
        goods_name = goods[0]
        if goods_name in shopping_car:
            shopping_car[goods_name] += 1
            user_dic['shop_car'][goods_name] += 1
        else:
            shopping_car[goods_name] = 1
            user_dic['shop_car'][goods_name] = 1

        db_handler.save_json(user_dic)
        price[0] += int(goods[1])
        print(f'商品:{goods_name}-->已加入购物车\n')


    return True,f'购买商品为：{shopping_car},商品价格为：{price[0]}'




# 购物车接口
def shopping_car_interface(username,choice):
    user_dic = db_handler.read_json(username)


    if choice == 'y':
        if user_dic['extra'] >= price[0]:
            user_dic['extra'] -= price[0]
            user_dic['shop_car'].clear()

            msg = f'{username}已购物成功，消费金额为：{price[0]}'
            user_dic['history'].append(msg)
            db_handler.save_json(user_dic)
            return True,msg
        else:
            return False,'滚去还款，钱不够了，购物车已保存'

    elif choice == 'n':
        user_dic['shop_car'].clear()
        db_handler.save_json(user_dic)
        shopping_car.clear()
        price[0] = 0
        return False,'你取消了付款，购物车已经清空了。。。。。'


