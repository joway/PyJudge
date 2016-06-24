from unittest import TestCase

from judge.judge import Judge


class JudgeTestCase(TestCase):
    def setUp(self):
        self.python_segment = """print("123");
        """

        self.c_segment = """
        #include <stdio.h>
        int main(){
            printf("%d", 123);
        }
        """
        self.judge = Judge()

    def test_judge_python(self):
        self.assertEquals(self.judge.judge_python(segment=self.python_segment)[0],
                          b'123\n')

    def test_judge_c(self):
        self.assertEquals(self.judge.judge_c(segment=self.c_segment)[0],
                          b'123')
