import time
import json
import os

# 延时函数
def yan_shi(s):
    time.sleep(s)

# 读取用户信息文件
def load_users():
	if not os.path.exists("users.json"):
		with open("users.json", "w", encoding = "utf-8") as f:
			json.dump({}, f, indent = 4)
	else:
		with open("users.json", "r", encoding = "utf-8") as f:
			users = json.load(f)
			return users
	return {}

# 保存用户信息文件
def save_users(users):
	with open("users.json", "w", encoding = "utf-8") as f:
		json.dump(users, f, indent = 4)

# 用户登录
def deng_lu():
    while True:
        yong_hu_ming = input("请输入用户名（输入“t”回到指令页面）：")
        if yong_hu_ming == "t":
            print("正在返回...")
            yan_shi(0.5)
            break
        elif yong_hu_ming in users:
            mi_ma = input("请输入密码：")
            if users[yong_hu_ming]["密码"] == mi_ma:
                print("登录中请稍后...")
                yan_shi(0.5)
                print("登录成功")
                yong_hu_xin_xi(yong_hu_ming)
                break
            else:
                print("密码错误，请重新输入")
                yan_shi(0.5)

        else:
            print("用户名不存在，请先注册账号")
            yan_shi(0.5)
            
# 用户操作系统
def yong_hu_xin_xi(yong_hu_ming):
    print("你可以查看用户信息和更改密码\n----------\n输入“c”查看用户信息\n输入“g”更改账户密码\n输入“t”退出账户\n----------")
    while True:
        a = input("请输入(查看指令输入“r”)：")
        if a == "t":
            print("正在退出账户...")
            yan_shi(0.5)
            print("退出成功")
            break
        elif a == "c":
            for cha_kan in users[yong_hu_ming]:
                print(f"{cha_kan}: {users[yong_hu_ming][cha_kan]}")
        elif a == "g":
            while True:
                b = input("请输入原密码(返回请输入“f“)：")
                if b == "f":
                    print("返回中...")
                    yan_shi(0.5)
                    break
                elif b == users[yong_hu_ming]["密码"]:
                    while True:
                     mi_ma = input("请输入新密码：").replace(" ", "")
                     if not mi_ma:
                          print("密码不能包含空格或为空")
                     elif len(mi_ma) >=6:
                          break
                     else:
                          print("字数小于限制X>6")
                    users[yong_hu_ming]["密码"] = mi_ma
                    print("设置成功，正在返回...")
                    save_users(users)
                    yan_shi(0.5)
                    break
                else:
                    print("密码错误，请重新输入")
                    yan_shi(0.5)
        elif a == "r":
            print("----------\n输入“c”查看用户信息\n输入“g”更改账户密码\n输入“t”退出账户\n----------")
        else:
            print("请输入有效指令")
            yan_shi(0.5)

# 用户注册
def zhu_ce():
    while True:
        while True:
            yong_hu_ming = input("请输入用户名(输入“t”取消注册)：").replace(" ","")
            if yong_hu_ming == "t":
            	print("已取消，正在返回...")
            	yan_shi(0.5)
            	break
            if not yong_hu_ming:
            	print("用户名不能为空, 包含空格则自动去除")
            elif len(yong_hu_ming) <= 10:
                break
            else:
            	print("字数限制X<10，请重新输入")
        if yong_hu_ming == "t":
        	break
        if yong_hu_ming in users:
            print("用户名已存在，请换一个名字")
        else:
            while True:
            	mi_ma = input("请输入密码：").replace(" ", "")
            	if not mi_ma:
            		print("密码不能为空, 包含空格则自动去除")
            	elif len(mi_ma) >=6:
            		break
            	else:
            		print("字数限制X>6")
            users[yong_hu_ming] = {
                "密码": mi_ma,
                "等级": 1
            }
            save_users(users)
            print("注册成功，正在返回...")
            yan_shi(0.5)
            break

# 用户注销
def zhu_xiao():
    while True:
        yong_hu_ming = input("请输入您要注销的用户名(输入“t”取消注销)：")
        if yong_hu_ming == "t":
            print("已取消，正在返回...")
            yan_shi(0.5)
            break
        elif yong_hu_ming in users:
            mi_ma = input("请输入密码：")
            if users[yong_hu_ming]["密码"] == mi_ma:
                del users[yong_hu_ming]
                print("注销成功，正在返回...")
                save_users(users)
                yan_shi(0.5)
                break
            else:
                print("密码错误，请重新输入")
                yan_shi(0.5)
        else:
            print("不存在用户名，无法注销")
            yan_shi(0.5)

# 用于提示用户指令
def zhi_ling():
    print("__________\n登录账户请输入“d”\n注册账户请输入“f”\n注销账户请输入“g”\n__________")

users = load_users()
print("账户登录\n__________\n登录账户请输入“d”\n注册账户请输入“f”\n注销账户请输入“g”\n__________")
while True:
    a = input("请输入指令（输入“r”查看指令）：")
    if a == "d":
        deng_lu()
    elif a == "f":
        zhu_ce()
    elif a == "g":
        zhu_xiao()
    elif a == "r":
        zhi_ling()
    else:
        print("请输入有效指令")