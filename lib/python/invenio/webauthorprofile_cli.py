# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2011 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""
webauthorprofile_cli
    This module provides a command-line interface for WebAuthorProfile.
"""

import bibauthorid_config as bconfig


def main():
    """Main function """
    try:
        import webauthorprofile_daemon as daemon
    except ImportError:
        bconfig.LOGGER.error("Hmm...No Daemon process running.")
        return

    daemon.webauthorprofile_daemon()


if __name__ == '__main__':
    main()

