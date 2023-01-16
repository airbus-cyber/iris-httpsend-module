import subprocess


class DockerCompose:

    def __init__(self, docker_compose_path):
        self._docker_compose_path = docker_compose_path

    # TODO: investigate why this does not seem to be working: subprocess.run(['docker-compose', '--file', _DOCKER_COMPOSE_PATH, 'up', '--detach'])
    def start(self):
        subprocess.run(['docker-compose', 'up', '--detach'], cwd=self._docker_compose_path)

    def stop(self):
        subprocess.run(['docker-compose', 'down'], cwd=self._docker_compose_path)
