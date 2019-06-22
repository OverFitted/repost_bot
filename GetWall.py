def get_last(authed=None, g_id=None):
    if authed:
        wall = authed.method('wall.get', {'owner_id': '-{}'.format(g_id)})
        try:
            if wall["items"][0]['is_pinned'] == 1:
                return wall["items"][1]
            else:
                return wall["items"][0]
        except:
            return wall["items"][0]
    else:
        return print('Для использования этой функции нужно сначала войти в аккаунт')
