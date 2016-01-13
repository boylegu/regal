# coding: utf-8
import abc

from six import with_metaclass


class AlgorithmABC(with_metaclass(abc.ABCMeta, object)):
    """
    实现了一套简单的虚拟接口检查类, 主要用于检测'发布算法器'的各项接口是否存在.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        重写了instance方法, 用于实现一个虚拟接口;
        :param subclass: 被检测的接口类
        :return:

        其中__mro__方法主要是把所有的subclass和base类的所有属性都遍历出来,并放在一个容器中;
        然后通过定义好的抽象接口属性name,与其进行比对,最终返回结果.
        """
        if cls is AlgorithmABC:
            methods = ("initialize", "calculate", "final")
            all_attribute_dict = [all_attribute.__dict__ for all_attribute in subclass.__mro__][0]
            if all(method in all_attribute_dict for method in methods):
                return True
        return NotImplemented
