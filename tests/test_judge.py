from judge import Judge

python_segment = """
print("123");
"""

c_segment = """
#include <stdio.h>
int main(){
    printf("%d", 123);
}

"""
judge = Judge()
print(judge.judge_python(segment=python_segment))
print(judge.judge_c(segment=c_segment))
