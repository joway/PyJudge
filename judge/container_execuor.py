import os
import uuid

import requests

from config import VOLUME_INPUT, VOLUME_OUTPUT, DEFAULT_OUTPUT_FILENAME, LOCAL_INPUT, LOCAL_OUTPUT
from utils.constants import ExecScriptType, ExecScripts, IMAGE_MAPPER
from utils.docker_client import DockerClient
from utils.regex_helper import is_url_format


class ContainerExecuor(object):
    def __init__(self):
        self.client = DockerClient()
        self.volume_input = VOLUME_INPUT
        self.volume_output = VOLUME_OUTPUT

    def exec(self, uid, input_string, script_type):
        uuid_dir, filename = self.process_input_string(uid, input_string)

        if script_type == ExecScriptType.PYTHON2:
            script = ExecScripts[ExecScriptType.PYTHON2]
            self.client.run_container(image=IMAGE_MAPPER[ExecScriptType.PYTHON2],
                                      command='python %s %s %s' %
                                              (script,
                                               self.volume_input + uuid_dir + filename,
                                               self.volume_output + uuid_dir + DEFAULT_OUTPUT_FILENAME),
                                      volume_binds=[
                                          LOCAL_INPUT + ':/input/:rw',
                                          LOCAL_OUTPUT + ':/output/:rw'])
        elif script_type == ExecScriptType.HADOOP:
            script = ExecScripts[ExecScriptType.PYTHON2]
            self.client.run_container(image=IMAGE_MAPPER[ExecScriptType.HADOOP],
                                      command='')

    def process_input_string(self, uid, input_string):
        uuid_dir = uid + '/'
        local_input_dir = LOCAL_INPUT + uuid_dir
        local_output_dir = LOCAL_OUTPUT + uuid_dir
        os.makedirs(local_input_dir)
        os.makedirs(local_output_dir)
        if is_url_format(input_string):
            # only support for rar file
            filename = 'input.rar'
            req = requests.get(url=input_string)
            # 保存文件并解压到 volume_dir
            file_content = req.content
        else:
            filename = 'input.txt'
            file_content = input_string
        with open(local_input_dir + filename, 'w') as file:
            file.write(file_content)

        return uuid_dir, filename
