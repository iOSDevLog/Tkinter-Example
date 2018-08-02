# -*- coding:utf-8 -*-
# https://gitbook.cn/books/5b4d510905a002571926ed7e/index.html

from tkinter import *
from tkinter import messagebox
import requests


# 根据用户输入内容翻译
def translation():
    # 获取用户输入的内容
    content = entry.get()
    if content == '':
        messagebox.showinfo('提示', '请输入需要翻译的内容')
    else:
        print(content)
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    # data['salt'] = '1530332652360' # 时间戳
    # data['sign'] = '7f281888e41d12a63b20790707672708'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    result = requests.post(url, data=data, headers=header)
    translation = result.json()
    translation = translation['translateResult'][0][0]['tgt']
    print(translation)
    res.set(translation)


# 1.创建窗口
root = Tk()
# 2.窗口标题
root.title('中英文互译')
# 3.窗口大小以及显示位置,中间是小写的x
root.geometry('320x100+573+286')
# 窗口显示位置
# root.geometry('+573+286')
# 变量
res = StringVar()
# 4.标签控件
lable = Label(root, text='输入要翻译的文字:', font=('微软雅黑'))
lable.grid(row=0, column=0)

lable1 = Label(root, text='翻译后的结果:', font=('微软雅黑'))
lable1.grid(row=1, column=0)

# 5.输入控件
entry = Entry(root, font=('微软雅黑'))
entry.grid(row=0, column=1)
# 翻译之后的结果
entry1 = Entry(root, font=('微软雅黑'), textvariable=res)
entry1.grid(row=1, column=1)

# 6.按钮控件
button = Button(
    root, text='翻译', width=10, font=('微软雅黑', 10), command=translation)
button.grid(row=2, column=0, sticky=W)

button1 = Button(
    root, text='退出', width=10, font=('微软雅黑', 10), command=root.quit)
button1.grid(row=2, column=1, sticky=E)

# 消息循环,显示窗口
root.mainloop()
