# This file is part of hello-copr <https://pagure.io/copr-tito-quickdoc>.
# Copyright (C) 2020 Christopher Engelhard
#
# hello-copr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hello-copr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hello-copr.  If not, see <http://www.gnu.org/licenses/>.

from colorama import init

from hello_copr.colors import red, green, normal

init()

def hello():
    arg = red("Hello! ") + green("I'm the hello-copr demo program. ") + normal("I don't do much.")
    return arg

def main():
    print(hello())

if __name__ == "__main__":
    main()
