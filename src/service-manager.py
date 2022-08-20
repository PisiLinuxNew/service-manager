#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# System
import sys
import dbus

# Application Stuff
#import servicemanager.about as about
# Application Stuff
from servicemanager.base import MainManager
from PyQt5.QtGui import QIcon

    # Pds Stuff
from pds.quniqueapp import QUniqueApplication
from servicemanager.context import KIcon, i18n

# Create a QUniqueApllication instance
app = QUniqueApplication(sys.argv, catalog="service-manager")


if __name__ == '__main__':

    # DBUS MainLoop
    if not dbus.get_default_main_loop():
        from dbus.mainloop.pyqt5 import DBusQtMainLoop
        DBusQtMainLoop(set_as_default = True)

    # Create Main Widget and make some settings
    mainWindow = MainManager(None)
    mainWindow.show()
    mainWindow.resize(640, 480)
    mainWindow.setWindowTitle("Service Manager")
    mainWindow.setWindowIcon(QIcon("/usr/share/pixmaps/plymouth-pisilinux.png"))

    # Create connection for lastWindowClosed signal to quit app
    app.lastWindowClosed.connect(app.quit)

    # Run the applications
    app.exec_()
