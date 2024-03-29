# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('ubuntu-pomadoro-tasks')

import gtk

from ubuntu_pomadoro_tasks import UbuntuPomadoroTasksWindow

from ubuntu_pomadoro_tasks_lib import set_up_logging, preferences, get_version

def parse_options():
    """Support for command line options"""
    parser = optparse.OptionParser(version="%%prog %s" % get_version())
    parser.add_option(
        "-v", "--verbose", action="count", dest="verbose",
        help=_("Show debug messages (-vv debugs ubuntu_pomadoro_tasks_lib also)"))
    (options, args) = parser.parse_args()

    set_up_logging(options)

def main():
    'constructor for your class instances'
    parse_options()

    # preferences
    # set some values for our first session
    # TODO: replace defaults with your own values
    default_preferences = {
    'example_entry': 'I remember stuff',
    }
    preferences.update(default_preferences)
    # user's stored preferences are used for 2nd and subsequent sessions
    preferences.db_connect()
    preferences.load()

    # Run the application.    
    window = UbuntuPomadoroTasksWindow.UbuntuPomadoroTasksWindow()
    window.show()
    gtk.main()
    
    preferences.save()
