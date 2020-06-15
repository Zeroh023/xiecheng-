
from urllib import request
import json
import xlwt
import time


def getResponse(url,i):

    data = {"hotelId": 8514712, "pageIndex": i, "tagId": 0, "pageSize": 10, "groupTypeBitMap": 2,
            "needStatisticInfo": 0, "order": 0, "basicRoomName": "", "travelType": -1,
            "head": {"cid": "09031093310029736463", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888",
                     "syscode": "09", "auth": "", "extension": []}
            }
    data = json.dumps(data).encode(encoding='utf-8')

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    url_request = request.Request(url=url, data=data, headers=header_dict)
    print("这个对象的方法是：", url_request.get_method())

    url_response = request.urlopen(url_request)
    #start_json = json.loads(url_response.read())
    #print(start_json)


    return url_response
def get_keyinfor(respose):
    fx = open('D:\携程酒店\评论5.txt', "a+",encoding='utf-8')

    data = respose.read().decode('utf-8')

    start_json = json.loads(data)  # 返回值转为字典型

    # print(json.dumps(start_json,ensure_ascii=False,indent=4))#格式化输出
    j = start_json["othersCommentList"]

    HotelName = start_json['tdk']
    name =HotelName['title']
    name =str(name)
    fx.write(name)
    f = xlwt.Workbook()
    '''
    sheet1 = f.add_sheet(name)
    sheet1.write(0, 0, "用户名称")
    sheet1.write(0, 1, "用户ID")
    sheet1.write(0, 2, "基本房型")
    sheet1.write(0, 3, "评论时间")
    sheet1.write(0, 4, "评论内容")
    f.save(r'D:\携程酒店\携程酒店评论.xls')
    row = 0'''





    for x in j:

        print(x["userNickName"])
        print(x['id'])
        print(x['baseRoomName'])
        print(x["postDate"])
        print(x['content'])


        fx.write((x['content']))
        fx.write(' \n')






if __name__ == '__main__':
    for i in range(1, 100):
        http_response = getResponse("https://m.ctrip.com/restapi/soa2/16765/gethotelcomment?&_fxpcqlniredt=09031093310029736463", i)
        time.sleep(3)
        get_keyinfor(http_response)

