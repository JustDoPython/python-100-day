import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)
def simple_reply(msg):
    print(msg.text)

itchat.auto_login(hotReload=True)
itchat.run()