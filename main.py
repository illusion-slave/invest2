
import datetime
import json
import requests
 
from WeChatPush import WechatMessagePush
 
def get_info2():
    url = "http://hslhapp.hhws168.com/common/v1/jsonDownload/"
    headers = {
        "Host": "hslhapp.hhws168.com",
        "Token":"3a90beddb879790a606bcb1141e325d9",
        "Content-Encoding": "gzip",
        "Versioncode":"1.2.8",
        "Channel":"alphago",
        "Content-Type":"application/json;charset=utf-8",
        "Content-Length":"156",
        "Connection": "Keep-Alive",
        "Accept-Encoding":"gzip",
        "User-Agent":"okhttp/3.8.0"
    }
    #date = "2022-11-04"
    date = str(datetime.date.today())
    body = {"option0": "alphaGo",
        "option1": "server",
        "option2": "minuteUpShadow",
        "option3": "stockData",
        "option4": str(date),
        "option5": "9999",
        "truncation": "cut20191111"
    }
    responses = requests.post(url = url,data = json.dumps(body),headers = headers)
    return responses
 
def parse_info(res2):
    json1 = json.loads(res.text)
    dict1 = dict(json1)
    list1 = dict1.get("data")
    str1 = ''.join(list1)
    list2 = json.loads(str1)
    # for i in range(len(list2)):
    #     print(list2[i])
    dict_result = {}
    list3 = list()
    for _ in list2:
        for k, v in _.items():
            if k == 'code' or k == 'name' or k == 'firstGetTime':
                dict_result[k] = v
        # print(dict_result)
        # if dict_result['getTime'] != dict_result['firstGetTime']:
        list3.append(dict_result.copy())
 
    return list3
 
    # for i in range(len(list3)):
    #     print(list3[i])
 
def save_list(filepath,c_list):
 
    c_list = json.dumps(c_list)
    '''将c_list存入文件
    '''
    a = open(filepath, "w", encoding='UTF-8')
    a.write(c_list)
    a.close()
 
def read_list(filepath):
    '''读取data_source_list文件
    '''
    b = open(filepath, "r", encoding='UTF-8')
    out = b.read()
    out = json.loads(out)
    b.close()
    return out
 
def push_info(filepath,list_result2,web_hook2):
    appid = "wx112f057de987d19e"
    screct = "0c9af8144a9f98b2ece14e8a0918778d"
    #template_id = "Vos7ef7UiEXRXL6AfLsA83zbOD9Ehkd9nQ79OMLKuYg"
 
    last_list = read_list(filepath)
    push_list = list()
 
    print("list_result")
    for i in range(len(list_result)):
       print(list_result[i])
    
    try:
        print("last_list")
        for i in range(len(last_list)):
            print(last_list[i])
    except IOError:
       print("no result")
 
 
    if len(list_result) != len(last_list):
        # 数据数量不一致，直接推送
        for i in range(len(list_result)):
            #WechatMessagePush(appid, screct, template_id).send_wechat_temple_msg(list_result[i])
            push_report(list_result[i],web_hook)
        print("数据数量不一致，直接推送")
 
        for i in range(len(list_result)):
           print(list_result[i])
    else:
        # 数据数量一致，判断更新推送
        for i in range(len(list_result)):
            if list_result[i] != last_list[i]:
                push_list.append(list_result[i].copy())
 
        print("数据数量一致，判断更新推送")
 
        print("push_list")
        for i in range(len(push_list)):
           print(push_list[i])
 
        if len(push_list):
            for i in range(len(push_list)):
                #WechatMessagePush(appid, screct, template_id).send_wechat_temple_msg(push_list[i])
                push_report(push_list[i],web_hook)
        else:
            print("没有数据更新,不推送")
 
    save_list(filepath,list_result)
 
 
def push_report(push_dict2,web_hook2):
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msgtype": "text",
        "text": {
            "content":
                " •  code："+ push_dict['code'] +
                "                      "
                " •  name："+ push_dict['name'] +
                "                      "
                "https://m.10jqka.com.cn/stockpage/hs_"+push_dict['code'] +
                "                      "
                " •  firstGetTime："+ push_dict['firstGetTime']
        },
                "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    send_data = json.dumps(message_body)  # 将字典类型数据转化为json格式
    ChatBot = requests.post(url=web_hook, data=send_data, headers=header)
    opener = ChatBot.json()
    if opener["errmsg"] == "ok":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))
 
if __name__ == '__main__':
    filepath2 = "./data_source_list_2.txt"
    res2 = get_info2()
    list_result2 = parse_info(res2)
    webhook2 = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9b6a9289-c683-4f42-9a77-04c4384cf19e"
    push_info(filepath,list_result2,webhook3)
