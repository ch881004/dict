"""
dict 客户端

功能：根据用户输入，发送请求，得到结果
结构：一级界面-->注册 登录 退出
    二级界面-->查询单词 历史记录 注销
"""
from socket import *
from getpass import getpass  # 运行使用终端

# 服务器地址
ADDR = (("127.0.0.1", 8888))


# 注册
def do_register(s, cmd):
    while True:
        name = input("User：")
        passwd = getpass()
        passwd1 = getpass("Again:")

        if passwd != passwd1:
            print("两次密码不一致！")
            continue
        if " " in name or " " in passwd:
            print("用户名和密码不允许存在空格！")
            continue

        msg = "R %s %s" % (name, passwd)
        s.send(msg.encode())  # 发送给服务器
        data = s.recv(128).decode()  # 接受结果
        if data == "OK":
            print("注册成功")
        else:
            print("注册失败")
        return

    # 搭建客户端网络


def main():
    s = socket()
    s.connect(ADDR)
    while True:
        print("""
        ===============================
            1.注册    2.登录    3.注销
        ===============================
        """)
        cmd = input("请输入选项：")
        if cmd == "1":
            do_register(s, cmd)
        elif cmd == "2":
            s.send(cmd.encode())
        elif cmd == "3":
            s.send(cmd.encode())
        else:
            print("请输入正确选项！")


if __name__ == '__main__':
    main()
