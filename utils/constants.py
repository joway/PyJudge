class ExecScriptType(object):
    PYTHON2 = 1
    HADOOP = 2


ExecScripts = {
    ExecScriptType.PYTHON2: './python2.py',
    ExecScriptType.HADOOP: './hadoop.sh'
}

IMAGE_MAPPER = {
    ExecScriptType.PYTHON2: 'joway/judge',
    ExecScriptType.HADOOP: 'joway/hadoop'
}
