'''Configuration file for the Warnme installation script.
'''

DOC = 'Installation script for Warn Me.'''
COPYRIGHT_YEAR = '2012'
VERSION = '2.3.1'
DATE = '#TODO'
AUTHOR = 'António Manuel Dias <ammdias@gmail.com>'
LICENSE = '''
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
'''


# List of file to be copied to installation the directory
FILES = ('gwarnme.py', 'gwmnotify.py', 'gwmtext.py', 'warnme.py', 'wmat.py',
         'wmcommon.py', 'wmnotify.py', 'wmtext.py', 'warnme.svg', 'warnme.desktop',
         'UNINSTALL.py', '__version__', 'LICENSE.md', 'README.md', 'CHANGES.md')

# List of directories to be copied to the installation directory
TREES = ('locales',)

# Name of the icon file
ICO_FILE = 'warnme.svg'

# Name of the desktop entry file (for GUI menus)
DESKTOP_FILE = 'warnme.desktop'

# Files to make executable
EXECS = ('warnme.py', 'gwarnme.py', 'wmnotify.py')

# Name of the application (will be the name of the installation directory)
APP_NAME = 'WarnMe'

# Symbolic links to make: dictionary of 'link name': 'executable name' pairs
LINKS = {'warnme': 'warnme.py', 'gwarnme': 'gwarnme.py'}

# List of configuration files
CONFIG_FILES = ('warnme_alarms',)
