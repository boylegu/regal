# coding: utf-8
from operator import contains

from six.moves import xrange


class GroupAlgorithm(object):
    """
    一个abstraction class,主要实现了分流算法的接口,不过代码应该还可以再一次深度优化;

    """
    base_hostlist = None
    host_list = None

    @classmethod
    def recursive_grouping(cls, hosts, combine, hostindex, init_host, base_hostlist):

        baselist = base_hostlist

        def grouping(hosts, combine, hostindex, init_host, init_n=0):
            try:
                f_count = init_n + 1  # 记录创建子列表的次数
                baselist[hostindex][1][0] = [init_host]
                baselist[hostindex][1].append(list())
                for i in xrange(combine):
                    baselist[hostindex][1][init_n + 1].append(hosts.pop())
            except IndexError:
                return 0
            else:
                return grouping(hosts, combine, hostindex, init_host, f_count)

        return grouping(hosts, combine, hostindex, init_host, init_n=0)

    def initialize(self, hostinfo):
        self.base_hostlist = list()
        self.host_list = [(i[0], ','.join(i[1]).split(',')) for i in hostinfo]
        return

    def calculate(self, combine, schedule):
        for infoindex, info in enumerate(self.host_list):
            self.base_hostlist.append((info[0], [[]]))
            # print ','.join(info[1][:2])
            hosts = info[1][schedule:]
            hosts.reverse()
            GroupAlgorithm.recursive_grouping(
                hosts=hosts, combine=combine, hostindex=infoindex,
                init_host=','.join(info[1][:schedule]), base_hostlist=self.base_hostlist)

            if not self.base_hostlist[infoindex][1][-1]:
                self.base_hostlist[infoindex][1].pop(-1)
        return

    def final(self, priority_name):
        base_hostlist = self.base_hostlist
        if priority_name:
            base_hostlist = sorted(
                base_hostlist, key=lambda x: contains(x[0], priority_name), reverse=True)
        return base_hostlist
