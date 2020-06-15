import re
import requests
import json
import time
import xlwt

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

postUrl = "https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031100212114028694"

urls = [
   # ['107540', '广州塔'],
   # ['6802', '长隆野生动物世界']
    #['4355', '乐山大佛']
    #['110282','峨眉山']
    #['4327','金顶']
    #['110342','灵秀温泉']
    #['107569', '嘉阳小火车']
    ['127819','金顶索道']
]
f = xlwt.Workbook()
sheet1 = f.add_sheet('携程景区评论')
sheet1.write(0, 0, "用户ID")
sheet1.write(0, 1, "景区名称")
sheet1.write(0, 2, "用户姓名")
sheet1.write(0, 3, "评论内容")
sheet1.write(0, 4, "评论时间")
f.save(r'E:\XieCheng_try\携程景区评论_嘉阳小火车.xls')

row = 0
for data in urls:

    data_1 = {
        "pageid": "10650000804",
        "viewid": data[0],
        "tagid": "0",
        "pagenum": "1",
        "pagesize": "50",
        "contentType": "json",
        "SortType": "1",
        "head": {
            "appid": "100013776",
            "cid": "09031100212114028694",
            "ctok": "",
            "cver": "1.0",
            "lang": "01",
            "sid": "8888",
            "syscode": "09",
            "auth": "",
            "extension": [
                {
                    "name": "protocal",
                    "value": "https"
                }
            ]
        },
        "ver": "7.10.3.0319180000"
    }

    html = requests.post(postUrl, data=json.dumps(data_1)).text
    html = json.loads(html)
    jingqu = data[1]
    # comments = html['data']['comments']
    pages = html['data']['totalpage']
    datas = []
    for j in range(pages):
        data1 = {
            "pageid": "10650000804",
            "viewid": data[0],
            "tagid": "0",
            "pagenum": str(j + 1),
            "pagesize": "50",
            "contentType": "json",
            "SortType": "1",
            "head": {
                "appid": "100013776",
                "cid": "09031100212114028694",
                "ctok": "",
                "cver": "1.0",
                "lang": "01",
                "sid": "8888",
                "syscode": "09",
                "auth": "",
                "extension": [
                    {
                        "name": "protocal",
                        "value": "https"
                    }
                ]
            },
            "ver": "7.10.3.0319180000"
        }
        datas.append(data1)

    for k in datas:
        print('正在抓取第' + k['pagenum'] + "页")
        time.sleep(3)
        html1 = requests.post(postUrl, data=json.dumps(k)).text
        html1 = json.loads(html1)
        comments = html1['data']['comments']

        for i in comments:
            ID = i['id']
            name = i['uid']
            content = i['content']
            content = re.sub("&#x20;", "", content)
            time1 = i['date']
            print("用户ID：",ID,"景区名称：", jingqu,"用户姓名：", name,"评论内容:", content,"评论时间：", time1)

            row= row +1
            sheet1.write(row, 0, ID)
            sheet1.write(row, 1, jingqu)
            sheet1.write(row, 2, name)
            sheet1.write(row, 3, content)
            sheet1.write(row, 4, time1)
            f.save(r'E:\XieCheng_try\携程景区评论_嘉阳小火车.xls')