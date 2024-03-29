"""Warn Me

Timed notification program
Common Warn Me code
(C) 2012 António Manuel Dias

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


import sys 
from wmtext import _


#------------------------------------------------------------------------------
# common Warn Me functions

def error(message, quit=True):
    '''Print error message.
       quit: terminate program when True.'''
    print(_('Error:'), message, file=sys.stderr)
    if quit:
        sys.exit(1)


