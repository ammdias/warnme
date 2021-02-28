#!/usr/bin/python3

"""Warn Me

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

__version__ = '2.2'
__date__ = '2021-02-28'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


#------------------------------------------------------------------------------
# Changes history:
#  2.2 (2021-02-28): changed directory of alarm list file, for multi-user use
#  2.1 (2021-02-27): publishing in GitHub
#  2.0 (2019-10-13): Complete rewrite using Tkinter interface
#                    from previous portable version (terminated)
#                    focus on terminal usage in Linux, using POSIX 'at'
#                      and freedesktop.org 'notify-send' utilities
#                    added possibility of recurrent alarms (repeat)
#
#  1.0.1 (2019-09-07): require correct GTK/Notify versions from GI library
#  1.0 (2014-02-23): Complete rewrite using GTK3, GObject and Python >= 3.3
#
#  0.7 (2012-02-22): added icon to notification
#  0.6 (2012-02-09): fixed time format problem in fmttm()
#                      reported by António Lima
#  0.5 (2012-02-05): added time format function: fmttm()
#                      some code clean up
#  0.4 (2012-02-02): changed notification summary to 'Warn Me'
#                    (requested by António Lima)
#  0.3 (2012-01-31): added zenity dialog, i18n, pt_PT locale
#                      and freedesktop.org menu and icons
#  0.2 (2012-01-26): added 'message in xx seconds' notification
#                    added error notifications
#                    added notification function: nwarn()


import sys
import argparse
import subprocess

from wmtext import WARNME_NAME, WARNME_VERSION, WARNME_SHORT_COPYRIGHT, \
                   WARNME_COPYRIGHT, WARNME_WARRANTY
from wmtext import _

from wmat import setAlarmFromNow, setAlarmAtTime, removeAlarm, listConfigAlarms   
from wmcommon import error


#------------------------------------------------------------------------------
# helper functions

def checkAt():
    '''Check if "at" is available.'''
    try:
        subprocess.check_call('atq', stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
    except:
        error(_("'at/atq/atrm' utilities not available."), False)
        return False

    return True


def checkNotify():
    '''Check if "notify-send" is available.'''
    try:
        subprocess.check_call(('notify-send', '--version'),
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
    except:
        error(_("'notify-send' utility not available."), False)
        return False

    return True



def arguments():
    '''Parse command line arguments.'''
    
    parser = argparse.ArgumentParser(description=
                                         WARNME_NAME + ' ' +  WARNME_VERSION)

    parser.add_argument("-a", "--at", type=str, default="", 
                        metavar=_('HH:MM'),
                        help=_('hour and minute for the warning.'))

    parser.add_argument("-i", "--in", type=int, default=0, dest='ain',
                        metavar= _('MINUTES'),
                        help=_('interval for the warning.'))

    parser.add_argument("-t", "--text", type=str,
                        default=_('Standard notification'),
                        help=_('Notification text.'))

    parser.add_argument("-r", "--repeat", type=int, default=0,
                        metavar=_('MINUTES'),
                        help=_('repeat interval.'))

    parser.add_argument("-l", "--list", action="store_true",
                        help=_('list set alarms.'))

    parser.add_argument("-d", "--delete", type=int, default=0,
                        metavar= _('ALARM'),
                        help=_('delete alarm by index.'))

    parser.add_argument("-g", "--gui", action="store_true",
                        help=_('launch graphical user interface.'))

    parser.add_argument("-c", "--copyright", action="store_true",
                        help=_('show copyright information.'))

    parser.add_argument("-w", "--warranty", action="store_true",
                        help= _('show warranty information.'))

    parser.add_argument("-v", "--version", action="store_true",
                        help=_('show version information.'))

    
    return parser, parser.parse_args()


#------------------------------------------------------------------------------
# process arguments
parser, args = arguments()

if args.gui or not checkAt() or not checkNotify():
    print(_("Proceeding in stand-alone mode:\n"
            "closing the GUI will delete all alarms."))
    from gwarnme import gstart
    gstart()
else:
    if args.copyright:
        print(WARNME_NAME, WARNME_VERSION)
        print(WARNME_SHORT_COPYRIGHT, '\n')
        print(WARNME_COPYRIGHT)
    if args.warranty:
        print(WARNME_NAME, WARNME_VERSION)
        print(WARNME_SHORT_COPYRIGHT, '\n')
        print(WARNME_WARRANTY)
    if args.version:
        print(WARNME_NAME, WARNME_VERSION)
        print(WARNME_SHORT_COPYRIGHT)
    if args.list:
        for i in listConfigAlarms():
            print('{}: {}'.format(*i))
    if args.delete:
        if removeAlarm(str(args.delete)):
            print(_('Alarm removed.'))
        else:
            print(_('Alarm not found.'))
    if args.ain:
        if args.at:
            error(_("Conflicting options: '--at/--in'"), True)
        print(_('Alarm set:'),
              setAlarmFromNow(args.ain, args.text, args.repeat))
        if args.repeat:
            print(_('Repeat every {} minutes.').format(args.repeat))
    if args.at:
        if args.ain:
            error(_("Conflicting options: '--at/--in'"), True)
        print(_('Alarm set:'),
              setAlarmAtTime(args.at, args.text, args.repeat))
        if args.repeat:
            print(_('Repeat every {} minutes.').format(args.repeat))
    if not (args.copyright or
            args.warranty or
            args.version or
            args.list or
            args.delete or
            args.ain or args.at):
        parser.print_help()
