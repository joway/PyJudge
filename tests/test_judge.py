from unittest import TestCase

from judge.judge import Judge


class JudgeTestCase(TestCase):
    def setUp(self):
        self.python_segment = self.readfile('../cases/hello.py')

        self.c_segment = self.readfile('../cases/hello.c')

        self.assert_data = b'hello world\n'
        self.judge = Judge()

    def readfile(self, filename):
        with open(filename, 'r') as fi:
            return fi.read()

    def test_judge_python(self):
        self.assertEquals(self.judge.judge_python(segment=self.python_segment)[0],
                          self.assert_data)

    def test_judge_python_docker(self):
        self.assertEquals(self.judge.judge_python_docker(segment=self.python_segment),
                          self.assert_data)

    def test_judge_c(self):
        self.assertEquals(self.judge.judge_c(segment=self.c_segment)[0],
                          self.assert_data)
