#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Created on Fri Nov 23 02:51:41 2018
* Purpose: test out running a linux shell process from Python
*
* Copyright (c) 2018 Giorgi [DrAcid] Maghlakelidze (https://github.com/dracid/)
*
* This program is free software; you can redistribute it and/or
* modify it under the terms of the GNU General Public
* License as published by the Free Software Foundation; either
* version 3 of the License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
* General Public License for more details.
*
* You should have received a copy of the GNU General Public
* License along with this program; if not, write to the
* Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
* Boston, MA 02110-1301 USA
*
* Authored by: Giorgi [DrAcid] Maghlakelidze <acidlabz@gmail.com>
"""
import subprocess


def execute_command(cmd, print_output=False):
    # TODO something about timeouts? Connecting may take time, maybe allow as an argument
    out = subprocess.run(cmd + " 1>&2", shell=True, timeout=10, stderr=subprocess.PIPE)
    msg = out.stderr.decode()

    if print_output:
        indent = '   '
        newline = '\r'
        msg_print = indent + msg.replace(newline, newline + indent)
        print("The command returned: \n" + msg_print)

    return msg

# # Testing out the code
# cmd = "nordvpn status"
# msg = execute_command(cmd, print_output=True)
# print(msg)