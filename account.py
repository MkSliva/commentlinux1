import random
class Account(object):

    message_list=[]
    mode = 'None'
    # last_join_chat = 0
    timeout=5
    spam = False
    count_success = 0
    chats_for_ioin = []
    chats_list = []
    posts = []
    send_as = None
    # last_join_chats=""
    # id_chat=0

    def __init__(self, client):
        self.client=client

    
    def сomment_text(self):
        if len(self.message_list)>0:
            return random.choice(self.message_list)
        else:
            print('Нет шаблонов для комментариев!')
            return None

