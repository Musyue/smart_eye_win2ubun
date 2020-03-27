#coding=utf-8
#引入套接字
import socket
import time
def tcpSend():
    #创建套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口，发送数据时会从绑定的端口发送，不会再生成随机端口
    tcp_socket.bind(("", 8001))
    #连接服务器
    tcp_socket.connect(("192.168.1.16",8090))#变量为元组
    # while True:
    #数据传输
    send_data=input("请输入传输的数据")
    tcp_socket.send(send_data.encode("utf-8"))
    #关闭套接字
    tcp_socket.close()
def main():
    tcpSend()
if __name__=="__main__":
    main()