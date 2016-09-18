import subprocess

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

child = subprocess.Popen(['python', input_file],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
child.wait()
error = child.stderr.read()
output = error if error else child.stdout.read()
with open(output_file, 'w') as file:
    print(output.decode('UTF-8'))
    file.write(output.decode('UTF-8'))
