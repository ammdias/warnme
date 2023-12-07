"""Warn Me GUI information dialog

Timed notification program
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


from tkinter import *
from tkinter import ttk

from wmtext import WARNME_NAME
from wmtext import _


#------------------------------------------------------------------------------
class TextDialog(Toplevel):
    '''Text message dialog for Warn Me program.
    '''

    #--------------------------------------------------------------------------
    def __init__(self, parent, message):

        Toplevel.__init__(self, parent)
        self.title(WARNME_NAME)

        # make modal
        self.transient(parent)
        self.grab_set()

        t = Text(self) # width=80, height=24
        t.insert('1.0', message)

        vscroll = ttk.Scrollbar(self, orient=VERTICAL, command=t.yview)
        hscroll = ttk.Scrollbar(self, orient=HORIZONTAL, command=t.xview)
        t.configure(yscrollcommand=vscroll.set, xscrollcommand=hscroll.set,
                    state=DISABLED)

        t.grid(column=0, row=0, sticky=(W,N,E,S))
        vscroll.grid(column=1, row=0, sticky=(N,S))
        hscroll.grid(column=0, row=1, sticky=(W,E))

        close = ttk.Button(self, text=_("Close"), command=self.onClose)
        close.grid(column=0, row=2, padx=2, pady=5)
        close.focus()

        self.bind('<Return>', self.onClose)

        self.resizable(FALSE, FALSE)


    #--------------------------------------------------------------------------
    def onClose(self, *args):
        self.destroy()
