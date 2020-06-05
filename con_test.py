from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import unittest
from Test_Model import TestMathFunc, ParametrizedTestCase
from BeautifulReport import BeautifulReport as bf


if __name__ == '__main__':

    def test_case(param):
        suite = unittest.TestSuite()
        suite.addTest(ParametrizedTestCase.parametrize(TestMathFunc, param=param))
        unittest.TextTestRunner(verbosity=2).run(suite)

    password = "123456"
    filename = "B0000076_zs_焦油.docx"
    param_list = [ ('yaliceshi{:02d}'.format(num), 
                    password, 
                    filename) for num in range(1, 2) ]
    #with ThreadPoolExecutor(max_workers=10) as executor:
    with ProcessPoolExecutor(max_workers=10) as executor:
        for param in param_list:
            future = executor.submit(fn=test_case,
                                     param = param )
    future.result()

    