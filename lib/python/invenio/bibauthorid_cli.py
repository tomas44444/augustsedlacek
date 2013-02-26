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
bibauthorid_cli
    This module provides a command-line interface for BibAuthorID.
"""

from bibauthorid_general_utils import bibauthor_print

def main():
    """Main function """
    try:
        import bibauthorid_daemon as daemon
    except ImportError:
        bibauthor_print("Hmm...No Daemon process running.")
        return

    daemon.bibauthorid_daemon()


if __name__ == '__main__':
    main()

