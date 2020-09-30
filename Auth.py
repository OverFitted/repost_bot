import vk_api


def auth_handler():
    key = int(input("2 auth factor code: "))

    remember_device = True

    return key, remember_device


def auth(login=None, password=None, token=None):
    if token:
        group = vk_api.VkApi(token=token)
        return group
    elif login and password:
        try:
            me = vk_api.VkApi(login=login, password=password)
            me.auth()
        except:
            me = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
            me.auth()
        return me
    else:
        return print('Need pass and login or group token')
