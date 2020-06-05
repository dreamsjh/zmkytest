import unittest
from Test_Model import TestMathFunc, ParametrizedTestCase
from BeautifulReport import BeautifulReport as bf


if __name__ == '__main__':

    def test_case(param):
        suite = unittest.TestSuite()
        suite.addTest(ParametrizedTestCase.parametrize(TestMathFunc, param=param))
        unittest.TextTestRunner(verbosity=2)
        run = bf(suite)
        run.report(filename='test',description='芝麻快译测试环境单用户功能测试')

    username = "yaliceshi01"
    password = "123456"
    filename = "B0000076_zs_焦油.docx"
    param = ( username, password, filename) 

    test_case(param=param)
