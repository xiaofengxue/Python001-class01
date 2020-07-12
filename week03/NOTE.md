学习笔记

1、Scrapy并发参数优化原理
settings 参数调优 
# Configure maximum concurrent requests performed by Scrapy (default: 16) 最大请求数量 默认16
#CONCURRENT_REQUESTS = 32
    # Configure a delay for requests for the same website (default: 0)  请求延时时间 
    DOWNLOAD_DELAY = 3 
    # The download delay setting will honor only one of: 
    #CONCURRENT_REQUESTS_PER_DOMAIN = 16 
    #CONCURRENT_REQUESTS_PER_IP = 16

2、基于twisted的异步io框架

3、多线程与多进程
1. os 模块学习文档：
https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html#operating-system-interface
2. multiprocessing – 基于进程的并行学习文档： https://docs.python.org/zh-cn/3.7/library/multiprocessing.html

进程的父子关系
multiprocessing 模块 
multiprocessing.process(group=None,target=None,args=(),kwargs={})
group:分组
target:对象调用，
name:别名
args:参数元组
kwargs:调用对象的字典
start() 进程开始
join() 进程终止

进程之间的通信
共享方式：队列、管道、共享内存
4、多线程
1. 基于线程的并行学习文档：https://docs.python.org/zh-cn/3.7/library/threading.html
2. 基于进程的并行学习文档：https://docs.python.org/zh-cn/3.7/library/multiprocessing.html
3. 底层多线程 API：https://docs.python.org/zh-cn/3.7/library/_thread.html

4、进程和线程的区别：多个线程在一个线程中运行，多线程之间数据同步会更方便。

5、阻塞状态：一直等待对方请求发起状态，在调用结果返回之前，当前线程会处于挂起状态。（发起方的行为）

      非阻塞状态：不用等待对方发起请求，在不能立刻得到返回结果之前不会阻塞当前线程，会立刻返回（发起方的行为）
	  同步：就是在发出一个功能调用时，在没有得到结果之前，该调用就不返回（被发起方）
      异步：当一个异步过程调用发出后，调用立刻返回，调用者不能立刻得到结果（被发起方）
      # 调用方
	  # 阻塞  得到调用结果之前，线程会被挂起
	  # 非阻塞 不能立即得到结果，不会阻塞线程

	  # 被调用方 
      # 同步 得到结果之前，调用不会返回
      # 异步 请求发出后，调用立即返回，没有返回结果，通过回调函数得到实际结果

6、多线程只能在一个cpu上运行，多进程可以开辟更多的cpu

7、协程负责管理调度多进程之间的运行

8、并发：多线程的运行机制（多个队列排队等待一个咖啡机）
      并行：多进程的运行机制（多个队列排队等待多个对应的咖啡机）

9、锁机制
      普通锁Lock     嵌套锁RLock
	  2. 锁对象学习文档：https://docs.python.org/zh-cn/3.7/library/threading.html#lock-objects
     3. 递归锁对象：https://docs.python.org/zh-cn/3.7/library/threading.html#rlock-objects

10、队列（先进先出）
        import queue   存队列put  取队列 get
	    queue 学习文档：https://docs.python.org/zh-cn/3.7/library/queue.html

11、多线程在cpython解释器的基础上实际上是一个伪多线程的操作，这里存在一个全局锁GIL，他在一段时间内只允许一个线程去操作，其他线程都处于等待状态，对于CPU密集型的操作，多线程的优势并不明显，在对于IO密集型的任务，多线程的优势才能体现出来。

作业心得总结：
1、argparse模块的使用，主要有三个步骤：
创建 ArgumentParser() 对象
调用 add_argument() 方法添加参数
使用 parse_args() 解析添加的参数
2、IP地址的判读与解析，判断IP地址可以使用IPy模块（返回状态），解析IP，主要是针对参数为IP段时使用，并以列表的形式返回IP
3、subprocess模块的使用，可以生成新的进程，返回状态码（0：成功），通过这个模块监测扫描服务器是否可以ping通
4、tcp端口的监测，使用socket 套接字，同时捕获异常。
5、通过将结果数据转化成字典，在通过字典转换成json文件。
6、采用进程池和线程池的方式对程序进行并发执行。









    
   