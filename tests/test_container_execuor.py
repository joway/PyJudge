from judge.container_execuor import ContainerExecuor
from utils.constants import BashScriptType

ce = ContainerExecuor()
ce.exec(input_string="""
prin
""", script_type=BashScriptType.PYTHON2)
