#!/usr/bin/env python3

"""Warn Me

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

__version__ = '2.3'
__date__ = '2023-12-07'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


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

    parser.add_argument("--uninstall", action="store_true",
                        help=_('uninstall application.'))

    
    return parser, parser.parse_args()


#------------------------------------------------------------------------------
# process arguments
parser, args = arguments()

if args.uninstall:
    from UNINSTALL import uninstall
    uninstall()
elif args.gui or not checkAt() or not checkNotify():
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
