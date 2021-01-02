import socket
import threading
import json  # json.dumps(some)打包   json.loads(some)解包
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包
import time
import requests
from tkinter import filedialog
import vachat
import os
from time import sleep
from PIL import ImageGrab
from robot import Tencent_AI_Chat_Robot
from netifaces import interfaces, ifaddresses, AF_INET6
## 数据库模块
import pymysql
# 查表操作
def check(name):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "passwd123", "qq")
    cursor = db.cursor()
    # name
    name = "'"+name+"'"
    # SQL 查询语句
    sql = "SELECT * FROM user WHERE user = " + name
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 判断是否存在信息
        if len(results) == 0:
            # print("No Messages")
            db.close()
            return None
        else:
            msg = {}
            for rst in results:
                msg['user'] = rst[1]
                msg['passwd'] = rst[2]
            db.close()
            return msg
        #关闭连接
    except:
        print("Error: unable to fetch data")
        # 关闭连接
        db.close()
        return None

# 添加表操作
def add(msg):
    user = msg['user']
    passwd = msg['passwd']
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "passwd123", "qq")
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO user(user, passwd) VALUES ('%s','%s')" % (user,passwd)
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交数据
        db.commit()
        #关闭连接
        db.close()
        return True
    except:
        #回滚数据
        db.rollback()
        # 关闭连接
        db.close()
        return None

#初始化信息
IP = ''
PORT = ''
user = ''
listbox1 = ''  # 用于显示在线用户的列表框
ii = 1  # 用于判断是开还是关闭列表框
fi = 1  # 用于判断是开还是关闭文件下载框
li = 1  # 用于判断是开还是关闭日志文件框
users = []  # 在线用户列表
chat = '------Group chat-------'  # 聊天对象, 默认为群聊
# 登陆窗口
root1 = tkinter.Tk()
root1.title('Log in')
root1.iconbitmap('./images/qq.ico')
root1['height'] = 400
root1['width'] = 275
screenWidth = root1.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = root1.winfo_screenheight()  # 获取显示区域的高度
left = (screenWidth - root1['width']) / 2
top = (screenHeight - root1['height']) / 2
root1.geometry("%dx%d+%d+%d" % (root1['width'], root1['height'], left, top))
root1.configure(bg='#a9eedb')
root1.resizable(0, 0)  # 限制窗口大小

IP1 = tkinter.StringVar()
IP1.set('127.0.0.1:8080')  # 默认显示的ip和端口
User = tkinter.StringVar()
User.set('jluzh')
Passwd = tkinter.StringVar()
Passwd.set('jluzh')

# 顶部LOGO
img_png = tkinter.PhotoImage(file = './images/jluzh.png')
label_img = tkinter.Label(root1, image = img_png,bg='#a2d8db')
label_img.place(x=0,y=0,width=275,height=232)

# 服务器标签
labelIP = tkinter.Label(root1, text='Server',bg='#AFEEEE',relief="ridge")
labelIP.place(x=30, y=250, width=80, height=20)

entryIP = tkinter.Entry(root1, width=80, textvariable=IP1)
entryIP.place(x=120, y=250, width=130, height=20)

# 用户名标签
labelUser = tkinter.Label(root1, text='Username',bg='#AFEEEE',relief="ridge")
labelUser.place(x=30, y=280, width=80, height=20)

entryUser = tkinter.Entry(root1, width=80, textvariable=User)
entryUser.place(x=120, y=280, width=130, height=20)

# 密码标签
labelPasswd = tkinter.Label(root1, text='Passwd',bg='#AFEEEE',relief="ridge")
labelPasswd.place(x=30,y=310,width=80,height=20)
entryPasswd = tkinter.Entry(root1, width=80, show='*' ,textvariable=Passwd)
entryPasswd.place(x=120, y=310, width=130, height=20)
# 登录按钮
def login(*args):
    global IP, PORT, user
    IP, PORT = entryIP.get().split(':')  # 获取IP和端口号
    PORT = int(PORT)                     # 端口号需要为int类型
    user1 = entryUser.get()
    passwd = entryPasswd.get()
    msg = check(user1)
    if msg is None:
        tkinter.messagebox.showerror('Name type error', message="Check your user")
    elif msg['user'] == user1 and msg['passwd'] == passwd:
        user = msg['user']
        root1.destroy()
    else:
        tkinter.messagebox.showerror('Name type error', message='Check your password')


# 注册按钮
def register(*args):
    # 注册窗口
    root2 = tkinter.Tk()
    root2.title('Register')
    root2.configure(bg='#a9eedb')
    root2['height'] = 140
    root2['width'] = 270
    screenWidth = root2.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = root2.winfo_screenheight()  # 获取显示区域的高度
    left = (screenWidth - root2['width']) / 2
    top = (screenHeight - root2['height']) / 2
    root2.geometry("%dx%d+%d+%d" % (root2['width'], root2['height'], left, top))
    root2.resizable(0, 0)  # 限制窗口大小
    User = tkinter.StringVar()
    Passwd = tkinter.StringVar()
    # 用户名标签
    labelUser = tkinter.Label(root2, text='Username',bg='#AFEEEE',relief="ridge")
    labelUser.place(x=30, y=40, width=80, height=20)
    NewUser = tkinter.Entry(root2, width=80, textvariable=User)
    NewUser.place(x=120, y=40, width=130, height=20)

    # 密码标签
    labelPasswd = tkinter.Label(root2, text='Passwd',bg='#AFEEEE',relief="ridge")
    labelPasswd.place(x=30, y=70, width=80, height=20)
    NewPasswd = tkinter.Entry(root2, width=80, show='*',textvariable=Passwd)
    NewPasswd.place(x=120, y=70, width=130, height=20)

    def submit(*args):
        newuser = NewUser.get()
        password = NewPasswd.get()
        msg = {}
        msg['user'] = newuser
        msg['passwd'] = password
        add(msg)
        root2.destroy()
    # 按钮提交
    but = tkinter.Button(root2, text='Submit', command=submit,bg='#AFEEEE',relief="solid")
    but.place(x=100, y=100, width=70, height=30)

root1.bind('<Return>', login)            # 回车绑定登录功能
but = tkinter.Button(root1, text='Login', command=login,bg='#AFEEEE',relief="solid")
but.place(x=140, y=340, width=70, height=25)


regsi_but = tkinter.Button(root1, text='Register', command=register,bg='#AFEEEE',relief="solid")
regsi_but.place(x=60, y=340, width=70, height=25)


root1.mainloop()

#建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
if user:
    s.send(user.encode())  # 发送用户名
else:
    s.send('no'.encode())  # 没有输入用户名则标记no

# 如果没有用户名则将ip和端口号设置为用户名
addr = s.getsockname()  # 获取客户端ip和端口号
addr = addr[0] + ':' + str(addr[1])
if user == '':
    user = addr

# 聊天窗口
# 创建图形界面
root = tkinter.Tk()
root.title(user)  # 窗口命名为用户名
root.configure(bg='#a9eedb')
root['width'] = 580
root['height'] = 490
root.iconbitmap('./images/qq.ico')

def update_clock():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    timelabel.configure(text=now)
    root.after(1000, update_clock)
# 创建时间标签
timelabel = tkinter.Label(text='')
timelabel.configure(bg='#a9eedb')
update_clock()
timelabel.place(x=245,y=0,width=120,height=20)
# 创建通知标签
# versionlabel = tkinter.Label(text='-------------------------通知---------------------------')
# versionlabel.configure(bg='black')
# versionlabel.place(x=5,y=0,width=240,height=20)
# bt1 5 0 60 20
# bt2 65 0 60 20
# bt3 125 0 60 20
# bt4 185 0 60 20
from tkinter import ttk
# 创建功能按钮
def extend1():
    print('1')
# extendbutton1 = ttk.Combobox(root, text='settings', command=extend1,bg='#AFEEEE',relief="solid")
# title1 = ttk.Combobox(root,text='settings') 这是一个下拉菜单
# title1['value'] = ('1','2','3','4')
# title1.place(x=5,y=0,width=60,height=20)
menubar = tkinter.Menu(root)#创建菜单
menubar.configure(bg='#a9eedb')
root.config(menu=menubar)

def Preference():
    global root
    def CallColor():
        import tkinter.colorchooser as cc
        global list2,listbox1
        Color = cc.askcolor()[1]
        root.configure(bg=Color)
        listbox.configure(bg=Color)
        entry.configure(bg=Color)
        timelabel.configure(bg=Color)
        eBut.configure(bg=Color)
        pBut.configure(bg=Color)
        sBut.configure(bg=Color)
        fBut.configure(bg=Color)# 文件管理
        list2.configure(bg=Color)

        button1.configure(bg=Color)# 用户列表
        listbox1.configure(bg=Color)

        button2.configure(bg=Color)# 聊天记录


        button.configure(bg=Color)
        vbutton.configure(bg=Color)

    chice = tkinter.Tk()
    chice.title('Preference')
    chice['width']=200
    chice['height']=100
    # background color
    bgLabel = tkinter.Label(chice, text="background")
    bgLabel.place(x=0,y=0,width=80,height=20)
    bgChoose = tkinter.Button(chice, text=' ',command=CallColor)
    bgChoose.place(x=80,y=0,width=40,height=20)

    chice.mainloop()

def Logout():
    root.destroy()

def Detail():
    lines = ['Version: 8.6', 'CvVersion: 4.1.2.30', 'Author: ayjin','Time: 2020-12-24']
    tkinter.messagebox.showinfo('Detail', "\n".join(lines))
menu1 = tkinter.Menu(menubar,tearoff=0)
menu1.add_command(label='Preference',command=Preference)
menu1.add_command(label='Logout',command=Logout)
menu1.add_command(label='Version',command=Detail)
menubar.add_cascade(label='Settings',menu=menu1)

def Spider():
    Spidertk = tkinter.Tk()
    Spidertk.title('Covid Data Spider')
    Spidertk['width'] = 360
    Spidertk['height'] = 175
    Spidertk.configure(bg='#a9eedb')
    # 查表
    import pandas as pd
    file = './data.csv'
    #spider data
    def update():
        import re
        url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        response = requests.get(url)
        response.encoding='utf-8'
        pattern = r'window.getAreaStat = ([\s\S]*?)</script>'
        data_list = re.findall(pattern, response.text)
        data = eval(data_list[0].replace('}catch(e){}',''))
        china_list = []
        for i in range(len(data)):
            province = data[i]['provinceName']
            city_list = data[i]['cities']
            for j in range(len(city_list)):
                cityName = city_list[j]['cityName'] # 城市名
                currentConfirmedCount = city_list[j]['currentConfirmedCount'] # 现存确诊
                confirmedCount = city_list[j]['confirmedCount'] # 累计确诊
                curedCount = city_list[j]['curedCount'] # 治愈
                deadCount = city_list[j]['deadCount'] # 死亡
                china_dict = {}
                china_dict['province'] = province
                china_dict['city'] = cityName
                china_dict['currentConfirmedCount'] = currentConfirmedCount
                china_dict['confirmedCount'] = confirmedCount
                china_dict['curedCount']=curedCount
                china_dict['deadCount'] = deadCount
                china_list.append(china_dict)
        china_data = pd.DataFrame(china_list)
        china_data.to_csv('data.csv',index=False,encoding='utf_8_sig')
        tkinter.messagebox.showinfo('提示', '数据已更新至data.csv文件')
    def getdata():
        update()
        DataLabel.configure(text='Update',bg='green')
    # Get Data
    dataButton = tkinter.Button(Spidertk,text='GetData',command=getdata,bg='#AFEEEE',relief="solid")
    dataButton.place(x=150,y=0,width=70,height=25)
    # 服务器标签
    StatusLabel = tkinter.Label(Spidertk, text='Status', bg='#AFEEEE', relief="ridge")
    StatusLabel.place(x=80, y=25, width=70, height=20)
    # 状态标签
    DataLabel = tkinter.Label(Spidertk, text='UnUpgrade', bg='red', relief="ridge")
    DataLabel.place(x=150, y=25, width=70, height=20)
    # 省份标签
    ProvinceLabel = tkinter.Label(Spidertk, text='Province', bg='#AFEEEE', relief="ridge")
    ProvinceLabel.place(x=80, y=45, width=70, height=20)
    # 省份输入框
    province = tkinter.StringVar()
    ProvinceEntry = tkinter.Entry(Spidertk, width=80, textvariable=province)
    ProvinceEntry.place(x=150, y=45, width=130, height=20)
    # 市级标签
    city = tkinter.StringVar()
    CityLabel = tkinter.Label(Spidertk, text='City', bg='#AFEEEE', relief="ridge")
    CityLabel.place(x=80, y=65, width=70, height=20)
    # 市级输入框
    CityEntry = tkinter.Entry(Spidertk, width=80, textvariable=city)
    CityEntry.place(x=150, y=65, width=130, height=20)
    # 查询按钮
    def CheckData():
        data = pd.io.parsers.read_csv(file)
        # print(data[data['province']==ProvinceEntry.get()])
        # print(data[data['city']==CityEntry.get()])
        msg = data[data['province'] == ProvinceEntry.get()]
        print(len(msg.values))
        msg2 = data[data['city'] == CityEntry.get()]
        print(len(msg2.values))
        rstList = []
        # 如果两个输入框都为空
        if len(msg.values) == 0 and len(msg2.values) == 0 :
            data = data.values
        elif len(msg.values) != 0:
            data = msg.values
        elif len(msg2.values) != 0:
            data = msg2.values
        for i in range(len(data)):
            tmp = {}
            tmp['province'] = data[i][0]
            tmp['city'] = data[i][1]
            tmp['currentConfirmedCount'] = data[i][2]
            tmp['confirmedCount'] = data[i][3]
            tmp['curedCount'] = data[i][4]
            tmp['deadCount'] = data[i][5]
            rstList.append(tmp)
        print(rstList)
        showWindows = tkinter.Tk()
        showWindows.title('查询结果')
        tree = ttk.Treeview(showWindows, columns=['1', '2', '3','4','5','6'], show='headings')
        tree.column('1', width=100, anchor='center')
        tree.column('2', width=80, anchor='center')
        tree.column('3', width=80, anchor='center')
        tree.column('4', width=80, anchor='center')
        tree.column('5', width=80, anchor='center')
        tree.column('6', width=80, anchor='center')
        tree.heading('1', text='省份')
        tree.heading('2', text='城市')
        tree.heading('3', text='当前确诊人数')
        tree.heading('4', text='共确诊人数')
        tree.heading('5', text='治愈人数')
        tree.heading('6', text='死亡人数')
        for rst in rstList:
            li = []
            li.append(rst['province'])
            li.append(rst['city'])
            li.append(rst['currentConfirmedCount'])
            li.append(rst['confirmedCount'])
            li.append(rst['curedCount'])
            li.append(rst['deadCount'])
            tree.insert('', 'end', values=li)
        tree.grid()
        VScroll1 = tkinter.Scrollbar(tree, orient='vertical', command=tree.yview)
        VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=VScroll1.set)
        root.mainloop()
        # tkinter.messagebox.showinfo('提示', data[data['province']==ProvinceEntry.get()])
    CheckButton = tkinter.Button(Spidertk,text='Check',command=CheckData,bg='#AFEEEE',relief="solid")
    CheckButton.place(x=150,y=130,width=70,height=20)
    Spidertk.mainloop()

def Jluzh():
    print('Weibo')
    StudentTk = tkinter.Tk()
    StudentTk.title('Jluzh Login')
    StudentTk['width'] = 360
    StudentTk['height'] = 200
    StudentTk.configure(bg='#a9eedb')
    # 学号标签
    AccountLabel = tkinter.Label(StudentTk, text='学号', bg='#AFEEEE', relief="ridge")
    AccountLabel.place(x=80, y=45, width=70, height=20)
    # 学号输入框
    account = tkinter.StringVar()
    AccountEntry = tkinter.Entry(StudentTk, width=80, textvariable=account)
    AccountEntry.place(x=150, y=45, width=130, height=20)
    # 密码标签
    password = tkinter.StringVar()
    PasswordLabel = tkinter.Label(StudentTk, text='密码', bg='#AFEEEE', relief="ridge")
    PasswordLabel.place(x=80, y=65, width=70, height=20)
    # 密码输入框
    PasswordEntry = tkinter.Entry(StudentTk, width=80, textvariable=password,show='*')
    PasswordEntry.place(x=150, y=65, width=130, height=20)
    def login(status):
        from selenium import webdriver
        import time
        if status == 0:
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome = webdriver.Chrome(chrome_options=chrome_options)
        else:
            chrome = webdriver.Chrome()
        url = 'http://wlkc.jluzh.edu.cn/meol/index.do'
        chrome.get(url)
        chrome.find_element_by_xpath("//div[@class='register login_button']").click()
        time.sleep(0.5)
        ac = AccountEntry.get()
        pd = PasswordEntry.get()
        chrome.find_element_by_xpath("//input[@id='userName']").send_keys(ac)
        chrome.find_element_by_xpath("//input[@id='passWord']").send_keys(pd)
        time.sleep(0.5)
        chrome.find_element_by_xpath("//input[@class='submit']").click()
        time.sleep(3)
        reminder = chrome.find_elements_by_xpath("//div[@class='reminderwrap']//ul[@id='reminder']/li")
        # print(len(reminder))
        userinfo = chrome.find_elements_by_xpath("//div[@class='userinfobody']//li")
        user = []
        for s in userinfo:
            if len(s.text) != 0:
                user.append(s.text)
        msg = {}
        for lis in reminder:
            try:
                title = lis.find_element_by_xpath(".//a")
                # print(title.text)
                title.click()
                time.sleep(0.5)
                names = lis.find_elements_by_xpath(".//ul[@style='display: block;']//li/a")
                content = []
                for name in names:
                    # print(name.text)
                    content.append(name.text)
                msg[title.text] = content
            except Exception as e:
                print(e)
        print(msg)
        if status == 0:
            StudentTk['height'] = 360
            # 姓名标签
            NameLabel = tkinter.Label(StudentTk, text=user[0], bg='#AFEEEE', relief="ridge")
            NameLabel.place(x=130, y=105, width=70, height=20)
            # 登陆时间标签
            LoginLabel = tkinter.Label(StudentTk, text=user[1], bg='#AFEEEE', relief="ridge")
            LoginLabel.place(x=80, y=125, width=170, height=20)
            # 总时长标签
            TimeLabel = tkinter.Label(StudentTk, text=user[2], bg='#AFEEEE', relief="ridge")
            TimeLabel.place(x=80, y=145, width=170, height=20)
            # 次数标签
            SumLabel = tkinter.Label(StudentTk, text=user[3], bg='#AFEEEE', relief="ridge")
            SumLabel.place(x=80, y=165, width=170, height=20)
            print(msg.keys())
            tree = ttk.Treeview(StudentTk, columns=['1'], show='headings')
            tree.column('1', width=170, anchor='center')
            tree.heading('1', text='查询信息')
            for rst in msg.keys():
                print(rst)
                li = []
                li.append(rst)
                tree.insert('', 'end', values=li)
            tree.place(x=80,y=185,width=170,height=110)

    # No windows login
    CmdButton = tkinter.Button(StudentTk, text='无窗口查询', command=lambda:login(0),bg='#AFEEEE',relief="solid")
    CmdButton.place(x=100,y=85,width=70,height=20)
    # login
    WebButton = tkinter.Button(StudentTk, text='网页查询', command=lambda:login(1),bg='#AFEEEE',relief="solid")
    WebButton.place(x=170,y=85,width=70,height=20)
    StudentTk.mainloop()



import glob
import pygame
realpath = os.path.realpath(__file__) #当前绝对路径
dirname = os.path.dirname(realpath) + '\music\\'
# print(dirname)
extension = '*.mp3'
file_list = glob.glob(dirname+extension) #返回一个列表
# print(file_list)
aulist = [] # 定义歌曲路径列表
aulist.extend(file_list)
musicname = []
for file in file_list:
    musicname.append(file.split("\\")[-1])
hit_it = False
flag = False
count = 40
def music():
    window = tkinter.Tk()
    window.title("MP3")
    window['width']=210
    window['height']=500
    window.attributes("-alpha",0.91)
    window.iconbitmap("./images/qq.ico")
    #播放主功能函数
    def replay():
        #初始化
        pygame.mixer.init()
        # 文件加载
        global count
        global flag
        if len(aulist) == 0:
            flag = True
        if flag == False:
            flag = True
            # 播放  第一个是播放值 -1代表当前单曲循环播放，第二个参数代表开始播放的时间
            pygame.mixer.music.load(aulist[count])
            pygame.mixer.music.play(-1, 0.3)
            print("正在播放：", aulist[count])
        else:
            flag = False
            pygame.mixer.music.pause()
    #上一首
    def last_one():
        print('上一首')
        global count
        global flag
        if count != 0:
            count -= 1
            flag = False
            replay()
        else:
            flag = False
            count = len(aulist) - 1
            replay()
    #下一首
    def next_one():
        print('下一首')
        global count
        global flag
        if count != len(aulist) - 1:
            count += 1
            flag = False
            replay()
        else:
            flag = False
            count = 0
            replay()
    #暂停
    def pause():
        global hit_it
        if hit_it == False:
            hit_it = True
            pygame.mixer.music.pause()
        else:
            hit_it = False
            pygame.mixer.music.unpause()
    #播放列表所选歌曲
    def chooseMusic():
        global count
        id = musiclist.curselection()[0]
        count = id
        replay()
        print(id)
        print(musiclist.get(id))
    #是否要更新
    def IsUpdate():
        import tkinter.messagebox
        a = tkinter.messagebox.askokcancel('提示','确定要更新曲库吗？')
        if a:
            print('爬虫')
            import requests
            from lxml import etree
            # url = "https://music.163.com/song/media/outer/url?id=1806584346.mp3"
            # headers = {
            #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            # }
            # rep = requests.get(url,headers=headers)
            # with open('test4.mp3','wb') as fp:
            #     fp.write(rep.content)
            url = 'https://music.163.com/discover/toplist'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
            rep = requests.get(url, headers=headers)
            # print(rep.text)
            # rep = etree.HTML(rep.text)
            rep.encoding = 'utf-8'
            root = etree.HTML(rep.content)
            links = root.xpath("//ul[@class='f-hide']//li//a/@href")
            names = root.xpath("//ul[@class='f-hide']//li//a/text()")
            # print(links[0])# /song?id=1806584346
            # print(len(links))
            # print(len(names))
            msglist = []
            for i in range(0, 100):
                music = {}
                music['id'] = links[i].split('=')[1]
                music['name'] = names[i]
                msglist.append(music)

            for music in msglist:
                url = "https://music.163.com/song/media/outer/url?id=" + music["id"] + ".mp3"
                path = "./music/" + music["name"] + '.mp3'
                rep = requests.get(url, headers=headers)
                with open(path, 'wb') as fp:
                    fp.write(rep.content)
                print(music)


    #控件布局
    btn1 = tkinter.Button(window, text="播放",height=1, width=3, bg="#66CCFF", command = replay)
    btn1.place(x=45,y=400)
    btn2 = tkinter.Button(window, text="上一首",height=1, width=4, bg="#33CCFF", command = last_one)
    btn2.place(x=0,y=400)
    btn3 = tkinter.Button(window, text="下一首",height=1, width=4, bg="#00CCFF", command = next_one)
    btn3.place(x=80,y=400)
    btn4 = tkinter.Button(window, text="暂停",  height=1, width=3, bg="#00CCFF", command = pause)
    btn4.place(x=120,y=400)
    btn9 = tkinter.Button(window, text="刷新曲库", height=1, width=6, bg="#CCCCFF", command =IsUpdate)
    btn9.place(x=37,y=430)
    btn10 = tkinter.Button(window, text="播放选中", height=1, width=6, bg="#CCCCFF", command =chooseMusic)
    btn10.place(x=142,y=430)

    musiclist = tkinter.Listbox(window)
    musiclist.place(x=0,y=0,width=200,height=400)
    for name in musicname:
        musiclist.insert(tkinter.END,name)
    yscrollbar = tkinter.Scrollbar(musiclist, command=musiclist.yview)
    yscrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    musiclist.config(yscrollcommand=yscrollbar.set)
    window.mainloop()
menu2 = tkinter.Menu(menubar,tearoff=0)
menu2.add_command(label='CovidData',command=Spider)
menu2.add_command(label='Jluzh',command=Jluzh)
menu2.add_command(label='Music',command=music)
menubar.add_cascade(label='Extensions',menu=menu2)


def Help():
    tkinter.messagebox.showinfo('Help','The document link: https://github.com/ay1Jin')
menu3 = tkinter.Menu(menubar,tearoff=0)
menu3.add_command(label='Help',command=Help)
menubar.add_cascade(label='Help',menu=menu3)
# extendbutton1.place(x=5,y=0,width=60,height=20)
#
# def extend2():
#     print('2')
# extendbutton2 = tkinter.Button(root, text='bt2', command=extend2,bg='#AFEEEE',relief="solid")
# extendbutton2.place(x=65,y=0,width=60,height=20)
#
# def extend3():
#     print('3')
# extendbutton3 = tkinter.Button(root, text='extensions', command=extend3,bg='#AFEEEE',relief="solid")
# extendbutton3.place(x=125,y=0,width=60,height=20)
#
# def extend4():
#     print('4')
# extendbutton4 = tkinter.Button(root, text='versions', command=extend4,bg='#AFEEEE',relief="solid")
# extendbutton4.place(x=185,y=0,width=60,height=20)

# 创建多行文本框
listbox = ScrolledText(root)
listbox.configure(bg='#a9eedb',relief="solid")
listbox.place(x=5, y=20, width=570, height=300)
# 文本框使用的字体颜色
listbox.tag_config('red', foreground='red')
listbox.tag_config('blue', foreground='blue')
listbox.tag_config('green', foreground='green')
listbox.tag_config('pink', foreground='pink')
listbox.insert(tkinter.END, 'Welcome to the chat room!', 'blue')


# 表情功能代码部分
# 四个按钮, 使用全局变量, 方便创建和销毁
b1 = ''
b2 = ''
b3 = ''
b4 = ''
# 将图片打开存入变量中
p1 = tkinter.PhotoImage(file='./emoji/facepalm.png')
p2 = tkinter.PhotoImage(file='./emoji/smirk.png')
p3 = tkinter.PhotoImage(file='./emoji/concerned.png')
p4 = tkinter.PhotoImage(file='./emoji/smart.png')
# 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
dic = {'aa**': p1, 'bb**': p2, 'cc**': p3, 'dd**': p4}
ee = 0  # 判断表情面板开关的标志


# 发送表情图标记的函数, 在按钮点击事件中调用


def mark(exp):  # 参数是发的表情图标记, 发送后将按钮销毁
    global ee
    mes = exp + ':;' + user + ':;' + chat
    s.send(mes.encode())
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    ee = 0


# 四个对应的函数
def bb1():
    mark('aa**')


def bb2():
    mark('bb**')


def bb3():
    mark('cc**')


def bb4():
    mark('dd**')


def express():
    global b1, b2, b3, b4, ee
    if ee == 0:
        ee = 1
        b1 = tkinter.Button(root, command=bb1, image=p1,
                            relief=tkinter.FLAT, bd=0)
        b2 = tkinter.Button(root, command=bb2, image=p2,
                            relief=tkinter.FLAT, bd=0)
        b3 = tkinter.Button(root, command=bb3, image=p3,
                            relief=tkinter.FLAT, bd=0)
        b4 = tkinter.Button(root, command=bb4, image=p4,
                            relief=tkinter.FLAT, bd=0)

        b1.place(x=5, y=248)
        b2.place(x=75, y=248)
        b3.place(x=145, y=248)
        b4.place(x=215, y=248)
    else:
        ee = 0
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()


# 创建表情按钮
eBut = tkinter.Button(root, text='emoji', command=express,bg='#AFEEEE',relief="solid")
eBut.place(x=5, y=320, width=60, height=30)


# 图片功能代码部分
# 从图片服务端的缓存文件夹中下载图片到客户端缓存文件夹中
def fileGet(name):
    PORT3 = 8082
    ss2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss2.connect((IP, PORT3))
    message = 'get ' + name
    ss2.send(message.encode())
    fileName = './Client_image_cache/' + name
    print('Start downloading image!')
    print('Waiting.......')
    with open(fileName, 'wb') as f:
        while True:
            data = ss2.recv(1024)
            if data == 'EOF'.encode():
                print('Download completed!')
                break
            f.write(data)
    time.sleep(0.1)
    ss2.send('quit'.encode())
    # img = Image.open(fileName)
    # plt.figure('picture')
    # plt.imshow(img)
    # plt.show()


# 将图片上传到图片服务端的缓存文件夹中
def filePut(fileName):
    PORT3 = 8082
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(IP)
    ss.connect((IP, PORT3))
    # 截取文件名
    print(fileName)
    name = fileName.split('/')[-1]
    print(name)
    message = 'put ' + name
    ss.send(message.encode())
    time.sleep(0.1)
    print('Start uploading image!')
    print('Waiting.......')
    with open(fileName, 'rb') as f:
        while True:
            a = f.read(1024)
            if not a:
                break
            ss.send(a)
        time.sleep(0.1)  # 延时确保文件发送完整
        ss.send('EOF'.encode())
        print('Upload completed')
    ss.send('quit'.encode())
    time.sleep(0.1)
    # 上传成功后发一个信息给所有客户端
    mes = '``#' + name + ':;' + user + ':;' + chat
    s.send(mes.encode())
    # img = Image.open(fileName)
    # img.show()


def picture():
    # 选择对话框
    fileName = tkinter.filedialog.askopenfilename(title='Select upload image')
    # 如果有选择文件才继续执行
    if fileName:
        # 调用发送图片函数
        print('开始上传')
        filePut(fileName)


# 创建发送图片按钮
pBut = tkinter.Button(root, text='Image', command=picture,bg='#AFEEEE',relief="solid")
pBut.place(x=65, y=320, width=60, height=30)


# 截屏函数如下所示
class MyCapture:
    def __init__(self, png):
        # 变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        # 屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        # 创建顶级组件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        # 不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top, bg='white', width=screenWidth, height=screenHeight)
        # 显示全屏截图，在全屏截图上进行区域截图
        self.image = tkinter.PhotoImage(file=png)
        self.canvas.create_image(screenWidth / 2, screenHeight / 2, image=self.image)
        self.sel = None

        # 鼠标左键按下的位置

        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            # 开始截图
            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)

        # 鼠标左键移动，显示选取的区域
        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                # 删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
                self.canvas.delete(lastDraw)
            except Exception as e:
                print(e)
            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

        self.canvas.bind('<B1-Motion>', onLeftButtonMove)

        # 获取鼠标左键抬起的位置，保存区域截图
        def onLeftButtonUp(event):
            self.sel = False
            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                print(e)
            sleep(0.1)
            # 考虑鼠标左键从右下方按下而从左上方抬起的截图
            left, right = sorted([self.X.get(), event.x])
            top, bottom = sorted([self.Y.get(), event.y])
            pic = ImageGrab.grab((left + 1, top + 1, right, bottom))
            # 弹出保存截图对话框
            fileName = tkinter.filedialog.asksaveasfilename(title='Save screenshot',
                                                            filetypes=[('image', '*.jpg *.png')])
            fileName = fileName+'.png'
            if fileName:
                pic.save(fileName)
            # 关闭当前窗口
            self.top.destroy()

        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        # 让canvas充满窗口，并随窗口自动适应大小
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


# 开始截图
def buttonCaptureClick():
    # 最小化主窗口
    root.state('icon')
    sleep(0.2)
    filename = 'temp.png'
    # grab()方法默认对全屏幕进行截图
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    # 显示全屏幕截图
    w = MyCapture(filename)
    sBut.wait_window(w.top)
    # 截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    root.state('normal')
    os.remove(filename)


# 创建截屏按钮
sBut = tkinter.Button(root, text='Capture', command=buttonCaptureClick,bg='#AFEEEE',relief="solid")
sBut.place(x=125, y=320, width=60, height=30)

# 文件功能代码部分
# 将在文件功能窗口用到的组件名都列出来, 方便重新打开时会对面板进行更新
list2 = ''  # 列表框
label = ''  # 显示路径的标签
upload = ''  # 上传按钮
close = ''  # 关闭按钮


def fileClient():
    PORT2 = 8081  # 聊天室的端口为8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT2))

    # 修改root窗口大小显示文件管理的组件
    root['width'] = 800
    root['height'] = 470

    # 创建列表框
    list2 = tkinter.Listbox(root)
    list2.place(x=580, y=25, width=200, height=350)

    # 将接收到的目录文件列表打印出来(dir), 显示在列表框中, 在pwd函数中调用
    def recvList(enter, lu):
        s.send(enter.encode())
        data = s.recv(4096)
        data = json.loads(data.decode())
        list2.delete(0, tkinter.END)  # 清空列表框
        lu = lu.split('\\')
        if len(lu) != 1:
            list2.insert(tkinter.END, 'Return to the previous dir')
            list2.itemconfig(0, fg='green')
        for i in range(len(data)):
            list2.insert(tkinter.END, ('' + data[i]))
            if '.' not in data[i]:
                list2.itemconfig(tkinter.END, fg='orange')
            else:
                list2.itemconfig(tkinter.END, fg='blue')

    # 创建标签显示服务端工作目录
    def lab():
        global label
        data = s.recv(1024)  # 接收目录
        lu = data.decode()
        try:
            label.destroy()
            label = tkinter.Label(root, text=lu)
            label.place(x=580, y=0, )
        except:
            label = tkinter.Label(root, text=lu)
            label.place(x=580, y=0, )
        recvList('dir', lu)

    # 进入指定目录(cd)
    def cd(message):
        s.send(message.encode())

    # 刚连接上服务端时进行一次面板刷新
    cd('cd same')
    lab()

    # 接收下载文件(get)
    def get(message):
        # print(message)
        name = message.split(' ')
        # print(name)
        name = name[1]  # 获取命令的第二个参数(文件名)
        # 选择对话框, 选择文件的保存路径
        fileName = tkinter.filedialog.asksaveasfilename(title='Save file to', initialfile=name)
        # 如果文件名非空才进行下载
        if fileName:
            s.send(message.encode())
            with open(fileName, 'wb') as f:
                while True:
                    data = s.recv(1024)
                    if data == 'EOF'.encode():
                        tkinter.messagebox.showinfo(title='Message',
                                                    message='Download completed!')
                        break
                    f.write(data)

    # 创建用于绑定在列表框上的函数
    def run(*args):
        indexs = list2.curselection()
        index = indexs[0]
        content = list2.get(index)
        # 如果有一个 . 则为文件
        if '.' in content:
            content = 'get ' + content
            get(content)
            cd('cd same')
        elif content == 'Return to the previous dir':
            content = 'cd ..'
            cd(content)
        else:
            content = 'cd ' + content
            cd(content)
        lab()  # 刷新显示页面

    # 在列表框上设置绑定事件
    list2.bind('<ButtonRelease-1>', run)

    # 上传客户端所在文件夹中指定的文件到服务端, 在函数中获取文件名, 不用传参数
    def put():
        # 选择对话框
        fileName = tkinter.filedialog.askopenfilename(title='Select upload file')
        # 如果有选择文件才继续执行
        if fileName:
            name = fileName.split('/')[-1]
            message = 'put ' + name
            s.send(message.encode())
            with open(fileName, 'rb') as f:
                while True:
                    a = f.read(1024)
                    if not a:
                        break
                    s.send(a)
                time.sleep(0.1)  # 延时确保文件发送完整
                s.send('EOF'.encode())
                tkinter.messagebox.showinfo(title='Message',
                                            message='Upload completed!')
        cd('cd same')
        lab()  # 上传成功后刷新显示页面

    # 创建上传按钮, 并绑定上传文件功能
    upload = tkinter.Button(root, text='Upload file', command=put)
    upload.place(x=600, y=380, height=30, width=80)

    # 关闭文件管理器, 待完善
    def closeFile():
        root['height'] = 470
        root['width'] = 580
        list2.destroy()
        upload.destroy()
        close.destroy()
        # 关闭连接
        s.send('quit'.encode())
        s.close()

    # 创建关闭按钮
    close = tkinter.Button(root, text='Close', command=closeFile)
    close.place(x=685, y=380, height=30, width=70)


# 创建文件按钮
fBut = tkinter.Button(root, text='File', command=fileClient,bg='#AFEEEE',relief="solid")
fBut.place(x=185, y=320, width=60, height=30)

# 创建多行文本框, 显示在线用户
listbox1 = tkinter.Listbox(root)
listbox1.configure(bg='#a9eedb',relief="solid")
listbox1.place(x=445, y=0, width=130, height=320)


def users():
    global listbox1, ii
    if ii == 1:
        root['width']=735
        listbox1.place(x=585, y=20, width=130, height=430)
        ii = 0
    else:
        listbox1.place_forget()  # 隐藏控件
        root['width']=585
        ii = 1


# 查看在线用户按钮
listbox1.place_forget()
button1 = tkinter.Button(root, text='Users online', command=users,bg='#AFEEEE',relief="solid")
button1.place(x=485, y=320, width=90, height=30)

# 查询日志操作
def checklogs(name):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "passwd123", "qq")
    cursor = db.cursor()
    # name
    name = "'"+name+"'"
    # SQL 查询语句
    sql = "SELECT * FROM logs WHERE user = " + name
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 判断是否存在信息
        if len(results) == 0:
            # print("No Messages")
            db.close()
            return None
        else:
            msglist = []
            for rst in results:
                msg = {}
                msg['user'] = rst[1]
                msg['reciver'] = rst[2]
                msg['message'] = rst[3]
                msg['time'] = rst[4].strftime("%Y/%m/%d %H:%M:%S")
                msglist.append(msg)
            db.close()
            return msglist
        #关闭连接
    except:
        print("Error: unable to fetch data")
        # 关闭连接
        db.close()
        return None


def showlogs():
    global li,list2
    # 关闭日志管理器, 待完善
    if li == 1:
        # 修改root窗口大小显示文件管理的组件
        root['height'] = 470
        root['width'] = 1200
        msglist = checklogs(user)
        # 创建列表框
        list2 = tkinter.Listbox(root)
        list2.place(x=580, y=25, width=600, height=325)
        title = '--------time-------' + '>>' +'-reciver--'+':message'
        list2.insert(tkinter.END, title)
        for msg in msglist:
            content = msg['time']+'>>'+msg['reciver']+':'+msg['message']
            list2.insert(tkinter.END,content)
        li = 0
    else:
        list2.place_forget()
        root['width']=580
        root['height']=470
        li = 1

# 查看聊天记录
button2 = tkinter.Button(root,text='user logs', command=showlogs,bg='#AFEEEE',relief="solid")
button2.place(x=300, y=320, width=90, height=30)



# 创建输入文本框和关联变量
a = tkinter.StringVar()
a.set('')
entry = tkinter.Entry(root, width=120, textvariable=a)
entry.configure(bg='#a9eedb',relief="solid")
entry.place(x=5, y=350, width=570, height=100)


def call_robot(url, apikey, msg):
    data = {
        "reqType": 0,
        "perception": {
            # 用户输入文文信息
            "inputText": {  # inputText文本信息
                "text": msg
            },
            # 用户输入图片url
            "inputImage": {  # 图片信息，后跟参数信息为url地址，string类型
                "url": "https://cn.bing.com/images/"
            },
            # 用户输入音频地址信息
            "inputMedia": {  # 音频信息，后跟参数信息为url地址，string类型
                "url": "https://www.1ting.com/"
            },
            # 客户端属性信息
            "selfInfo": {  # location 为selfInfo的参数信息，
                "location": {  # 地理位置信息
                    "city": "杭州",  # 所在城市，不允许为空
                    "province": "浙江省",  # 所在省份，允许为空
                    "street": "灵隐街道"  # 所在街道，允许为空
                }
            },
        },
        "userInfo": {
            "apiKey": "ee19328107fa41e987a42a064a68d0da",  # 你注册的apikey,机器人标识,32位
            "userId": "Brandon"  # 随便填，用户的唯一标识，长度小于等于32位
        }
    }
    headers = {'content-type': 'application/json'}  # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def send(*args):
    # 没有添加的话发送信息时会提示没有聊天对象
    users.append('------Group chat-------')
    users.append('Robot')
    print(chat)
    if chat not in users:
        tkinter.messagebox.showerror('Send error', message='There is nobody to talk to!')
        return
    if chat == 'Robot':
        print('Robot')
    if chat == user:
        tkinter.messagebox.showerror('Send error', message='Cannot talk with yourself in private!')
        return
    mes = entry.get() + ':;' + user + ':;' + chat  # 添加聊天对象标记
    s.send(mes.encode())
    a.set('')  # 发送后清空文本框


# 创建发送按钮
button = tkinter.Button(root, text='Send', command=send,bg='#AFEEEE',relief="solid")
button.place(x=515, y=380, width=60, height=30)
root.bind('<Return>', send)  # 绑定回车发送信息

# 视频聊天部分
IsOpen = False    # 判断视频/音频的服务器是否已打开
Resolution = 0    # 图像传输的分辨率 0-4依次递减
Version = 4       # 传输协议版本 IPv4/IPv6
ShowMe = True     # 视频聊天时是否打开本地摄像头
AudioOpen = True  # 是否打开音频聊天


def video_invite():
    global IsOpen, Version, AudioOpen
    if Version == 4:
        host_name = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    else:
        host_name = [i['addr'] for i in ifaddresses(interfaces()[-2]).setdefault(AF_INET6, [{'addr': 'No IP addr'}])][
            -1]

    invite = 'INVITE' + host_name + ':;' + user + ':;' + chat
    s.send(invite.encode())
    if not IsOpen:
        vserver = vachat.Video_Server(10087, Version)
        if AudioOpen:
            aserver = vachat.Audio_Server(10088, Version)
            aserver.start()
        vserver.start()
        IsOpen = True


def video_accept(host_name):
    global IsOpen, Resolution, ShowMe, Version, AudioOpen

    vclient = vachat.Video_Client(host_name, 10087, ShowMe, Resolution, Version)
    if AudioOpen:
        aclient = vachat.Audio_Client(host_name, 10088, Version)
        aclient.start()
    vclient.start()
    IsOpen = False


def video_invite_window(message, inviter_name):
    invite_window = tkinter.Toplevel()
    invite_window.geometry('300x100')
    invite_window.title('Invitation')
    label1 = tkinter.Label(invite_window, bg='#f0f0f0', width=20, text=inviter_name)
    label1.pack()
    label2 = tkinter.Label(invite_window, bg='#f0f0f0', width=20, text='invites you to video chat!')
    label2.pack()

    def accept_invite():
        invite_window.destroy()
        video_accept(message[message.index('INVITE') + 6:])

    def refuse_invite():
        invite_window.destroy()

    Refuse = tkinter.Button(invite_window, text="Refuse", command=refuse_invite)
    Refuse.place(x=60, y=60, width=60, height=25)
    Accept = tkinter.Button(invite_window, text="Accept", command=accept_invite)
    Accept.place(x=180, y=60, width=60, height=25)


def video_connect_option():
    global Resolution, ShowMe, Version, AudioOpen

    video_connect_option = tkinter.Toplevel()
    video_connect_option.geometry('150x450')
    video_connect_option.title('Connection option')

    var1 = tkinter.StringVar()
    label1 = tkinter.Label(video_connect_option, bg='#f0f0f0', width=20, text='Resolution   ')
    label1.pack()

    def print_resolution():
        global Resolution
        Resolution = var1.get()
        label1.config(text='Resolution   ' + Resolution)

    r0 = tkinter.Radiobutton(video_connect_option, text='0', variable=var1, value='0', command=print_resolution)
    r0.pack()
    r1 = tkinter.Radiobutton(video_connect_option, text='1', variable=var1, value='1', command=print_resolution)
    r1.pack()
    r2 = tkinter.Radiobutton(video_connect_option, text='2', variable=var1, value='2', command=print_resolution)
    r2.pack()
    r3 = tkinter.Radiobutton(video_connect_option, text='3', variable=var1, value='3', command=print_resolution)
    r3.pack()
    r4 = tkinter.Radiobutton(video_connect_option, text='4', variable=var1, value='4', command=print_resolution)
    r4.pack()

    var2 = tkinter.StringVar()
    label2 = tkinter.Label(video_connect_option, bg='#f0f0f0', width=20, text='Protocol version   ')
    label2.pack()

    def print_version():
        global Version
        Version = var2.get()
        label2.config(text='Version   IPv' + Version)

    v0 = tkinter.Radiobutton(video_connect_option, text='IPv4', variable=var2, value='4', command=print_version)
    v0.pack()
    v1 = tkinter.Radiobutton(video_connect_option, text='IPv6', variable=var2, value='6', command=print_version)
    v1.pack()

    var3 = tkinter.StringVar()
    label3 = tkinter.Label(video_connect_option, bg='#f0f0f0', width=20, text='Show yourself   ')
    label3.pack()

    def print_show():
        global ShowMe
        if var3.get() == '1':
            ShowMe = True
            txt = 'Yes'
        else:
            ShowMe = False
            txt = 'No'
        label3.config(text='Show yourself   ' + txt)

    s0 = tkinter.Radiobutton(video_connect_option, text='Yes', variable=var3, value='1', command=print_show)
    s0.pack()
    s1 = tkinter.Radiobutton(video_connect_option, text='No', variable=var3, value='0', command=print_show)
    s1.pack()

    var4 = tkinter.StringVar()
    label4 = tkinter.Label(video_connect_option, bg='#f0f0f0', width=20, text='Audio open   ')
    label4.pack()

    def print_audio():
        global AudioOpen
        if var4.get() == '1':
            AudioOpen = True
            txt = 'Yes'
        else:
            AudioOpen = False
            txt = 'No'
        label4.config(text='Audio open   ' + txt)

    a0 = tkinter.Radiobutton(video_connect_option, text='Yes', variable=var4, value='1', command=print_audio)
    a0.pack()
    a1 = tkinter.Radiobutton(video_connect_option, text='No', variable=var4, value='0', command=print_audio)
    a1.pack()

    def option_enter():
        video_connect_option.destroy()

    Enter = tkinter.Button(video_connect_option, text="Enter", command=option_enter)
    Enter.place(x=10, y=400, width=60, height=35)
    Start = tkinter.Button(video_connect_option, text="Start", command=video_invite)
    Start.place(x=80, y=400, width=60, height=35)


vbutton = tkinter.Button(root, text="Video", command=video_connect_option,bg='#AFEEEE',relief="solid")
vbutton.place(x=245, y=320, width=60, height=30)


# 私聊功能
def private(*args):
    global chat
    # 获取点击的索引然后得到内容(用户名)
    indexs = listbox1.curselection()
    index = indexs[0]
    if index > 0:
        chat = listbox1.get(index)
        # 修改客户端名称
        if chat == '------Group chat-------':
            root.title(user)
            return
        ti = user + '  -->  ' + chat
        root.title(ti)


# 在显示用户列表框上设置绑定事件
listbox1.bind('<ButtonRelease-1>', private)

# 保存日志
def savelogs(logs):
    user = logs['user']
    reciver = logs['reciver']
    message  = logs['message']
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "passwd123", "qq")
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO logs(user, reciver, message) VALUES ('%s','%s','%s')" % (user,reciver,message)
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交数据
        db.commit()
        #关闭连接
        db.close()
        # print('完成')
        return True
    except:
        #回滚数据
        db.rollback()
        # 关闭连接
        db.close()
        return None

# 用于时刻接收服务端发送的信息并打印
def recv():

    global users
    while True:
        data = s.recv(1024)
        data = data.decode()
        # 没有捕获到异常则表示接收到的是在线用户列表
        try:
            data = json.loads(data)
            users = data
            print(users)
            listbox1.delete(0, tkinter.END)  # 清空列表框
            number = ('   Users online: ' + str(len(data)))
            listbox1.insert(tkinter.END, number)
            listbox1.itemconfig(tkinter.END, fg='green', bg="#f0f0ff")
            listbox1.insert(tkinter.END, '------Group chat-------')
            listbox1.insert(tkinter.END, 'Robot')
            listbox1.itemconfig(tkinter.END, fg='green')
            for i in range(len(data)):
                listbox1.insert(tkinter.END, (data[i]))
                listbox1.itemconfig(tkinter.END, fg='green')
        except:
            data = data.split(':;')
            # print(data) # [' jluzh：nihao ', 'jluzh', 'Robot']
            data1 = data[0].strip()  # 我发送的信息
            data2 = data[1]  # 发送信息的用户名 自己
            data3 = data[2]  # 聊天对象 发送给的对象
            tmpsave = data3
            if tmpsave == '------Group chat-------':
                tmpsave = 'Group chat'
            # print(data2+'>'+tmpsave+':'+data1.split('：')[1])---jluzh>Group chat:q
            logs = {}
            logs['user'] = data2
            logs['reciver'] = tmpsave
            logs['message'] = data1.split('：')[1]
            try:
                savelogs(logs)
            except:
                print('日志存储失败')
            if 'INVITE' in data1:
                if data3 == 'Robot':
                    tkinter.messagebox.showerror('Connect error', message='Unable to make video chat with robot!')
                elif data3 == '------Group chat-------':
                    tkinter.messagebox.showerror('Connect error', message='Group video chat is not supported!')
                elif (data2 == user and data3 == user) or (data2 != user):
                    video_invite_window(data1, data2)
                continue
            markk = data1.split('：')[1]
            # print(markk)
            # 判断是不是图片
            pic = markk.split('#')
            # print(pic)
            # 判断是不是表情
            # 如果字典里有则贴图
            if (markk in dic) or pic[0] == '``':
                data4 = '\n' + data2 + '：'  # 例:名字-> \n名字：
                if data3 == '------Group chat-------':
                    if data2 == user:  # 如果是自己则将则字体变为蓝色
                        listbox.insert(tkinter.END, data4, 'blue')
                    else:
                        listbox.insert(tkinter.END, data4, 'green')  # END将信息加在最后一行
                elif data2 == user or data3 == user:  # 显示私聊
                    listbox.insert(tkinter.END, data4, 'red')  # END将信息加在最后一行
                if pic[0] == '``':
                    # 从服务端下载发送的图片
                    fileGet(pic[1])
                    # 贴图
                    try:
                        fileName = './Client_image_cache/' + pic[1]
                        img = tkinter.PhotoImage(file=fileName)
                        listbox.image_create(tkinter.END, image=img)
                    except Exception as e:
                        print(e)
                else:
                    # 将表情图贴到聊天框
                    listbox.image_create(tkinter.END, image=dic[markk])
            else:
                data1 = '\n' + data1
                if data3 == '------Group chat-------':
                    if data2 == user:  # 如果是自己则将则字体变为蓝色
                        listbox.insert(tkinter.END, data1, 'blue')
                    else:
                        listbox.insert(tkinter.END, data1, 'green')  # END将信息加在最后一行
                    if len(data) == 4:
                        listbox.insert(tkinter.END, '\n' + data[3], 'pink')
                elif data3 == 'Robot' and data2 == user:
                    listbox.insert(tkinter.END, data1, 'blue')
                    rsp = Tencent_AI_Chat_Robot(data1.split('：')[1])
                    reply_txt = '\nRobot:' + rsp
                    listbox.insert(tkinter.END, reply_txt, 'pink')
                elif data2 == user or data3 == user:  # 显示私聊
                    listbox.insert(tkinter.END, data1, 'red')  # END将信息加在最后一行
            listbox.see(tkinter.END)  # 显示在最后


r = threading.Thread(target=recv)
r.start()  # 开始线程接收信息

root.mainloop()
s.close()  # 关闭图形界面后关闭TCP连接
