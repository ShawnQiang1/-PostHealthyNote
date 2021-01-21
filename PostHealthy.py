# -*- encoding: utf-8 -*-
import urllib.request
from lxml import etree
import http.cookiejar
user="2019xxx"#你的学号
passwd="mima" #你的智慧东大密码
try:
        #定义UA标识
        header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                }
        #登录智慧东大的url
        url_login = "https://pass.neu.edu.cn/tpass/login"
        #创建储存cookie对象
        cookie = http.cookiejar.CookieJar()
        headler = urllib.request.HTTPCookieProcessor(cookie)
        opener =urllib.request.build_opener(headler)
        #获取登录智慧东大时所需流水号，创建正确的提交表单
        first_get=opener.open(url_login)
        first_get_text=first_get.read().decode("utf-8")
        tree = etree.HTML(first_get_text)
        lt_value=tree.xpath('//*[@id="lt"]/@value')[0]
        data={
                "rsa": user+passwd+lt_value,
                "ul": str(len(user)),
                "pl": str(len(passwd)),
                "lt": lt_value,
                "execution": 'e1s1',
                "_eventId": 'submit'
        }
        #将所需提交的表单（data）类型转换为bytes类型！！！
        postdata = urllib.parse.urlencode(data).encode("utf-8")
        #构造访问请求,此时保存cookie至opener
        request =urllib.request.Request(url_login,headers=header,data=postdata)
        upme=opener.open(request)


        #提交上报信息的url
        post_note_url="https://e-report.neu.edu.cn/api/notes"
        #填写上报信息的url
        note_page_url= "https://e-report.neu.edu.cn/notes/create"
        #获取本人姓名
        note_page_text=opener.open(note_page_url).read().decode("utf-8")
        tree2=etree.HTML(note_page_text)
        name=tree2.xpath("//*[@id='navbarDropdown']/text()")[0].split("：")[1]
        #获取_token
        _token = tree2.xpath("//*[@id='logout-form']/input/@value")[0]
        #创建提交健康信息表单
        note={
                '_token':_token,
                'jibenxinxi_shifoubenrenshangbao': "1",
                'profile[xuegonghao]': user,
                'profile[xingming]': name,
                'profile[suoshubanji]': "",
                'jiankangxinxi_muqianshentizhuangkuang': "正常",
                'xingchengxinxi_weizhishifouyoubianhua': "0",
                'cross_city': "无",
                'qitashixiang_qitaxuyaoshuomingdeshixiang': ""
        }
        #将所需提交的表单（note）类型转换为bytes类型！！！
        post_note=urllib.parse.urlencode(note).encode("utf-8")
        #提交健康信息表单
        note_request= urllib.request.Request(post_note_url,data=post_note)
        up_note=opener.open(note_request)
        print("上报成功！")
except:
        print("密码或者学号错误，上报失败！\n请检查自己学号密码是否已经修改正确！")