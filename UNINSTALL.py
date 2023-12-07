#!/usr/bin/env python3
'''Uninstall function.
   May be used as a standalone script.
'''

import sys
import os
import shutil


def _quit(msg):
    '''Print error message and quit.
    '''
    print(f'Error: {msg}\n', file=sys.stderr)
    _rollback()
    sys.exit(1)


def _getlog():
    '''Get and parse application install log.
    '''
    log = []
    logfile = os.path.join(sys.path[0], 'install.log')
    if os.path.lexists(logfile):
        for f in open(logfile).readlines():
            f = f.strip()
            if f:
                ptype, sep, path = f.partition(':')
                log.append((ptype, path))
    else:
        # no install log, add program directory only;
        # config file, if it exists, will be ignored.
        log = [('dir', sys.path[0])]

    return log


def yesno(question):
    '''Get a yes or no answer to a question.
    '''
    answer = ''
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = input(f'{question} (y/n): ').strip().lower()

    return answer in ('y', 'yes')


def uninstall():
    '''Uninstall application.
    '''
    try:
        INSTALL_LOG = _getlog()
        for ptype, path in INSTALL_LOG:
            match ptype:
                case 'dir':
                    shutil.rmtree(path)
                case 'link':
                    os.remove(path)
                case 'config_file':
                    if yesno(f"Remove configuration file '{path}'?"):
                        os.remove(path)
                case _:
                    _quit('Unknown log entry type.')
    except Exception as e:
        print('Installation could not uninstalled.\n'
              'Some files or directories may still be on your filesystem.\n'
              'Please check these paths manually:\n', file=sys.stderr)
        print('\n'.join([path for ptype,path in INSTALL_LOG]), file=sys.stderr)
        sys.exit(1)

    print('Installation uninstalled successfully.', file=sys.stderr)


if __name__ == '__main__':
    uninstall()
