"""Warn Me 'at' communication library
 
Timed notification program
Use 'at' program to schedule a notification
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
#    2.2 (2021-02-28): changed place of alarm list for multi-user use
#    2.1 (2021-02-27): publishing in GitHub
#    2.0 (2019-10-13): rewrite for Warn Me 2.0
#  1.0.1 (2019-09-07): moved config directory into .config
#    1.0 (2014-02-23): first version


import os
import sys
import re
from subprocess import Popen, PIPE

from wmtext import _
from wmcommon import error


#------------------------------------------------------------------------------
# Path related constants
WARNME_DIR = os.path.dirname(__file__)
WARNME_NOTIFY = os.path.join(WARNME_DIR, 'wmnotify.py')

user_dir = os.path.expanduser(os.path.join('~', '.config'))
if os.path.exists(user_dir):
    WARNME_ALARM_LIST = os.path.join(user_dir, 'warnme_alarms')
else:
    WARNME_ALARM_LIST = os.path.expanduser(os.path_join('~', '.warnme_alarms'))

# Check if alarm list file exists, create it if not
try:
    if not os.path.isfile(WARNME_ALARM_LIST):
        open(WARNME_ALARM_LIST, 'w').write('')
except:
    error(_('cannot create alarm list file.'), True)


#------------------------------------------------------------------------------
def _configAlarm(jobId, time, text):
    '''Append alarm to alarm list file.
       Returns string with alarm time and message.
    '''
    message = '{} {}'.format(time, text)
    try:
        open(WARNME_ALARM_LIST, 'a').write("{}|{}\n".format(jobId, message))
    except:
        error(_('could not append alarm to alarm list file.'), True)

    return message


#------------------------------------------------------------------------------
def _atCommunicate(atProc, text, repeat):
    '''Communicate with 'at' proccess to set the notification message,
       decode its output and append alarm to alarm file list.
       Returns string with alarm time and message.'''
    (dummy, atOutp) = atProc.communicate("{} '{}' -r {}".format(WARNME_NOTIFY,
                                                                text, repeat))

    # atOutp will be something like this:
    #   warning: commands will be executed using /bin/sh
    #   job 9 at Sat Feb 15 18:56:00 2014
    #
    match = re.search('job\s+(\d+) at \w{3} \w{3}\s+\d{1,2} (\d\d:\d\d)',
                      atOutp,
                      re.IGNORECASE + re.MULTILINE)
    if match:
        (jobId, time) = match.group(1,2)
        return _configAlarm(jobId, time, text)
    
    error(_("could not parse 'at' response."), True)
    return None


#------------------------------------------------------------------------------
def _listSetAlarms():
    '''Call 'atq' to get list of 'at' job IDs.
       Returns list of strings with job IDs.
    '''
    p = Popen('atq', stdout=PIPE, universal_newlines=True)
    atOutp = p.stdout.read().split('\n')
    p.terminate()

    # atOutp will be something like this:
    # [ '13\tSun Feb 16 19:01:00 2014 a antonio',
    #   '14\tSun Feb 16 19:02:00 2014 a antonio',
    #   ''
    # ]
    return [ln.split()[0] for ln in atOutp if ln]


#------------------------------------------------------------------------------
def setAlarmFromNow(timeLapse, text, repeat):
    '''Call 'at' to set an alarm timeLapse minutes from now with notification
       message and append alarm to alarm file list.
       Returns string with alarm time and message.
    '''
    atProc = Popen(('at', 'now', '+ {} minutes'.format(timeLapse)),
                   stdin=PIPE, stdout=PIPE, stderr=PIPE,
                   universal_newlines=True)
    return _atCommunicate(atProc, text, repeat)


#------------------------------------------------------------------------------
def setAlarmAtTime(atTime, text, repeat):
    '''Call 'at' to set an alarm at specific atTime with notification message
       and appen alarm to alarm file list.
       Returns string with alarm time and message.
    '''
    atProc = Popen(('at', atTime),
                   stdin=PIPE, stdout=PIPE, stderr=PIPE,
                   universal_newlines=True)
    return _atCommunicate(atProc, text, repeat)


#------------------------------------------------------------------------------
def removeAlarm(jobId):
    '''Call 'atrm' to remove jobId from 'at' jobs.
       Returns True on successful removal, False otherwise (job was not found).
    '''
    p = Popen(['atrm', jobId], stderr=PIPE, universal_newlines=True)
    atOutp = p.stderr.read()
    p.terminate()

    # atOutp will be empty if alarm was removed or something like this if not:
    #   Cannot find jobid 11
    #
    return atOutp == ''


#------------------------------------------------------------------------------
def listConfigAlarms():
    '''Get alarms from alarm list file, removing expired or removed alarms.
       Writes updated alarm list to alarm list file.
       Returns list of string tuples (alarm job ID, alarm time+message).
    '''
    setAlarms = _listSetAlarms()
    alarms = []

    try:
        for ln in open(WARNME_ALARM_LIST, 'r'):
            ln = ln.strip()
            if ln:
                (jobId, descr) = ln.split('|')
                if jobId in setAlarms:
                    alarms.append((jobId, descr))
    except:
        error(_('corrupted alarm list file.'), True)

    # purge unset alarms from alarm list file
    try:
        f = open(WARNME_ALARM_LIST, 'w')
        for a in alarms:
            print("{}|{}".format(*a), file = f)
        f.close()
    except:
        error(_('could not write to alarm list file.'), True)

    return alarms
