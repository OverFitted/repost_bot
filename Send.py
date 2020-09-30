def send_message(authed, post):
    authed.method("messages.send", {"chat_id": 1,
                                    "message": 'New post',
                                    "random_id": 0,
                                    "attachment": 'wall{}_{}'.format(post['owner_id'], post['id'])})

    return 0
