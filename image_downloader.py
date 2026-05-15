import os
import requests
from urllib.parse import urlencode

# 请求并解析网址
def urls(url):
    html = requests.get(url)
    content = html.json()
    return content

# 打开或创建文件夹
def open_file(names):
    if not os.path.exists(names):
        os.makedirs(names)

# 拿到图片链接下载图片到文件夹
def download(name, file, link, n):
    picture = requests.get(link).content
    with open(file, "wb") as f:
        f.write(picture)
    print(f"已下载第{n}张", flush=True)

# 找到所有图片链接并下载
def tag(content, names, name, n):
    content_list = content.get("data", {}).get("object_list", [])
    open_file(names)
    if not content_list:
        print("未找到, 请重试更小的页码", flush=True)
    else:
        for i in content_list:
            n += 1
            link = i["photo"]["path"]
            if link:
                file = os.path.join(names, f"{name}{n}.jpg")
                download(name, file, link, n)
            else:
                print("未找到, 请重试更小的页码", flush=True)
        print("已全部下载完成", flush=True)

keyword = {
    "kw": "伊蕾娜",
    "start": 0
}

n = 0
while True:
    print("图片下载器(动漫美图)\n--------------------")
    keywords = input("请输入图片关键词：")
    number = int(input("请输入第几页(从第一页开始, 一页24张)："))
    if number > 0:
        numbers = number*24-24
        keyword["kw"] = keywords
        keyword["start"] = numbers
        names = input("输入文件夹名称没有则自动创建到当前目录：")
        name = input("请给图片命名(小心覆盖原图片)：")
        url = f"https://www.duitang.com/napi/blog/list/by_search/?{urlencode(keyword, encoding='utf8')}"
        try:
            content = urls(url)
            tag(content, names, name, n)
        except Exception as e:
            print(e, flush=True)
    else:
        print("输入页数小于1, 请重新输入", flush=True)

