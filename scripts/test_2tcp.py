#coding=utf-8
import socket
import threading
import time
import inspect
import ctypes

import base64
import re
import time
def read(socket_fuwu):
    print("In read ")
    before=time.time()
    print("before",before)
    while True:
        recv_data = socket_fuwu.recv(4096)#(1024)

        if recv_data:
            # print(recv_data)
            print(recv_data.decode('utf-8', errors="replace"))      #因为在window测试，所以使用gbk编码规则
            
            # strdata=recv_data#.decode('hex')
            # print(str(strdata))
    #         nums=re.findall(r'\d+(?:\.\d+)?', strdata)
            after=time.time()
            print("after",after)

    # print(len(nums))
    # print(after-before)
            # print(int.from_bytes(recv_data,'big'))
            # print(base64.b64decode(recv_data).decode('utf-8'))
def write(socket_fuwu):
    print("In write")
    count=0
    while True:
        socket_fuwu.send("S4".encode('utf-8'))
        time.sleep(200)
        count+=1
        print("go to next point %d",count)

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_ulong(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    print("stop thread")
    _async_raise(thread.ident,SystemExit)

def isThreadAlive(t):
    # for t in threads:
    if t.isAlive():
        return 1
    else:
        return 0

def main():
    tcp_socket_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket_host.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_socket_host.bind(('',8090))
    tcp_socket_host.listen(128)
    socket_fuwu,addr_client=tcp_socket_host.accept()
    print(socket_fuwu)
    print(addr_client)

    t1=threading.Thread(target=read,args=(socket_fuwu,))
    t2=threading.Thread(target=write,args=(socket_fuwu,))
    
    t1.start()
    t2.start()
    t1id=0
    t1id=0
    for tid, tobj in threading._active.items():
        print(tid,tobj)
        if tobj==t1:
            t1id=tid
        elif tobj==t2:
            t2id=tid
        else:
            pass
    threads=[]
    threads.append(t1)
    threads.append(t2)
    flag=1
    flag2=0
    while flag:
        time.sleep(3)
        flag2=isThreadAlive(t1)
        if flag2:
            print("threading t1 alive check loop")
        if flag2==0:
            print("t1",flag2)
            # stop_thread(t1)
            # t1=threading.Thread(target=read,args=(socket_fuwu,))
            # t1.start()
            # t1.clone()
        flag2=isThreadAlive(t2)
        if flag2==0:
            print("t2",flag2)
        if flag2:
            print("threading t2 alive check loop")
            # t2.clone()

    # print t1.isAlive()
    # print t2.isAlive()

    # socket_fuwu.close()    #服务器一般不关闭   此时服务端口因为需要一直执行所以也不能关闭


if __name__ == '__main__':
    main()