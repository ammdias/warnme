Warn Me
=======

(C) 2012 António Manuel Dias

Changes list:

    * 2.3 (2023-12-07): Added uninstall option.
                        Changed linux installation scripts.
                        Changed README and LICENSE files to Markdown.

    * 2.2 (2021-02-28): Relocated 'at' alarm list for multi-user usage.

    * 2.1 (2021-02-27): Small changes to publish on GitHub.

    * 2.0 (2019-10-13): Complete rewrite, integrating Warn me Portable and
                        removing GTK requirement. If `at` and `notify-send` are
                        available, it may be used from the terminal.  If not,
                        it will work in standalone GUI mode using Tkinter.
                        Added recurrent alarm possibility (repeat function).

    * 1.0 (2014-02-23): Complete rewrite using GTK3, GObject, Python >= 3.3,
                        and POSIX at

    * 0.6 (2012-02-09): fixed time format problem in fmttm()
                        (reported by António Lima)

    * 0.5 (2012-02-05): code cleanup, several fixes,
                        regeneration of icon cache on installation

    * 0.4 (2012-02-02): changed notification summary to 'Warn Me'
                        (requested by António Lima)

    * 0.3 (2012-01-31): added zenity dialog, i18n, pt_PT locale
                        and freedesktop.org menu and icons

    * 0.2 (2012-01-26): added 'message in xx seconds' notification
                        added error notifications
                        added notification function: nwarn()

    * 0.1: Initial version.
