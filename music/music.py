# -*- coding:utf-8 -*-
import os
from tkinter import *
import requests
from bs4 import BeautifulSoup
# 根据链接下载歌曲
from urllib.request import urlretrieve


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("创建成功")
    else:
        print("文件夹已经存在")


# 爬取网易云音乐函数
def downlaod_song():
    # https://music.163.com/#/playlist?id=515223310
    # https://music.163.com/playlist?id=515223310
    # 获取用户输入的url下载链接
    url = entry.get().replace('#/', '')
    header = {
        'Host':
        'music.163.com',
        'Referer':
        'http://music.163.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    html = requests.get(url, headers=header).text
    # 3.创建对象，解析网页,获取的s的数据类型成为一个对象，并且显示的html代码格式变得清晰了
    s = BeautifulSoup(html, 'html.parser')
    # print(s)
    # 3.获取id
    muisc_dict = {}
    result = s.find('ul', {'class', 'f-hide'}).find_all('a')
    # print(result)
    for music in result:
        muisc_id = music.get('href').strip('/song?id=')
        music_name = music.text
        muisc_dict[muisc_id] = music_name
    # print(muisc_dict)

    for song_id in muisc_dict:
        song_url = 'http://music.163.com/song/media/outer/url?id=%s' % song_id
        print(song_url)
        # 下载路径
        path = './download/%s.mp3' % muisc_dict[song_id]

        # 添加数据到列表框的最后
        text.insert(END, '正在下载:%s' % muisc_dict[song_id])
        # 文本框向下滚动
        text.see(END)
        # 更新(不更新就一直卡在那，显示同样的内容)
        text.update()

        # 下载歌曲
        urlretrieve(song_url, path)

    text.insert(END, '下载完成')
    text.see(END)
    text.update()


mkdir('./download')
# 1.创建窗口
root = Tk()
# 2.窗口标题
root.title('网易云音乐')
# 3.窗口大小以及显示位置,中间是小写的x
root.geometry('550x400+550+230')
# 窗口显示位置
# root.geometry('+573+286')
# 4.标签控件
lable = Label(root, text='请输入要下载的歌单URL:', font=('微软雅黑', 10))
lable.grid(row=0, column=0)

# 5.输入控件
entry = Entry(root, font=('微软雅黑', 25))
entry.grid(row=0, column=1)
entry.insert(0, "https://music.163.com/#/playlist?id=515223310")

# 6.列表框控件
text = Listbox(root, font=('微软雅黑', 16), width=45, height=10)
# columnspan组件所跨月的列数
text.grid(row=1, columnspan=2)
# 7.按钮控件
button = Button(
    root, text='开始下载', width=10, font=('微软雅黑', 10), command=downlaod_song)
button.grid(row=2, column=0, sticky=W)

button1 = Button(
    root, text='退出', width=10, font=('微软雅黑', 10), command=root.quit)
button1.grid(row=2, column=1, sticky=E)

# 消息循环,显示窗口
root.mainloop()
