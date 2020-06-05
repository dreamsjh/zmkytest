import unittest
import ujson
import time
import datetime
from zmkytest import get_login, host, proxy_dict

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
    inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        if param is not None:
            self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
        subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


class TestMathFunc(ParametrizedTestCase):

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    def test_add(self):
        """Test Login"""
        print(self.get_time())
        username, password = self.param
        session, content = get_login(username=username, password=password)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.assertEqual(result, None)


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
if __name__ == '__main__':

    def test_case(param):
        suite = unittest.TestSuite()
        suite.addTest(ParametrizedTestCase.parametrize(TestMathFunc, param=param))
        unittest.TextTestRunner(verbosity=1).run(suite)

    password = '123456'
    param_list = [ ('yaliceshi{:02d}'.format(num), password) for num in range(1, 51) ]
    
    with ThreadPoolExecutor(max_workers=1) as executor:
    #with ProcessPoolExecutor(max_workers=35) as executor:
        for param in param_list:
            future = executor.submit(fn=test_case,
                                     param = param )
    future.result()