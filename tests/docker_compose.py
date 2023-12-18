# This file is part of IRIS HTTP Send Module.
#
# Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
# IRIS HTTP Send Module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# IRIS HTTP Send Module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with IRIS HTTP Send Module. If not, see <https://www.gnu.org/licenses/>.

import subprocess


class DockerCompose:

    def __init__(self, docker_compose_path):
        self._docker_compose_path = docker_compose_path

    # TODO: investigate why this does not seem to be working: subprocess.run(['docker-compose', '--file', _DOCKER_COMPOSE_PATH, 'up', '--detach'])
    def start(self):
        subprocess.run(['docker-compose', 'up', '--detach'], cwd=self._docker_compose_path)

    def extract_all_logs(self):
        return subprocess.check_output(['docker-compose', 'logs', '--no-color'], cwd=self._docker_compose_path, universal_newlines=True)

    def stop(self):
        subprocess.run(['docker-compose', 'down'], cwd=self._docker_compose_path)
        subprocess.run(['docker', 'volume', 'prune', '--force'])
