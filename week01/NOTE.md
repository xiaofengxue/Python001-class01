1、python官方文档：： https://docs.python.org/zh-cn/3.7/
2、git的安装使用：
	初始化本地仓库：git init
	配置用户名邮箱：git config --global user.name "username"
			  git config --global user.email "email"
	
	查看仓库状态：git status
   跟踪文件命令：git add .
   提交文件命令：git commit -m '注释说明'
   查看历史提交状态：git log
   
   fork;复制仓库
	clone  克隆到本地 ： git  clone  git@github.com:xiaofengxue/Python001-class01.git
	git push -u origin master 
	作业提交链接：https://github.com/Python001-class01/Python001-class01/issues/1

3、requests 两个方法：
	post 发送请求
	get  获取响应内容
4、Beautiful Soup 官方文档链接： https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
	find_all('div',attrs={'class':'movie-item-hover'}) : 查找div标签下class属性为：'movie-item-hover对应的内容
	get_text()  获取文本内容
5、 Scrapy Xpath 官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
	Xpath 中文文档：
	https://www.w3school.com.cn/xpath/index.asp
	Xpath 英文文档：
	https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf
  xpath('//div[@class="movie-hover-info"]')  // 灵活匹配
  ./ 下一级目录寻找
 ../ 同级目录寻找
/text() 获取文本内容
/@href  获取属性美容

Scrapy核心组件
Scrapy 核心组件 简介
引擎（Engine）“大脑”，指挥其他组件协同工作。 
调度器（Scheduler） 调度器接收引擎发过来的请求，按照先后顺序，压入队列中，同时去除重复的请求。 
下载器（Downloader） 下载器用于下载网页内容，并返回给爬虫。
爬虫（Spiders）        用于从特定的网页中提取需要的信息，即所谓的实体（Item） 用户也可以从中提取出链接，让 Scrapy 继续抓取下一个页面。
项目管道（Item Pipelines）项目管道负责处理爬虫从网页中抽取的实体。 主要的功能是持久化实体、验证实体的有效性、清除不需要的信息等。


scrapy engine 通过配置找到所需的域名进行爬取数据
通过域名找到相对应的spiders
对应的spiders通过要爬取指定的url进行请求的发起，到scheduler
scheduler首先自动做一遍去重，再根据请求的先后顺序发给scrapy engine，
scrapy engine 再通过Downloader进行请求，
Downloader根据请求的网页传送给scrapy engine，由scrapy engine判断是否在进行爬取或者存到指定的管道（item pipeline）



关键代码：
创建一个爬虫工程：scrapy startproject spiders
初始化文件：scrapy genscrapy movies douban.com
运行爬虫:scrapy crawl name 
requests
response = requests.get(myurl,headers=header)
import pandas as pd movie1 = pd.DataFrame(data = mylist)

scrapy
yield scrapy.Request(url=url, callback=self.parse)
item = response.meta['item'] item['content'] = content




  