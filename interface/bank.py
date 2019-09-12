from db import db_handler

# 查看余额接口
def check_extra_interface(username):
    user_dic = db_handler.read_json(username)
    extra = user_dic['extra']

    msg= f'{username}查看了余额，余额为:{extra}'
    user_dic['history'].append(msg)
    db_handler.save_json(user_dic)

    return user_dic.get('extra')



# 取款接接口
def withdraw_interface(username,money):
    user_dic = db_handler.read_json(username)
    withdraw_money = money*1.05
    if user_dic.get('extra') >= withdraw_money:
        user_dic['extra'] -= withdraw_money
        msg = f'{username}取款成功，取款金额:{money},手续费为{withdraw_money-money}'
        user_dic['history'].append(msg)
        db_handler.save_json(user_dic)


        return True,msg
    return False,'滚，余额不够！'




# 转账接口
def transfer_interface(username,to_username,money):

    to_username_dic= db_handler.read_json(to_username)
    if not to_username_dic:
        return False,'傻逼，用户不存在，你转给谁'

    username_dic = db_handler.read_json(username)
    if username_dic['extra'] >= money:
        username_dic['extra'] -= money
        to_username_dic['extra'] += money


        msg = f'{username}向{to_username}转了{money}元'
        username_dic['history'].append(msg)

        to_username_dic['history'].append( f'{to_username}收到了{username}转的{money}元')

        db_handler.save_json(username_dic)
        db_handler.save_json(to_username_dic)
        return True,msg

    return False,'傻逼，转账之前不会查看一下余额？？'


# 还款接口
def repay_interface(username,money):
    user_dic = db_handler.read_json(username)

    user_dic['extra'] += money
    db_handler.read_json(user_dic)

    msg = f'{username}还款成功,还款金额为:{money}'
    user_dic['history'].append(msg)
    db_handler.save_json(user_dic)

    return True,msg


# 查看流水接口
def history_interface(username):
    user_dic = db_handler.read_json(username)
    return user_dic['history']
