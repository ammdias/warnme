#!/usr/bin/python3

"""Warn Me GUI

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
from tkinter import ttk, messagebox

from time import localtime
from threading import Timer, Lock, current_thread

from wmtext import *
from wmtext import _

from gwmtext import TextDialog
from gwmnotify import NotifyDialog


#------------------------------------------------------------------------------
class Warnme:
    '''Graphical User Interface for Warn Me program.
    '''
    ALARM_IN, ALARM_AT = 0, 1
    TEXT, REPEAT = 0, 1

    #--------------------------------------------------------------------------
    def __init__(self, win):
        self.win = win
        self.win.title(WARNME_NAME)
        self.win.option_add('*tearOff', FALSE)

        self.alarmInAtVar = IntVar()
        self.messageVar = StringVar()
        self.alarmTimersLock = Lock()
        # alarm lists
        self.alarmTimers = [] 
        self.alarmConfig = [] # (text, repeat)

        self.buildMenu()
        self.buildWidgets()
        self.win.resizable(FALSE, FALSE)

        self.win.bind('<Return>', self.onSetAlarm)

        # initial state
        self.alarmInAtVar.set(Warnme.ALARM_IN)
        self.messageVar.set(_('Standard notification'))


    #--------------------------------------------------------------------------
    def _deleteAlarm(self, idx):
        '''Remove alarm from every list.
        '''
        self.alarmTimers[idx].cancel()
        del self.alarmTimers[idx]
        del self.alarmConfig[idx]
        self.alarmListbox.delete(idx)

    
    #--------------------------------------------------------------------------
    def notify(self):
        '''Display message notification.
        '''
        with self.alarmTimersLock:
            idx = self.alarmTimers.index(current_thread())

            NotifyDialog(self.win, self.alarmConfig[idx][Warnme.TEXT])

            # check for alarm repetition
            if self.alarmConfig[idx][Warnme.REPEAT]:
                text, repeat = (self.alarmConfig[idx][Warnme.TEXT],
                                self.alarmConfig[idx][Warnme.REPEAT])
            else:
                repeat = False

            self._deleteAlarm(idx)

        if repeat:
            self._setAlarm(interval=repeat, text=text, repeat=repeat)


    #--------------------------------------------------------------------------
    def _setAlarm(self, hour=0, minute=0, interval=0, text='', repeat=0):
        '''Set new alarm.
        '''
        HOUR, MIN, SEC = 3, 4, 5
        now = localtime()

        if interval:
            interval = interval + now[MIN]
            hour, minute = (interval // 60 + now[HOUR]) % 24, interval % 60

        interval = hour * 3600 + minute * 60 \
                   - now[HOUR] * 3600 - now[MIN] * 60 - now[SEC]
        if interval < 0:
            interval += 86400

        timer = Timer(interval, self.notify)
        timer.start()

        with self.alarmTimersLock:
            self.alarmTimers.append(timer)
            self.alarmConfig.append((text, repeat))
            self.alarmListbox.insert(END,
                        '%02d:%02d %s%s' % \
                           (hour, minute, text,
                           (_(', repeat every %d minutes') % repeat)
                              if repeat else ""))


    #--------------------------------------------------------------------------
    def onSetAlarm(self, *args):
        '''Set new alarm.
        '''
        if self.alarmInAtVar.get() == Warnme.ALARM_IN:
            self._setAlarm(interval=int(self.timeSpin.get()),
                           text=self.messageVar.get(),
                           repeat=int(self.repeatSpin.get()))
        else:
            self._setAlarm(hour=int(self.hourSpin.get()),
                           minute=int(self.minuteSpin.get()),
                           text=self.messageVar.get(),
                           repeat=int(self.repeatSpin.get()))


    #--------------------------------------------------------------------------
    def onRemoveAlarm(self, *args):
        '''Remove selected alarms.
        '''
        with self.alarmTimersLock:
            while self.alarmListbox.curselection():
                idx = int(self.alarmListbox.curselection()[0])
                self._deleteAlarm(idx)


    #--------------------------------------------------------------------------
    def onAbout(self, *args):
        '''Show About dialog.
        '''
        messagebox.showinfo(message='{} {}'.format(WARNME_NAME, WARNME_VERSION),
                            detail='{}\n\n{}'.format(WARNME_SHORT_COPYRIGHT,
                                                     WARNME_WEBSITE),
                            title='{} {}'.format(_('About'), WARNME_NAME))


    #--------------------------------------------------------------------------
    def onManual(self, *args):
        '''Show Help dialog.
        '''
        self.infoDialog(WARNME_HELP)


    #--------------------------------------------------------------------------
    def onWarranty(self, *args):
        '''Show Warranty dialog.
        '''
        self.infoDialog('{} {}\n{}\n\n{}'.format(WARNME_NAME, WARNME_VERSION,
                                                 WARNME_SHORT_COPYRIGHT,
                                                 WARNME_WARRANTY))


    #--------------------------------------------------------------------------
    def onCopyright(self, *args):
        '''Show Copyright dialog.
        '''
        self.infoDialog('{} {}\n{}\n\n{}'.format(WARNME_NAME, WARNME_VERSION,
                                                 WARNME_SHORT_COPYRIGHT,
                                                 WARNME_COPYRIGHT))


    #--------------------------------------------------------------------------
    def onQuit(self, *args):
        '''Show Copyright dialog.
        '''
        self.win.destroy()


    #--------------------------------------------------------------------------
    def infoDialog(self, message):
        '''Build and show information dialog with title and message.
        '''
        self.win.wait_window(TextDialog(self.win, message))


    #--------------------------------------------------------------------------
    # validation functions
    def valTime(self, val):
        self.alarmInAtVar.set(Warnme.ALARM_IN)
        return val.isdigit() and 1 <= int(val) <= 999

    def valHours(self, val):
        self.alarmInAtVar.set(Warnme.ALARM_AT)
        return val.isdigit() and 0 <= int(val) <= 23

    def valMinutes(self, val):
        self.alarmInAtVar.set(Warnme.ALARM_AT)
        return val.isdigit() and 0 <= int(val) <= 59

    def valRepeat(self, val):
        return val.isdigit() and 0 <= int(val) <= 720

    def valMessage(self, val):
        self.setAlarmButton.state(['disabled' if val == '' else '!disabled'])
        return True


    #--------------------------------------------------------------------------
    def buildMenu(self):
        '''Create root window menu.
        '''
        menubar = Menu(self.win)
        self.win['menu'] = menubar
        helpMenu = Menu(menubar)
        lbl, pos = labelUnderline(_('_Help'))
        menubar.add_cascade(menu=helpMenu, label=lbl, underline=pos)


        lbl, pos = labelUnderline(_('_Manual'))
        helpMenu.add_command(label=lbl, accelerator=_('F1'),
                             command=self.onManual, underline=pos)

        helpMenu.add_separator()

        lbl, pos = labelUnderline(_('_About'))
        helpMenu.add_command(label=lbl, command=self.onAbout, underline=pos)

        lbl, pos = labelUnderline(_('_Warranty'))
        helpMenu.add_command(label=lbl, command=self.onWarranty,
                             underline=pos)

        lbl, pos = labelUnderline(_('_Copyright'))
        helpMenu.add_command(label=lbl, command=self.onCopyright,
                             underline=pos)

        helpMenu.add_separator()

        lbl, pos = labelUnderline(_('_Quit'))
        helpMenu.add_command(label=lbl, accelerator=_('CTRL+Q'),
                             command=self.onQuit, underline=pos)

        self.win.bind(_('<Control-Key-q>'), self.onQuit)
        self.win.bind(_('<Key-F1>'), self.onManual)


    #--------------------------------------------------------------------------
    def buildWidgets(self):
        '''Create widgets.
        '''
        frame = ttk.Frame(self.win, padding=5)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # alarm in
        b = ttk.Radiobutton(frame, text=_('Set alarm in'),
                            variable=self.alarmInAtVar, value=Warnme.ALARM_IN)
        b.grid(column=0, row=0, sticky=W, padx=2, pady=2)

        self.timeSpin = Spinbox(frame, from_=1, to=999, width=4,
                                validate='key', justify=RIGHT,
                                validatecommand=(frame.register(self.valTime),
                                                 '%P'),
                                command=lambda: \
                                        self.alarmInAtVar.set(Warnme.ALARM_IN))
        self.timeSpin.grid(column=1, row=0, sticky=W, padx=2, pady=2)

        b = ttk.Label(frame, text=_('minutes'))
        b.grid(column=3, row=0, columnspan=2, sticky=W, padx=2, pady=2)

        # alarm at
        b = ttk.Radiobutton(frame, text=_('Set alarm at'),
                            variable=self.alarmInAtVar, value=Warnme.ALARM_AT)
        b.grid(column=0, row=1, sticky=W, padx=2, pady=2)

        self.hourSpin = Spinbox(frame, from_=0, to=23, wrap=True, width=4,
                                validate='key', format='%02.0f', justify=RIGHT,
                                validatecommand=(frame.register(self.valHours),
                                                 '%P'),
                                command=lambda: \
                                        self.alarmInAtVar.set(Warnme.ALARM_AT))
        self.hourSpin.grid(column=1, row=1, sticky=W, padx=2, pady=2)

        ttk.Label(frame, text=':').grid(column=2, row=1, sticky=(W, E),
                                        pady=2)

        self.minuteSpin = Spinbox(frame, from_=0, to=59, wrap=True, width=4,
                                  validate='key', format='%02.0f',
                                  justify=RIGHT,
                                  validatecommand=( \
                                      frame.register(self.valMinutes), '%P'),
                                  command=lambda: \
                                          self.alarmInAtVar.set(Warnme.ALARM_AT))
        self.minuteSpin.grid(column=3, row=1, sticky=W, padx=2, pady=2)

        b = ttk.Label(frame, text=_('hours'))
        b.grid(column=4, row=1, sticky=W, padx=2, pady=2)

        # message
        b = ttk.Label(frame, text=_('Message:'))
        b.grid(column=0, row=2, sticky=E, padx=2, pady=2)

        b = ttk.Entry(frame, textvariable=self.messageVar,
                      validate='key',
                      validatecommand=( \
                          frame.register(self.valMessage), '%P'))
        b.grid(column=1, row=2, columnspan=5, sticky=(W, E), padx=2, pady=2)

        # repeat interval
        b = ttk.Label(frame, text=_('Repeat every'))
        b.grid(column=0, row=3, sticky=E, padx=2, pady=2)

        self.repeatSpin = Spinbox(frame, from_=0, to=720, wrap=True, width=4,
                                  validate='key', justify=RIGHT,
                                  validatecommand=( \
                                      frame.register(self.valRepeat), '%P'))
        self.repeatSpin.grid(column=1, row=3, sticky=W, padx=2, pady=2)

        b = ttk.Label(frame, text=_('minutes'))
        b.grid(column=3, row=3, sticky=E, padx=2, pady=2)

        # set alarm
        self.setAlarmButton = ttk.Button(frame, text=_('Set alarm'),
                                         command=self.onSetAlarm)
        self.setAlarmButton.grid(column=3, row=4, columnspan=3, sticky=E,
                                 padx=2, pady=2)

        b = ttk.Separator(frame, orient=HORIZONTAL)
        b.grid(column=0, row=5, columnspan=6, sticky=(W,E), pady=4)

        b = ttk.Label(frame, text=_('Pending alarms:'))
        b.grid(column=0, row=6, columnspan=6, sticky=W, padx=2, pady=2)

        # alarm list
        b = ttk.Scrollbar(frame, orient=VERTICAL)
        b.grid(column=5, row=7, sticky=(N,S), pady=2)

        self.alarmListbox = Listbox(frame, selectmode='extended',
                                    yscrollcommand=b.set)
        self.alarmListbox.grid(column=0, row=7, columnspan=5,
                               sticky=(N,W,E,S), pady=2)
        b['command'] = self.alarmListbox.yview

        # remove alarm
        b = ttk.Button(frame, text=_('Remove alarm'),
                       command=self.onRemoveAlarm)
        b.grid(column=3, row=8, columnspan=3, sticky=E, padx=2, pady=2)


#------------------------------------------------------------------------------
def gstart():
    '''display main window and run Warnme main loop
    '''
    try:
        win = Tk()
        gui = Warnme(win)
        win.mainloop()
    finally:
        # terminate all remaining threads
        for alm in gui.alarmTimers:
            alm.cancel()


if __name__ == '__main__':
    gstart()
