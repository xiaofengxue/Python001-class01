学习笔记
1. pandas 中文文档：
https://www.pypandas.cn/
sklearn-pandas
2. 安装参考文档：
https://pypi.org/project/sklearn-pandas/1.5.0/
3. Numpy 学习文档：
https://numpy.org/doc/
4. matplotlib 学习文档：
https://matplotlib.org/contents.html

5. Series 学习文档：
https://pandas.pydata.org/pandas-docs/stable/reference/series.html

6. DataFrame 学习文档：
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

7. Pandas 计算功能操作文档：
https://pandas.pydata.org/docs/user_guide/computation.html#method-summary

8. jieba 学习文档：
https://github.com/fxsjy/jieba/blob/master/README.md

关于python中的axis的定义：
axis=0指的是逐行，axis=1指的是逐列

df.mean其实是在每一行上取所有列的均值，而不是保留每一列的均值。
也许简单的来记就是axis=0代表往跨行（down)，而axis=1代表跨列（across)，作为方法动作的副词
使用0值表示沿着每一列或行标签\索引值向下执行方法
使用1值表示沿着每一行或者列标签模向执行对应的方法
mean(axis=0)计算的是每一列平均值， 
mean(axis=1)计算的是每一行平均值。 
drop(0,axis=0)删除行， 
drop([‘col1’],axis=1)删除列。
