from lib import common
from interface import user,bank,store



user_info = ['']

def register():
    while True:
        username = input('请输入用户名：').strip()
        pwd = input('请输入用户密码：').strip()
        re_pwd = input('请输入确认密码：').strip()
        if re_pwd == pwd:
            flag,msg = user.register_intrerface(username,pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break

        else:
            print('两次密码输入不一致！')




def login():

    while True:
        username = input('请输入用户名：').strip()
        pwd = input('请输入用户密码：').strip()
        flag,msg = user.login_interface(username,pwd)
        if flag:
            print(msg)
            user_info[0] = username

            break
        else:
            print(msg)


@common.login_auth
def check_extra():
    print('查看余额！')
    extra = bank.check_extra_interface(user_info[0])
    print(extra)





@common.login_auth
def withdraw():
    while True:
        money = input('请输入取款金额：').strip()
        if not money.isdigit():
            print('傻逼，金额必须是数字，滚回去重新输入。。')
            continue
        flag,msg = bank.withdraw_interface(user_info[0],int(money))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            choice = input('是否继续取款(y/n):')
            if not choice.isalpha():
                print('瞎了？？')
                continue
            elif choice == 'y':
                continue
            elif choice == 'n':
                break




@common.login_auth
def transfer():
    while True:
        to_username = input('请输入对方用户名:')
        money = input('请输入转账金额:')
        if not money.isdigit():
            print('傻逼，金额必须是数字。。。。')
            continue

        flag ,msg = bank.transfer_interface(user_info[0],to_username,int(money))
        if flag:
            print(msg)
            break
        else:
            print(msg)




@common.login_auth
def repay():
    while True:
        money = input('请输入还款金额:')
        if not money.isdigit():
            print('你是傻逼？，金额是数字不知道吗？？回去重新输入。')
            continue
        flag ,msg = bank.repay_interface(user_info[0],int(money))
        if flag:
            print(msg)
            break




@common.login_auth
def history():
    msg = bank.history_interface(user_info[0])
    for i in msg:
        print(i)




@common.login_auth
def shopping():
    flag,msg = store.shopping_interface(user_info[0])
    if flag:
        print(msg)





@common.login_auth
def shop_car():
    from db import db_handler
    while True:
        shop_car = db_handler.read_json(user_info[0])
        user_shop_car = shop_car['shop_car']
        user_money = store.price[0]
        if user_money == 0:
            print('滚，你没有买东西')
            break

        print(f'您购买的商品:{user_shop_car}')
        print(f'商品总价格为:{user_money}')

        choice = input('是否需要付款（y:付款/n:清空购物车）:')

        if (choice.isalpha() and choice != 'y' and choice != 'n') or choice.isdigit():
            print('你瞎了吗？？，看不懂提示？？，归回去重新输入。。。。')
            continue

        flag,msg = store.shopping_car_interface(user_info[0],choice)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break








@common.login_auth
def logout():
    pass



FUNC_DICT = {
    '1':register,
    '2':login,
    '3':check_extra,
    '4':withdraw,
    '5':transfer,
    '6':repay,
    '7':history,
    '8':shopping,
    '9':shop_car,
    '10':logout,
}
def run():

    while True:
        FUNC_MSG = {1:'注册',2:'登录',3:'查看额度',4:'提现',5:'转账',6:'还款',7:'查看流',8:'购物',9:'购物车',10:'注销','q':'退出'}
        for k,v in FUNC_MSG.items():
            print(f'{k}:{v}',end='   ' )

        choice = input('请选择功能(q退出):').strip()

        if choice == 'q':
            break

        func = FUNC_DICT.get(choice)
        if not func:
            print('没有这个功能，请重新选择')
            continue

        func()




if __name__ == '__main__':
    run()