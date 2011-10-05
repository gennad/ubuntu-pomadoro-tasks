# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('ubuntu-pomadoro-tasks')

import logging
logger = logging.getLogger('ubuntu_pomadoro_tasks')

from ubuntu_pomadoro_tasks_lib.AboutDialog import AboutDialog

# See ubuntu_pomadoro_tasks_lib.AboutDialog.py for more details about how this class works.
class AboutUbuntuPomadoroTasksDialog(AboutDialog):
    __gtype_name__ = "AboutUbuntuPomadoroTasksDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutUbuntuPomadoroTasksDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

