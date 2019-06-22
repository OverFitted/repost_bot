from Auth import auth
from GetWall import get_last
from Send import send_message
import time

login = input('Введите логин/телефон аккаута: ')
password = input('Введите пароль аккаунта: ')

me = auth(login=login, password=password)
group = auth(token=input('Введите токен сообщества: '))

group_id = int(input('Введите id группы: '))

last_date = 0
while 1:
    post = get_last(authed=me, g_id=group_id)
    date = post['date']
    if last_date != date:
        send_message(authed=group, post=post)
        last_date = date
    else:
        time.sleep(3)
