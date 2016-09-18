import os
from unittest import TestCase

from utils.docker_client import DockerClient


class DockerTestCase(TestCase):
    def setUp(self):
        self.client = DockerClient()
        self.path = os.getcwd() + '/'

    def test_build_images(self):
        self.client.build_images('./TestDockerfile', 'judge')

    def test_run_container(self):
        self.client.run_container('judge', binds=[self.path + ":/code"])

    def test_exec_container(self):
        self.client.exec_container('ubuntu:14.04',
                                   'cases -c "echo hello from; echo the other side;"')
