# Copyright 2014 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing fortran installation and cleanup functions."""


def GetLibPath(vm):
  """Get fortran library path."""
  out, _ = vm.RemoteCommand('find /usr/lib/ | grep fortran.a')
  return out[:-1]


def YumInstall(vm):
  """Installs the fortran package on the VM."""
  vm.InstallPackages('gcc-gfortran libgfortran')


def AptInstall(vm):
  """Installs the fortan package on the VM."""
  vm.InstallPackages('gfortran')
