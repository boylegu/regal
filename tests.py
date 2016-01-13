from unittest import TestCase

from regal import BaseInfo
from regal.grouping import GroupAlgorithm
from regal.check_interface import AlgorithmABC


# Run Method: python -m unittest -v tests.py
class TestBaseInfoInitial(TestCase):
    def test_empty_info(self):
        ab = BaseInfo('', '', '')
        with self.assertRaises(AttributeError):
            ab.grouping()

    def test_empty_info_version_host_isdict(self):
        ab = BaseInfo({}, '', '')
        self.assertIsNotNone(ab.grouping())

    def test_info_errortype(self):
        ab = BaseInfo({}, '1', 'sds')
        self.assertIsNotNone(ab.grouping())


class TestGroupingResult(TestCase):
    ver = {
        'ver1': '1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4,5.1.1.1,6.2.2.2,7.3.3.3,8.4.4.4'}
    combine_num = 4

    def test_combine_num(self):
        ab = BaseInfo(
            self.ver,
            self.combine_num
        )
        instance_combine_num = ab.grouping().result[0][1]
        self.assertEqual(len(instance_combine_num[1:-1][0]), self.combine_num)

    def test_schedule_num(self):
        schedule_num = 2
        ab = BaseInfo(self.ver, self.combine_num, schedule_num)
        instance_combine_num = ab.grouping().result[0][1]
        self.assertEqual(len(instance_combine_num[0][0].split(',')), schedule_num)


class TestInstance(TestCase):
    def test_algorithm_instance(self):
        self.assertIsInstance(GroupAlgorithm(), AlgorithmABC)
