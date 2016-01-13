# coding: utf-8
from six import iteritems

from regal.check_interface import AlgorithmABC
from regal.grouping import GroupAlgorithm
from regal.format import Format


class BaseInfo(object):
    """
    收集初始化信息的类
    """

    def __init__(self, version_host, combine=None, schedule=None):
        self.host_version = version_host
        self.schedule = 1 if not schedule else schedule
        self.combine = 1 if not combine else combine

    def __add_info(self):
        try:
            version_group = [(version, [hostname]) for version, hostname in iteritems(self.host_version)]
        except:
            raise AttributeError("ERROR! The information is wrong")
        return version_group

    def grouping(self, priority_name=None):
        control = Manager(
            base_info=self.__add_info(),
            grouping_algorithm=GroupAlgorithm(),  # Bridge Pattern
        )
        return control.grouping(self.combine, self.schedule, priority_name)


class Manager(object):
    """
    一个class hierarchy, 作为具体分组实现的方式
    """

    def __init__(self, base_info, grouping_algorithm):
        self.base_info = base_info
        if not isinstance(grouping_algorithm, AlgorithmABC):
            raise TypeError(
                "Expected object of type Algorithm, got {}".format(type(grouping_algorithm).__name__))
        self.__algorithm = grouping_algorithm

    def grouping(self, combine, schedule, priority_name):
        self.__algorithm.initialize(self.base_info)
        self.__algorithm.calculate(combine, schedule)
        result = self.__algorithm.final(priority_name)
        return Format(result)
