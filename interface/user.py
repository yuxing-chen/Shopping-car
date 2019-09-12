from db import db_handler
from core import src

# 注册接口
def register_intrerface(username,pwd):
    user_dic = db_handler.read_json(username)

    if user_dic:
        return False,'用户已存在'

    # 用户信息
    user_dic = {'username':username,'pwd':pwd,'extra':15000,'history':[],'lock':False,'shop_car':{}}
    db_handler.save_json(user_dic)
    return True,f'{username}注册成功'


# 登录接口
def login_interface(username,pwd):
    user_dic = db_handler.read_json(username)
    if not user_dic:
        return False,'用户不存在'

    if user_dic.get('pwd') == pwd:
        return True,f'{username}登录成功'
    else:
        return False,f'{username}用户密码错误'
