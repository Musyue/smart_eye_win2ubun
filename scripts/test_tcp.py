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
    tcp_socket.connect(("192.168.1.197",8000))#变量为元组
    # while True:
    #数据传输
    send_data=input("请输入传输的数据")
    tcp_socket.send(send_data.encode("utf-8"))
    #关闭套接字
    tcp_socket.close()
 
#tcp与udp不同，tcp必须先运行服务器客户端才能连接
def tcpRecv():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口，接收数据时会从绑定的端口发送，不会再生成随机端口
    tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_socket.bind(("", 8090))
    #listen使套接字变成可以被动链接
    tcp_socket.listen(128)
    # 为多个客户端服务while True:
    count=0

    while True:
        #accept等待客户端的链接,返回一个客户端元组
        client_scoket , client_addr = tcp_socket.accept()
        print(client_addr)
        while True:
            count+=1
            print("Send S1 to client to start cam---:the send num:%d",count)
            client_scoket.send("S1".encode("utf-8"))
            # 为一个客户端服务多次while True:
            #数据传输,接受请求后回复
            recv_data=client_scoket.recv(1024)
            print(recv_data)
            #客户端不需要服务.recv解堵塞，两种情况，客户端发送数据或客户端调用close。 if recv_data:发送了数据 else 关闭break
            # client_scoket.send("S1".encode("utf-8"))
            time.sleep(5)
            print("time out,go to next cam point")
            # 关闭套接字
            if recv_data=="Quit":
                client_scoket.close()
    tcp_socket.close()
 
if __name__ == '__main__':
    #tcpSend()
    # while 1:
    tcpRecv()
        # time.sleep(3)