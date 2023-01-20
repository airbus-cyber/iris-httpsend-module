#  Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import subprocess


class DockerCompose:

    def __init__(self, docker_compose_path):
        self._docker_compose_path = docker_compose_path

    # TODO: investigate why this does not seem to be working: subprocess.run(['docker-compose', '--file', _DOCKER_COMPOSE_PATH, 'up', '--detach'])
    def start(self):
        subprocess.run(['docker-compose', 'up', '--detach'], cwd=self._docker_compose_path)

    def stop(self):
        subprocess.run(['docker-compose', 'down'], cwd=self._docker_compose_path)
        subprocess.run(['docker', 'volume', 'prune', '--force'])
