## 东北大学定时健康打卡爬虫程序  
学习python中一个练手的小程序
一开始是打算使用python中requests模块中的session方法来保存cookie进行模拟登录，
折腾了半天还是没法使用session方法保持登录状态，最后参考了一位大佬的爬虫，
使用了http中的cookiejar类来进行模拟登录
# 声明：
   本脚本只是为了忘记每日打卡而写，如果自身身体出现任何症状，还请如实手动上报症状，同时通知辅导员！
## 使用方法：
1.首先安装lxml http模块    
  pip install lxml  
  pip install http  
2.修改脚本中第五六行为自己账号参数  
  例： user="20191111"  
      passwd="wohaocai1125"  
3.执行脚本：python PostHealthy.py
