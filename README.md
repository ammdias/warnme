WARN ME
=======
version 2.3.1

Copyright (C) 2012 António Manuel Dias

contact: ammdias@gmail.com

website: [AMMDIAS GitHub](https://github.com/ammdias/warnme)

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


## ABOUT THE PROGRAM

This is a simple alarm notifier to be used from the terminal window
that uses freedesktop.org `notify-send` to alert users of timed events
set by POSIX utility `at`.

If any of those utilities are not available the program will launch
a simple graphical interface (GUI) and use Python Timer to set the
notification events.  This interface may also be used, at the user
option, even if `at` and `notify-send` are available.

Depends on [Python 3.3+](https://www.python.org/). GUI uses
[Python Tkinter](https://docs.python.org/3/library/tkinter.html).


## INSTALLATION AND BASIC USAGE

### Linux systems:

The following instructions describe the installation process for basic usage
in a Linux environment.

1. Open a terminal in the directory where the program was uncompressed and run
   the installation script with Python 3:

       $ python3 INSTALL.py

   You will be prompted for the installation directory --- i.e. the directory
   under which the folder containing all the application files will be placed
   --- and for the start link directory --- i.e. the directory where the
   symbolic link for the program will be created.

   The default directories will install the program for the current user only
   and are suited for single-user systems.  If you want to keep these
   settings, just press ENTER when prompted.  The program will be installed in
   the directory `$HOME/.local/lib/PROGRAM` and the symbolic link
   `$HOME/.local/bin/program` will be created.  On most Linux systems the
   `$HOME/.local/bin` directory will be inserted in the execution PATH, if it
   exists. If it doesn't, you will have to add it manually.

   If a previous installation exists on the selected directory, you will be
   asked if you want to overwrite it.  Answer "`yes`" (or just "`y`") if that
   is the case or "`no`" ("`n`") if not.

2. Test that the installation was successful with the command:

       $ warnme --help

3. To launch the graphical user interface, type:

       $ gwarnme

4. Uninstall the program with the command:

       $ warnme --uninstall


### Other systems:

After download, unzip the file and run the program 'gwarnme.py' using Python 3.
Read the program's help for further instructions on how to use it.
