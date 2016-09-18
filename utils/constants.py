class BashScriptType(object):
    PYTHON2 = 1
    HADOOP = 2


BashScripts = {
    BashScriptType.PYTHON2: './python2.py',
    BashScriptType.HADOOP: './hadoop.sh'
}
