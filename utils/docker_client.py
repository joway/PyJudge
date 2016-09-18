from io import BytesIO

from docker import Client


class DockerClient(object):
    def __init__(self):
        self.client = Client(base_url='unix://var/run/docker.sock')

    def build_images(self, dockerfile: str, tag: str):
        with open(dockerfile) as file:
            dkfile = BytesIO(file.read().encode('utf-8'))
        response = [line for line in self.client.build(
            fileobj=dkfile, rm=True, tag=tag)]
        return response

    def run_container(self, image, mem_limit=None, volume_binds: list = None, command=None):
        container = self.client.create_container(image=image,
                                                 host_config=self.client.create_host_config(
                                                     binds=volume_binds, mem_limit=mem_limit), command=command)
        self.client.start(container)
        print(container)
        print(self.client.logs(container))
        # self.client.remove_container(container)

    def exec_container(self, container, cmd):
        container_id = self.client.exec_create(container, cmd)['Id']
        return self.client.exec_start(container_id)
