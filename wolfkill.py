import itchat
from itchat.content import *
import time

time_full = time.asctime(time.localtime(time.time()))
time_MH = time.strftime("%m" , time.localtime()) + "月" + time.strftime("%d" , time.localtime()) + "日"
login_sucees = time_full + " Login Succeed"


chat_pipixia = "@@4bc86fb67970cf22b1ec13d07b0b5a7a69b7e3c033bb3e432d17f8e28c252e1f"
wolf_date = time.strftime("%m-%d", time.localtime())
wolf_rule = "开组开组杀狼12人标准局，多人开第二桌，女巫不能自救，报名集合啦，下午7点半开车啦👌👩🔫🙄🐺🐺🐺🐺👤👤👤👤"
wolf_list = []
WOLF_MAX = 12
#--------------------------------------#

#判断是否收到报名
def wolf_judge(room, msg):
    if(room == chat_pipixia):
        if(msg == "狼人杀报名") :
            return True
            print("Get the order")
        else:
            return False
    else:
        return False

#微信退出时报告
def ec():
    itchat.send("Exit", toUserName='filehelper')

#读取狼人杀玩家今天的列表
#包括查重，查人数是否超过
def read_wolf_list(name):   
    length = len(wolf_list)
    msg = ""
    if(length >= 12):
        msg = "抱歉，今晚的人数已满"
        return msg
    else:
        if(wolf_repeat(name) == False):
            msg = "你已经报名了哦"
            return msg
        else :
            wolf_list.append(name)
            msg = wolf_date + "\n" + wolf_rule + "\n\n"
            i = 1
            for item in wolf_list :
                msg_add = str(i) + " " + wolf_list[i-1] + "\n"
                msg+= msg_add
                i = i + 1
            return msg

def wolf_repeat(name):
    for item in wolf_list :
        if item == name :
            return False
    return True


#----------API修改----------------#

#----------for test--------------#
@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def text_reply(msg):
    text_reply_firstline = "The User " + msg['ActualNickName'] + " Send A Message" + "From Chat Room " + msg['FromUserName']
    text_reply_secondline = "Message is " + msg['Text']
    print(msg['Text'])
    itchat.send_msg(msg= text_reply_firstline, toUserName=msg['FromUserName'])
    itchat.send_msg(msg= text_reply_secondline, toUserName=msg['FromUserName'])

#---------for use-----------------#
@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def text_reply(msg):
    print(msg['FromUserName'])
    state = wolf_judge(msg['FromUserName'],msg['Text'])
    if(state == True) :
        msg_wolf = read_wolf_list(msg['ActualNickName'])
        itchat.send_msg(msg= msg_wolf, toUserName=msg['FromUserName'])
        
    
#--------------------------------------#
itchat.auto_login(hotReload=True,exitCallback=ec)

itchat.send(login_sucees, toUserName='filehelper')

itchat.run()
