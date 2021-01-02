import requests
from lxml import etree
# url = "https://music.163.com/song/media/outer/url?id=1806584346.mp3"
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# }
# rep = requests.get(url,headers=headers)
# with open('test4.mp3','wb') as fp:
#     fp.write(rep.content)
url ='https://music.163.com/discover/toplist'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
rep = requests.get(url,headers=headers)
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
for i in range(0,100):
    music = {}
    music['id']=links[i].split('=')[1]
    music['name']=names[i]
    msglist.append(music)

for music in msglist:
    url = "https://music.163.com/song/media/outer/url?id="+music["id"]+".mp3"
    path = "./music/"+music["name"]+'.mp3'
    rep = requests.get(url,headers=headers)
    with open(path,'wb') as fp:
        fp.write(rep.content)
    print(music)
