# Regal
====

[![pyversions](https://img.shields.io/badge/Python-2%20%26%203-brightgreen.svg)]()
[![ver](https://img.shields.io/badge/release-v1.1-red.svg)]()
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![coverage](https://img.shields.io/badge/coverage-92%25-yellowgreen.svg)]()
[![Build Status](https://travis-ci.org/boylegu/regal.svg?branch=master)](https://travis-ci.org/boylegu/regal)

用于"灰度发布"或 A/B Testing的智能分组引擎

## Regal能做什么？
举个最简单的例子，比如需要针对一个版本进行灰度发布，而这一版本对应的可能是一大堆服务器集群， 如下图:

![](http://i4.tietuku.com/71281a19596c5dd1.png)

就像图中描述的一样，无论你的服务器是多还是少，尤其很多中小型企业在进行灰度发布时，通常会遇到所制定的分流策略在实际的技术或开发中如何去实现，是机器直接写死？

因此让``Regal智能分组引擎``直接介入，让它来根据你的策略提前进行动态地分组分流。
在这里，我再举一个简单的例子，方便大家能够更清楚的明白Regal的主要工作：

假设有一个版本A，需要针对六台机器进行发布

![](http://i4.tietuku.com/5f7d4115746b6e97.png)

现在应该已经了解Regal到底是什么干货了吧，当然了，上面的例子是服务器非常少的情况，实际情况中，所面对的服务器集群是非常多，这个时候可以通过提供的``combine``和``schedule``两个API进行策略调整。详情可以见下文的``使用介绍``

- Feature：

  1. 提供发布策略，动态智能分流
  2. 支持多版本分组和优先级
  3. 数据格式化
  4. 同时兼容Python2.5以上和Python3以上的版本（建议使用Python2.7+或者Python3.5以后的版本）
  

## 安装和使用

### 安装

 -  `` pip install regal ``

### 使用说明

- 单个版本场景

```
In [1]: from regal import BaseInfo


# 初始化信息，请注意一下格式
In [6]: ab = BaseInfo(
version_host={'app-test-version1.0':'10.1.1.1,10.1.1.2,10.1.1.3,10.1.1.4,10.1.1.1.5'},
combine=2    # combine 希望以每组多少台服务器作为一组,进行用户群B的分流
             # 在这个例子中为2台
             # 默认：每组1台
)

# grouping() 进行分组
In [11]: smart_grouping = ab.grouping() 


# result属性 进行分组后的返回结果
In [12]: smart_grouping.result
Out[12]:
[('app-test-version1.0',
  [['10.1.1.1'], ['10.1.1.2', '10.1.1.3'], ['10.1.1.4', '10.1.1.1.5']])]
```
根据你的策略设置，会得到一个数据结构，我们来观察一下：

![](http://i4.tietuku.com/70e4610ed795f74e.png)

再看一个例子

```
In [7]: ab = BaseInfo(
version_host={'app-test-version1.0':'10.1.1.1,10.1.1.2,10.1.1.3,10.1.1.4,10.1.1.5'},
combine=3,
schedule=2)

In [10]: ab.grouping().result
Out[10]:
[('app-test-version1.0',
  [['10.1.1.1,10.1.1.2'], ['10.1.1.3', '10.1.1.4', '10.1.1.5']])]

```

- 多版本场景

``` 
In [17]: ab = BaseInfo(
   ....: version_host={
   ....: 'app-test-version1.0': '10.1.1.1,10.1.1.2,10.1.1.3,10.1.1.1.4,10.1.1.5',
   ....: 'app-test-version2.0': '10.1.1.9,10.1.1.8,10.1.1.7,10.1.1.6'},
   ....: combine=3,
   ....: schedule=2
   ....: )
   
In [20]: ab.grouping().result
Out[20]:
[('app-test-version2.0', [['10.1.1.9,10.1.1.8'], ['10.1.1.7', '10.1.1.6']]),
 ('app-test-version1.0',
  [['10.1.1.1,10.1.1.2'], ['10.1.1.3', '10.1.1.1.4', '10.1.1.5']])]   


# grouping()方法还提供了priority_name参数，当需要在多版本发布的时候，设置优先级，指定你需要优先发布的'版本名'
 In [22]: smart_grouping = ab.grouping(priority_name='app-test-version1.0')

In [23]: smart_grouping.result
Out[23]:
[('app-test-version1.0',
  [['10.1.1.1,10.1.1.2'], ['10.1.1.3', '10.1.1.1.4', '10.1.1.5']]),
 ('app-test-version2.0', [['10.1.1.9,10.1.1.8'], ['10.1.1.7', '10.1.1.6']])]

# 提供一个简易的API，可以让结果返回的更简洁  
In [16]: for i in smart_grouping.iter_dict():   
    print i
   ....:
{'app-test-version1.0': ['10.1.1.1', '10.1.1.2,10.1.1.3', '10.1.1.4,10.1.1.1.5']}

```

## Demo

- 你也可以通过 `` git clone https://github.com/boylegu/regal/ ``

- `` cd regal/ ``

- 参考`` example.py ``


## 分流分组之后？

Regal本身只是一个分组引擎，因此它并不承担直接发布的作用，但是通过Regal分组之后，你所得到数据，是非常容易和其他可以用来发布的组件进行配合；下面是我的一些建议和指导。

```
versionA:

  （第一组）    groupA   ip......     用户群A    
  （第二组）    groupB1  ip...... __ 
  （第三组）    groupB2  ip......   |
  （第四组）    groupB3  ip......   | --   用户群B   
   ......                       --|
```

- 关于发布

  分组之后，每一组的所有机器可以看作一个整体，扔进发布组件，进行'组内并发'

  你可以把每一组直接放在ansible、saltstack、pssh或异步IO框架等等进行发布；
  
  甚至你也可以和前端nginx＋lua进行组合；

- 关于停止发布

  每组进行发布，一旦出现异常，你可以利用发布组件，或者你自己写一套异常抓取工具来停止发布，这个时候就不会再针对剩下的组进行发布操作了。

- 关于回滚

  把回滚也看作一种发布,就不多说了

## 作者

- 顾鲍尔 (Boyle Gu)
  
## 技术交流与支持

有任何问题、建议可以通过Github；

也可以直接加入讨论群 QQ：315308272 与我进行交流


## Darwin's finches

![](http://i4.tietuku.com/91bdfbecc9e94efat.jpg)

第一次在Mac上绘图，这就当做本项目的吉祥物吧～

人类的创造从来没有离开大自然带给我们的启发，而无论是灰度发布，还是A/B Testing，早在千年以前，大自然早有绝佳的解决方案。因此我以‘Darwin's finches’作为原型，手工绘制了这张图，向伟大的大自然和达尔文《物种起源》致敬。

> Author: 顾鲍尔     
> Date： 2015.12.23 绘


