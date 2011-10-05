# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('ubuntu-pomadoro-tasks')

import gtk
import logging
logger = logging.getLogger('ubuntu_pomadoro_tasks')

from ubuntu_pomadoro_tasks_lib import Window
from ubuntu_pomadoro_tasks.AboutUbuntuPomadoroTasksDialog import AboutUbuntuPomadoroTasksDialog
from ubuntu_pomadoro_tasks.PreferencesUbuntuPomadoroTasksDialog import PreferencesUbuntuPomadoroTasksDialog

# See ubuntu_pomadoro_tasks_lib.Window.py for more details about how this class works
class UbuntuPomadoroTasksWindow(Window):
    __gtype_name__ = "UbuntuPomadoroTasksWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UbuntuPomadoroTasksWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutUbuntuPomadoroTasksDialog
        self.PreferencesDialog = PreferencesUbuntuPomadoroTasksDialog

        # Code for other initialization actions should be added here.

