import itchat


def get_head_pic():
    itchat.auto_login()
    for friend in itchat.get_friends(update=True)[0:]:
        # 可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
        print(friend['NickName'], friend['RemarkName'], friend['Sex'], friend['Province'], friend['Signature'])
        img = itchat.get_head_img(userName=friend["UserName"])
        path = "C:/Users/MC/Desktop/HeadImages1/" + friend['NickName'] + "(" + friend['RemarkName'] + ").jpg"
        try:
            with open(path, 'wb') as f:
                f.write(img)
        except Exception as e:
            print(repr(e))
    itchat.run()


def send_msg():
    itchat.auto_login()
    for i in range(0, 20):
        itchat.send(u'测试消息发送' + str(i), 'filehelper')


if __name__ == '__main__':
    # get_head_pic()
    send_msg()
