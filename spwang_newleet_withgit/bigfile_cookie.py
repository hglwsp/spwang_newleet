import requests
import uuid
import random
import re
import string
import csv
import time
import concurrent.futures

def generate_traceid():
    # 生成一个UUID版本4（随机生成的UUID）
    trace_id = uuid.uuid4()
    return trace_id

# 一键生成8位requestid
def generate_random_string():
    # 定义可能的字符集
    length = 8
    characters = string.ascii_letters + string.digits
    # 从字符集中随机选择指定数量的字符
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

class cookie_get:
    def __init__(self):
        self.s = requests.session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.duomian.com',
            'Referer': 'https://www.duomian.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Cookie':'XSRF-TOKEN=nFnDb_5FRquon3in07KkjQ; __gc_id=29b284fbdc364bb494a5bbe6f9adcd3c; __uuid=1667468491441.86; __session_seq=1; __uv_seq=1; __tlog=1667468491453.18%7C00000000%7C00000000%7C00000000%7C00000000',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'X-Client-Type': 'web',
            'X-Fscp-Fe-Version': '',
            'X-Fscp-Std-Info': '{"client_id": "40242"}',
            'X-Fscp-Trace-Id': 'f7edfaab-b1b5-494e-a7b1-5473cacb633b',
            'X-Fscp-Version': '1.1',
            'X-Requested-With': 'XMLHttpRequest',
            'X-XSRF-TOKEN': '-Uq3nq1_Tmeg6lhuown1BA',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

    def print_red(self,text):
        print("\033[31m" + text + "\033[0m")

        # 公共请求
    def send_req(self, method, url, data=None, json=None, headers=None):
        if headers == None:
            headers = self.headers
        if method.upper() == 'GET':
            r = self.s.request(method=method, url=url, headers=headers, params=data)
        else:
            if json:
                r = self.s.request(method=method, url=url, headers=headers, json=json)
            else:
                r = self.s.request(method=method, url=url, headers=headers, data=data)
        return r


    def login(self, tel, sms,trace_id):
        url = "https://api-passport.duomian.com/api/com.liepin.passport.account.tel-sms-login?traceId={}".format(trace_id)
        payload = f'businessId=11004002123230023123232&tel={tel}&smsCode={sms}'
        response = self.send_req("POST", url, data=payload)
        response_headers = response.headers
        flag = response.json()['flag']
        if flag == 1:
            # print("登录成功：" + response.text)
            # print("登录成功header:" ,response_headers)
            return response_headers
        else:
            self.print_red("登录失败：" + response.text)

def process_login(i):
    wsp_trace = str(generate_traceid())
    phone = str(18399992001 + i)
    return c_i.login(phone, '230701', wsp_trace)

# 记录开始时间
start_time = time.time()
c_i = cookie_get()
res = []

# 使用 ThreadPoolExecutor 进行多线程执行
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # 提交任务
    futures = [executor.submit(process_login, i) for i in range(1000)]

    # 收集结果
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        res.append(result)

# c_i = cookie_get()
# res = []
# for i in range(0,1000):
#     wsp_trace = str(generate_traceid())
#     res.append(c_i.login(str(12999992001+i), '900702', wsp_trace))
    # print("header:",res)
#########################优雅分开###########################
# 正则获取cookie
##########################################################
wsp_auth = []
for i, item in enumerate(res):
    match = re.search(r'duomian_auth=([^;]+);Max-Age', str(res[i]))
    if match:
        auth_value = match.group(1)
        wsp_auth.append(auth_value)
        print(f"第{i+1}个已完成正则")
        # print(f"duomian_auth value: {auth_value}")
    else:
        print("No match found.")
##########################################################


#########################优雅分开###########################
# 写入文件
##########################################################
with open('llzzmm8.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 逐行写入 auth_values 中的每个值
    for index, auth_value in enumerate(wsp_auth, start=1):
        writer.writerow([auth_value])
        print(f"第{index}个已完成写入")

# 文件完成
print("文件写入完成")
# 记录结束时间
end_time = time.time()
# 计算运行时间
elapsed_time = end_time - start_time
print("CSV file created successfully.")
print(f"Elapsed time: {elapsed_time:.6f} seconds")
