import requests
import ujson
import time

host = 'http://zmky.uthtest.com:61818'
#proxy_dict = { "http": "http://localhost:8080/" }
proxy_dict = { }

def get_login(username, password):
    log_url = '{}{}'.format(host, '/account/loginPost?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    
    login_data = {
        "LoginName":username,
        "EncryptPwd":password,
        "isRemember":"no2",
        "TokenKey":"",
        "refUrl":"/home/index","LoginType":"2"
    }
    
    login_data_json = ujson.dumps(login_data)
    session = requests.Session()
    content = session.post(url=log_url, data=login_data_json, headers=header_base, proxies=proxy_dict)
    print("{} 已登录".format(username))
    return ( session, content ) 

def checktmpfiletime(session):
    post_url = '{}{}'.format(host, '/translatenologin/checktmpfiletime?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
            "{}"
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def checktmpfile(session, filename):
    post_url = '{}{}'.format(host, '/translatenologin/checktmpfile?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "ta": "1",
        "name": filename 
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def file_upload(session, filename):
    post_url = '{}{}'.format(host, "/translatenologin/upload")
    header_base = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "id": "WU_FILE_0",
        "name": filename,
        "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "lastModifiedDate": "Tue Jun 02 2020 21:14:04 GMT+0800 (China Standard Time)"
    }
    
    files = {
        "file": open(filename, 'rb')
    }
    
    content = session.post(url=post_url, data=post_data, headers=header_base, files=files, proxies=proxy_dict)
    return content

def createflow(session, Id):
    post_url = '{}{}'.format(host, '/translate/createflow?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "FlowName":"FileVerify",
        "FlowModel":{
            "FileList":[Id],
            "SrcLanguage": "1",
            "TgtLanguage": ["2"],
            "contrast": "0",
            "isSendEmail": 0,
            "TranslateType": "verify",
            "IsConvert": False
        }
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def getprogres(session, result_Id):
    post_url = '{}{}'.format(host, '/translate/getprogres?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "Id": result_Id
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content


def verifyfilesresult(session, result_Id):
    post_url = '{}{}'.format(host, '/translate/verifyfilesresult?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "Id": result_Id
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def addproject(session, file_id):
    post_url = '{}{}'.format(host, '/translate/addproject?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "FileList": [ file_id ],
        "SrcLanguage": "1",
        "TgtLanguage": ["2"],
        "contrast": "0",
        "isSendEmail": 0,
        "TranslateType": "file",
        "IsConvert": False
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def createflow_two(session, file_id, project_data):
    post_url = '{}{}'.format(host, '/translate/createflow?_ajax=1')
    header_base = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    post_data = {
        "FlowName":"TranslateRestore",
        "Highlighting":0,
        "ProjectModel": {
            "FileList": [ file_id ],
            "SrcLanguage": "1",
            "TgtLanguage": ["2"],
            "contrast": "0",
            "isSendEmail": 0,
            "TranslateType": "file",
            "IsConvert": False
        },
        "ProjectData": project_data
    }
    post_data_json = ujson.dumps(post_data)
    content = session.post(url=post_url, data=post_data_json, headers=header_base, proxies=proxy_dict)
    return content

def projectdownload(session, project_id):
    post_url = '{}{}'.format(host, '/translate/projectdownload/?projectId={}'.format(project_id))
    header_base = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    }
    content = session.get(url=post_url, headers=header_base, proxies=proxy_dict)
    return content


def task_all(taskname, username, password, filename):
    #host = 'http://zmky.uthtest.com:61818' 
    #proxy_dict = { "http": "http://localhost:8080/" }
    session, get_login_result = get_login(username=username, password=password)
    checktmpfiletime_result = checktmpfiletime(session)
    checktmpfiletime_result_json = ujson.loads(checktmpfiletime_result.text)
    checktmpfile_result = checktmpfile(session, filename)
    checktmpfile_result_json = ujson.loads(checktmpfile_result.text)
    file_upload_result = file_upload(session, filename=filename)
    Id = ujson.loads(file_upload_result.text)["Obj"]["Id"]
    createflow_result = createflow(session, Id=Id)
    result_Id = ujson.loads(createflow_result.text)["Obj"]["Result"]
    
    while True: 
        getprogres_result = getprogres(session, result_Id=result_Id)
        the_rate = ujson.loads(getprogres_result.text)["Obj"]["Rate"]
        print("{} 文件处理当前进度为: {}%".format(taskname, the_rate))
        if the_rate == 100:
            break
        else:
            time.sleep(1)

    verifyfilesresult_result = verifyfilesresult(session, result_Id=result_Id)
    file_id = ujson.loads(ujson.loads(verifyfilesresult_result.text)["Obj"]["FlowResults"]["UTHQueue_VerifyQueue"])["VerificationOuts"][0]["FileId"]

    addproject_result = addproject(session, file_id=file_id)
    project_data = ujson.loads(addproject_result.text)["Obj"]

    createflow_two_result = createflow_two(session, file_id=file_id, project_data=project_data)

    while True: 
        tt = getprogres(session, result_Id=result_Id)
        the_rate = ujson.loads(tt.text)["Obj"]["Rate"]
        print("{} 正式处理进度为: {}%".format(taskname, the_rate))
        if the_rate == 100:
            break
        else:
            time.sleep(1)

    project_id = project_data["Project"]["Id"]
    project_download_result = projectdownload(session, project_id=project_id )

    if project_download_result.status_code == 200:
        print("{} 处理结束".format(taskname))
    else:

        print("{}下载出错, 状态码为{}".format(taskname, project_download_result.status_code))


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if __name__ == "__main__":
    username_list = [ 'yaliceshi{:02d}'.format(num) for num in range(1, 51) ]
    password = "123456"
    filename = "B0000076_zs_焦油.docx"

    with ThreadPoolExecutor(max_workers=10) as executor:
    #with ProcessPoolExecutor(max_workers=35) as executor:
        for username in username_list:
            future = executor.submit(fn=task_all, 
                                    taskname=username, 
                                    username=username, 
                                    password=password, 
                                    filename=filename  )
    future.result()

