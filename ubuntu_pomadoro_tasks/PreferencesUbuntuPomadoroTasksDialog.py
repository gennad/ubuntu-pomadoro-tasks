# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

# This is your preferences dialog.
#
# Define your preferences dictionary in the __init__.main() function.
# The widget names in the PreferencesTestProjectDialog.ui
# file need to correspond to the keys in the preferences dictionary.
#
# Each preference also need to be defined in the 'widget_methods' map below
# to show up in the dialog itself.  Provide three bits of information:
#  1) The first entry is the method on the widget that grabs a value from the
#     widget.
#  2) The second entry is the method on the widget that sets the widgets value
#      from a stored preference.
#  3) The third entry is a signal the widget will send when the contents have
#     been changed by the user. The preferences dictionary is always up to
# date and will signal the rest of the application about these changes.
# The values will be saved to desktopcouch when the application closes.
#
# TODO: replace widget_methods with your own values


widget_methods = {
    'example_entry': ['get_text', 'set_text', 'changed'],
}

import gettext
from gettext import gettext as _
gettext.textdomain('ubuntu-pomadoro-tasks')

import logging
logger = logging.getLogger('ubuntu_pomadoro_tasks')

from ubuntu_pomadoro_tasks_lib.PreferencesDialog import PreferencesDialog

class PreferencesUbuntuPomadoroTasksDialog(PreferencesDialog):
    __gtype_name__ = "PreferencesUbuntuPomadoroTasksDialog"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the preferences dialog"""
        super(PreferencesUbuntuPomadoroTasksDialog, self).finish_initializing(builder)

        # populate the dialog from the preferences dictionary
        # using the methods from widget_methods
        self.widget_methods = widget_methods
        self.set_widgets_from_preferences() # pylint: disable=E1101

        # Code for other initialization actions should be added here.
