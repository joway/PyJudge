from sidomo import Container

with Container('ubuntu:14.04') as c:
    for line in c.run('bash -c "echo hello from; echo the other side;"'):
        print(line)
