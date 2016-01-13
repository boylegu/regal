# coding: utf-8
from six.moves import zip


class Format(object):
    """
    专用于处理各种数据的格式化,目前还比较简单;之后有时间会加入json的支持-_-
    """

    def __init__(self, result_list):
        self.result = result_list

    def iter_dict(self):
        for i in zip(self.result):
            yield {
                i[0][0]: [','.join(ip) for ip in i[0][1]]
            }
