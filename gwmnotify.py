"""Warn Me GUI Notification Dialog

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
#  2.0 (2019-10-13): integration in Warn Me 2.0
#  1.0-portable (2014-03-14):  first version


import os
import sys

from tkinter import *
from tkinter import ttk

from wmtext import WARNME_NAME


#------------------------------------------------------------------------------
class NotifyDialog(Toplevel):
    '''Notification dialog for Warn Me program.
    '''

    #--------------------------------------------------------------------------
    def __init__(self, parent, message):

        Toplevel.__init__(self, parent)
        self.title(WARNME_NAME)

        # make modal
        self.transient(parent)
        self.grab_set()

        close = ttk.Button(self, text=message, command=self.onClose)
        close.grid(sticky=(W,N,E,S))
        close.focus()

        self.bind('<Return>', self.onClose)

        self.resizable(FALSE, FALSE)


    #--------------------------------------------------------------------------
    def onClose(self, *args):
        self.destroy()

