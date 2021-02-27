#!/usr/bin/python3

"""Warn Me notify-send interface

Timed notification program
(C) 2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

__version__ = '2.1'
__date__ = '2021-02-27'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


#------------------------------------------------------------------------------
# Changes history:
#  2.1 (2021-02-27): publishing in GitHub
#  2.0 (2019-10-13): first version


import argparse
import subprocess

from wmtext import WARNME_VERSION, WARNME_SHORT_COPYRIGHT, WARNME_NAME
from wmtext import _


parser = argparse.ArgumentParser(description=WARNME_NAME + \
                                             ' ' +  WARNME_VERSION)

parser.add_argument("text", type=str,
                    help=_('Notification text.'))

parser.add_argument("-r", "--repeat", type=int, default=0,
                    metavar=_('MINUTES'), help=_('repeat interval.'))

args = parser.parse_args()

if args.repeat:
    from wmat import setAlarmFromNow
    setAlarmFromNow(args.repeat, args.text, args.repeat)
    
subprocess.call(('notify-send', WARNME_NAME, args.text))
