import uuid

import requests

from config import LOCAL_TMP_PATH
from utils.regex_helper import is_url_format


class ContainerExecuor(object):
    def __init__(self, input_string, script_type):
        if is_url_format(input_string):
            req = requests.get(url=input_string)
            # 保存文件并解压
        else:
            filename = LOCAL_TMP_PATH + str(uuid.uuid4())
            print(filename)