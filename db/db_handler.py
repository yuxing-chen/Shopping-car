import  json
import os
from conf import settings

# 查看数据
def read_json(username):
    user_path = os.path.join(settings.DB_PATH,f'{username}.json')
    if os.path.exists(user_path):
        with open(user_path,'r',encoding='utf8') as fr:
            user_dic = json.load(fr)
            return user_dic


# 保存数据
def save_json(user_dic):
    user_path = os.path.join(settings.DB_PATH,f'{user_dic.get("username")}.json')
    with open(user_path,'w',encoding='utf8') as fw:
        json.dump(user_dic,fw)
        fw.flush()



