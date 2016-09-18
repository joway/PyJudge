import datetime
import uuid

from judge.container_execuor import ContainerExecuor
from utils.constants import ExecScriptType

ce = ContainerExecuor()
begin = datetime.datetime.now()
ce.exec(uid=str(uuid.uuid4()), input_string="""
print(10**1000)
""", script_type=ExecScriptType.PYTHON2)
end = datetime.datetime.now()

print((end - begin))
