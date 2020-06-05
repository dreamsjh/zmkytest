import unittest
import ujson
import time
import datetime
from zmkytest import (  host, 
                        proxy_dict,
                        get_login,
                        checktmpfiletime,
                        checktmpfile,
                        file_upload,
                        createflow,
                        getprogres,
                        verifyfilesresult,
                        addproject, 
                        createflow_two,
                        projectdownload
)
                        
                        

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

    @classmethod
    def setUpClass(cls):
        cls.session = None
        cls.username = ''
        cls.password = ''
        cls.filename = ''

    def print_request_resonse(self, content, skip=None):
        printtask = { 'Req_h', 'Req_b', 'Res_h', 'Res_b' }
        if skip is not None:
            printtask =  printtask - skip
        if 'Req_h' in printtask:
            request_headers = content.request.headers
            print("Request Headers:\n {}".format(request_headers))
        if 'Req_b' in printtask:
            request_body = ujson.loads(content.request.body)
            print("Request Body:\n {}".format(request_body))
        if 'Res_h' in printtask:
            response_headers = content.headers
            print("Response Headers:\n {}".format(response_headers))
        if 'Res_b' in printtask:
            response_body = ujson.loads(content.text)
            print("Response Body:\n {}".format(response_body))

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    def test_a_login(self):
        """Test Login"""
        print(self.get_time())
        self.username, self.password, TestMathFunc.filename = self.param
        TestMathFunc.taskname = '{}'.format(self.username)
        session, content = get_login(username=self.username, password=self.password)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.session =  session 
        TestMathFunc.session =  session 
        self.print_request_resonse(content)
        self.assertEqual(result, None)   

    def test_b_checktmpfiletime(self):
        """Test checktmpfiletime"""
        content = checktmpfiletime(self.session)
        result = ujson.loads(content.text)["Code"]
        self.print_request_resonse(content)
        self.assertEqual(result, 1)

    def test_c_checktmpfile(self):
        """Test checktmpfile"""
        content = checktmpfile(TestMathFunc.session, filename=TestMathFunc.filename)
        result = ujson.loads(content.text)["Code"]
        self.print_request_resonse(content)
        self.assertEqual(result, 1)

    def test_d_fileupload(self):
        """Test fileupload"""
        content = file_upload(TestMathFunc.session, filename=TestMathFunc.filename)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.print_request_resonse(content, skip={'Req_b'})
        self.assertEqual(result, None)
        TestMathFunc.Id = ujson.loads(content.text)["Obj"]["Id"]

    def test_e_createflow(self):
        """Test createflow"""
        content = createflow(TestMathFunc.session, Id=TestMathFunc.Id)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.print_request_resonse(content)
        TestMathFunc.result_Id = ujson.loads(content.text)["Obj"]["Result"]
        self.assertEqual(result, None)

    def test_f_getrpogres(self):
        """Test createflow"""
        while True: 
            getprogres_result = getprogres(TestMathFunc.session, result_Id=TestMathFunc.result_Id)
            the_rate = ujson.loads(getprogres_result.text)["Obj"]["Rate"]
            print("{} 文件处理当前进度为: {}%".format(TestMathFunc.taskname, the_rate))
            if the_rate == 100:
                break
            else:
                time.sleep(1)
        self.assertEqual(the_rate, 100)

    def test_g_verifyfilesresult(self):
        """Test verifyfilesresult"""
        content = verifyfilesresult(TestMathFunc.session, result_Id=TestMathFunc.result_Id)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.print_request_resonse(content)
        TestMathFunc.file_id = ujson.loads(ujson.loads(content.text)["Obj"]["FlowResults"]["UTHQueue_VerifyQueue"])["VerificationOuts"][0]["FileId"]
        self.assertEqual(result, None)
        
    def test_h_addproject(self):
        """Test addproject"""
        content = addproject(TestMathFunc.session, file_id=TestMathFunc.file_id)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.print_request_resonse(content)
        TestMathFunc.project_data = ujson.loads(content.text)["Obj"]
        self.assertEqual(result, None)

    def test_i_createflow_two(self):
        """Test createflow_two"""
        content = createflow_two(TestMathFunc.session, file_id=TestMathFunc.file_id,
                                 project_data=TestMathFunc.project_data)
        self.print_request_resonse(content)
        result = ujson.loads(content.text)["Obj"]["ErrorResult"]
        self.assertEqual(result, None)

    def test_j_getrpogres(self):
        """Test getprogres2"""
        while True: 
            getprogres_result = getprogres(TestMathFunc.session, result_Id=TestMathFunc.result_Id)
            the_rate = ujson.loads(getprogres_result.text)["Obj"]["Rate"]
            print("{} 正式处理当前进度为: {}%".format(TestMathFunc.taskname, the_rate))
            if the_rate == 100:
                break
            else:
                time.sleep(1)
        self.assertEqual(the_rate, 100)   

    def test_k_projectdownload(self):
        """Test projectdownload"""
        TestMathFunc.project_id = TestMathFunc.project_data["Project"]["Id"]
        result = projectdownload(TestMathFunc.session, project_id=TestMathFunc.project_id )
        self.print_request_resonse(result, skip={'Req_b', 'Res_b'})
        status_code = result.status_code
        self.assertEqual(status_code, 200)
        print("下载结束") 



