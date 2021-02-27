"""Warn Me text related stuff

Timed notification program
Copyright (C) 2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = '2.1'
__date__ = '2021-02-27'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


#------------------------------------------------------------------------------
# Changes history:
#    2.1 (2021-02-27): publishing in GitHub
#    2.0 (2019-10-01): updated to version 2.0
#  1.0.1 (2019-09-07): updated version number and date
#    1.0 (2014-02-23): first version


import os
import sys
import gettext


#------------------------------------------------------------------------------
# bind gettext domain (localization)
gettext.bindtextdomain('warnme', os.path.join(sys.path[0], 'locales'))
gettext.textdomain('warnme')
_ = gettext.gettext


#------------------------------------------------------------------------------
def labelUnderline(label):
    '''Format Tkinter menu label from general format.
       label: label with underscore before letter to underline
       Returns tuple (Tkinter label, Tkinter underline position).
    '''
    i = label.find('_')
    return (label[:i] + label[i+1:], i)


#------------------------------------------------------------------------------
# Help text

WARNME_NAME = 'Warn me'
WARNME_VERSION = '2.1'
WARNME_WEBSITE = 'https://ammdias.duckdns.org/downloads'
WARNME_WEBSITE_LABEL = 'AMMDIAS'
WARNME_SHORT_COPYRIGHT = '''Timed notification program
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
along with this program.  If not, see <https://www.gnu.org/licenses/>.'''


#------------------------------------------------------------------------------
# Legal stuff constants

WARNME_COPYRIGHT = _('''From the Preamble of the GNU General Public License:
        
The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

See the file LICENSE on the program's directory for more details.
If it's missing please refer to http://www.gnu.org/licenses/gpl.txt
''')

WARNME_WARRANTY = _('''From the GNU General Public License:
    
15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE
COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS"
WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY
AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

16. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
''')

WARNME_HELP = _('''
Warn me

Copyright (C) 2021 António Manuel Dias
contact: ammdias@gmail.com

This program comes with ABSOLUTELY NO WARRANTY;  for details use command
'warnme.py --warranty' or go to 'Help > Warranty' on the graphical user
interface.

This is free software, and you are welcome to redistribute it under certain
conditions; use command 'warnme.py --copyright' or go to 'Help > Copyright' on
the graphical user interface for details.

----

Warn me is a program to set timed desktop notifications.  It may be used from
the command line if the POSIX 'at' and the freedesktop.org 'notify-send'
utilities are available.  If not or if you prefer to use a graphical interface
the program may be used that way with no other dependencies except Python 3
with Tkinter module.


Graphical User Interface
========================

The program's graphical user interface may be launched in the following ways:

* Launch the 'gwarnme.py' program;
* Launch the 'warnme.py' program with the '--gui' option;
* Trying to use the 'warnme.py' program in a system without either the POSIX
  'at' or the freedesktop.org 'notify-send' utilities.

You may set an alarm in one of these ways:

* Set alarm to fire in a specified interval in minutes:
  - click "Set alarm in"
  - choose the number of minutes
  - type the desired alarm notification message
  - if you wish, set the recurrence interval of the alarm, in minutes
  - press "Set alarm" button

* Set alarm to fire at specified time:
  - click "Set alarm at"
  - choose the hour and minute
  - type the desired alarm notification message
  - if you wish, set the recurrence interval of the alarm, in minutes
  - press "Set Alarm" button

To remove an alarm, select it on the list of pending alarms and press the
"Remove alarm" button.  You may select several alarms simultaneously.

All notifications will be lost if you close the program.

Command Line Interface
======================

Command line interface (terminal) accepted commands and syntax:

* Set alarm at specified interval in minutes:
  warnme.py --in <minutes> [--text <message>]

* Set alarm at specific time:
  warnme.py --at <hour:minute> [--text <message>]

* For each of the previous commands, you may also set the recurrence of the
  alarms, in minutes:
  warnme.py --in <minutes> [--text <message>] --repeat <minutes>
  warnme.py --at <hour:minute> [--text <message>] --repeat <minutes>

* Show list of alarm IDs and descriptions:
  warnme.py --list
  
* Remove alarm identified by alarm ID:
  warnme.py --delete <alarm ID>

* Start the graphical user interface:
  warnme.py --gui

* Print Help, Warranty, Copyright and version information on the terminal:
  warnme.py --help
  warnme.py --warranty
  warnme.py --copyright
  warnme.py --version
  
* Test notification interface:
  wmnotify.py <message>
''')
