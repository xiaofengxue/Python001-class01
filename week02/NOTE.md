异常捕获
参考https://docs.python.org/zh-cn/3.6/library/exceptions.html 所有内置的非系统退出的异常都派生自Exception 类
所有内置的非系统退出的异常都派生自Exception

异常处理机制的原理
异常也是一个类
 • 异常捕获过程： 
	1. 异常类把错误消息打包到一个对象 
	2. 然后该对象会自动查找到调用栈
     3. 直到运行系统找到明确声明如何处理这些类异常的位置
• 所有异常继承自BaseException
• Traceback显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的

异常信息与异常捕获：
• 异常信息在Traceback信息的最后一行，有不同的类型
       • 捕获异常可以使用try…except语法 
       • try…except支持多重异常处理

常见的异常类型主要有： 
1. LookupError 下的 IndexError 和 KeyError
       2. IOError 
3. NameError 
4. TypeError 
5. AttributeError 
6. ZeroDivisionError

对于except（except1，except2....）对于多个异常的捕获，如果捕获到第一个异常，后面的异常就不会捕获了
抛出和自定义异常：
使用raise语句抛出异常
自定义异常建议从Exception继承
示例：
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):   # 函数可以以字符串的形式调用
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput

2. pretty_errors 官方文档链接：
https://pypi.org/project/pretty-errors/
3. try 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement
4. with 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement
5. with 语句上下文管理器官方文档：
https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers


反爬虫
1、根据用户基本的请求做判断
2、根据用户的行为做判断

爬虫的本质：模拟浏览器
模拟用户的行为，爬虫效率不高
反反爬虫：模拟用户的请求
浏览器的行为：	
1、带HTTP的头部信息：如：User-Agent，Referer（防止跨站）等（User-Agent大全，F12抓包）
模拟浏览器的头部信息：
模拟User-Agent
模拟Referer
2、带cookies（包含加密的用户名和密码验证信息）
有效期的限制，
模拟用户登录
post方式：
关注点：
url
post 方式
user-agent 
referer

中间件：
spidermiddlewares
downloademiddlewares

自定义中间件
随机设置代理IP：
1、settings.py 设置代理IP列表：HTTP_PROXY_LIST(设置项变量大写)
2、settings.py 修改DOWNLOADER_MIDDLEWARES 
3、middlewares.py自定义中间件，通过集成原有的中间件的类HttpProxyMiddleware
      __init__    : 初始化设置项
      from_crawler: 解析设置项
     _set_proxy   设置代理

本次作业心得：

如何将爬取的数据插入mysql数据库？
这里采用异步存储的方式（爬虫和写入数据分开执行，互不影响，提高数据库的访问效率）
异步存储数据库大致分为以下步骤：
1、在settings配置文件中配置mysql连接的参数（主机地址、用户账号、密码、端口号、数据库、数据库编码）
2、自定义pipelines，实现from_settings函数
3、from twisted.enterprise import adbapi 引入连接池模块
adbapi.ConnectionPool方法可以创建一个数据库连接池对象，其中包括多个连接对象，每个连接对象在独立的线程中工作。adbapi只是提供了异步访问数据库的编程框架，再其内部依然使MySQLdb这样的库访问数据库。
dbpool.runInteraction(insert_db,item)以异步方式调用insert_db函数，dbpool会选择连接池中的一个连接对象在独立线程中调用insert_db，其中参数item会被传给insert_db的第二个参数，传给insert_db的第一个参数是一个Transaction对象，其接口与Cursor对象类似，可以调用execute方法执行SQL语句，insert_db执行后，连接对象会自动调用commit方法
4、重写process_item方法
query =  self.db_pool.runInteraction(执行插入数据操作的函数对象，函数需要参数)，并接受执行返回结果
uery.addErrback(错误回调函数，函数需要参数)，添加执行sql失败回调的函数，在回调函数中对错误数据进一步处理

 增加代理IP：
	在settings配置文件中增 DOWNLOADER_MIDDLEWARES增加scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware

  通过selenium模拟用户登录：
获取登录连接
获取用户名输入框，填入用户名
获取密码输入框，填入米面
获取登录button




