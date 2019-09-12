

def login_auth(func):

    from core import src

    def inner(*args,**kwargs):

        if src.user_info[0]:

            res = func(*args,**kwargs)
            return res
        else:
            print('未登录，请先登录')
            src.login()
            res = func(*args, **kwargs)
            return res


    return inner