#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PyKDE4 Stuff
from PyKDE5.kdeui import *
from PyKDE5.kdecore import KGlobal

# Service Manager
from servicemanager.base import MainManager

class ServiceManager(KMainWindow):
    def __init__ (self, *args):
        KMainWindow.__init__(self)
        self.setWindowIcon(QIcon("/usr/share/pixmaps/icons/flag-yellow.svg"))

        # This is very important for translations when running as kcm_module
        KGlobal.locale().insertCatalog("service-manager")

        self.resize (640, 480)
        self.setCentralWidget(MainManager(self))

