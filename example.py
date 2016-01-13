# coding: utf-8
# regal v1.1 example
from regal import BaseInfo


ab = BaseInfo(
    version_host={
        'test-app-1.0.0-SNAPSHOT-201512191829.war': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4,5.1.1.1,6.2.2.2,7.3.3.3,8.4.4.4'},
    combine=4,  # 每组四台
    schedule=3  # groupA组 分三台
)

cc = ab.grouping()
print(cc.result)
for i in cc.iter_dict():
    print(i)


# 多版本支持
ab = BaseInfo(
    version_host={'ver1': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4',
                  'ver2': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4',
                  'ver3': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4',
                  'ver4': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4', },
    combine=3,
    # schedule=2   # groupA组 分三台
)

cc = ab.grouping(priority_name='ver2')  # priority_name 多版本的情况下可以作为优先级策略
print(cc.result)
for i in cc.iter_dict():
    print(i)


# 以上都只是例子, 事实上服务器可以更多,甚至可以非常多; 请随意~~
