import subprocess
import uuid

from config import LOCAL_TMP_PATH, CONTAINER_NAME, CODE_TMP_DIR
from dockerclient.docker_client import DockerClient


class Judge(object):
    def __init__(self):
        self.tmp_path = LOCAL_TMP_PATH
        self.suffix_map = {
            'python': 'py',
            'c': 'c'
        }
        self.build_cmd = {
            'python': 'python',
            'c': 'gcc %s -o %s -Wall -lm -O2 -std=c99'
        }
        self.docker = DockerClient()

    def save_file(self, language: str, content):
        filename = self.tmp_path + str(uuid.uuid1()) + '.' + \
                   self.suffix_map.get(language)
        with open(filename, "w") as fh:
            fh.write(content)
        return filename

    def judge_python(self, segment):
        filename = self.save_file('python', segment)
        child = subprocess.Popen(["python", filename], stdout=subprocess.PIPE)
        return child.communicate()

    def judge_python_docker(self, segment):
        filename = self.save_file('python', segment)
        return self.docker.exec_container(CONTAINER_NAME,
                                          'python ' + CODE_TMP_DIR + filename)

    def judge_c(self, segment):
        filename = self.save_file('c', segment)
        child = subprocess.Popen(((self.build_cmd.get('c')) % (filename, filename[:-2])).split(" "),
                                 stdout=subprocess.PIPE)
        child.communicate()
        child_exe = subprocess.Popen([filename[:-2]],
                                     stdout=subprocess.PIPE)
        return child_exe.communicate()

