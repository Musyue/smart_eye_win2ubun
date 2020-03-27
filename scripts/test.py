import math
def cacu_square(apoint,bpoint,cpoint):
    x=(apoint[0]-bpoint[0])
    y=(apoint[1]-bpoint[1])
    z=(apoint[2]-bpoint[2])
    len1=math.sqrt(x*2+y*2+z*2)
    print len1
    x1=(cpoint[0]-bpoint[0])
    y1=(cpoint[1]-bpoint[1])
    z1=(cpoint[2]-bpoint[2])
    len2=math.sqrt(x1*2+y1*2+z1*2)
    print len2
apoint=[0.155,-0.152,0.485]
bpoint=[-0.181,-0.190,0.720]
cpoint=[-0.196,0.101,0.730]
cacu_square(apoint,bpoint,cpoint)

apoint=[0.283,-0.277,0.894]
bpoint=[-0.183,-0.265,0.987]
cpoint=[-0.203,0.148,1.00]
cacu_square(apoint,bpoint,cpoint)
# import threading
# import inspect
# import ctypes
# import time

# # https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
# def _async_raise(tid, exctype):
#     if not inspect.isclass(exctype):
#         raise TypeError("Only types can be raised (not instances)")
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
#                                                   ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
#         raise SystemError("PyThreadState_SetAsyncExc failed")

# # https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
# class ThreadWithExc(threading.Thread):
#     def _get_my_tid(self):

#         if not self.isAlive():
#             raise threading.ThreadError("the thread is not active")

#         if hasattr(self, "_thread_id"):
#             return self._thread_id

#         for tid, tobj in threading._active.items():
#             if tobj is self:
#                 self._thread_id = tid
#                 return tid

#         raise AssertionError("could not determine the thread's id")

#     def raiseExc(self, exctype):
#         _async_raise(self._get_my_tid(), exctype )

# def work():
#     try:
#         while True:
#             print('work')
#             time.sleep(1)
#     except Server.ThreadStopped:
#         pass

#     print('exiting work() function')

# class Server:
#     class ThreadStopped(Exception): pass

#     def __init__(self):
#         self.thread = ThreadWithExc(target=work)

#     def start(self):
#         self.thread.start()

#     def stop(self):
# #        _async_raise(self.thread.raiseExc(TypeError))
#         self.thread.raiseExc(self.ThreadStopped)

# server = Server()
# server.start()
# server.stop()