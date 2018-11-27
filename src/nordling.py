#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Created on Thu Nov 22 21:45:03 2018
* Purpose: a tray icon that helps control NordVPN connection in a simple way.
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

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from runCMD import execute_command

debug = False
monochrome = True  # TODO make this as a launch parameter? Or autodetect KDE, which is a hassle perhaps?


class NordSystemTrayIcon(QtWidgets.QSystemTrayIcon):
    flag_connected = False
    home_path = os.path.expanduser('~')
    icon_path = home_path + r'/.local/share/icons/hicolor/64x64/apps/'
    
    if monochrome:
        icon_on  = icon_path + r'nordvpn_ON_monochrome_darktheme.svg'
        icon_off = icon_path + r'nordvpn_OFF_monochrome_darktheme.svg'
    else:
        icon_on  = icon_path + r'nordvpn_ON.svg'
        icon_off = icon_path + r'nordvpn_OFF.svg'
    
    countries_list   = ['Germany', 'United_States', 'Georgia']
    countries_recent = countries_list[0]
    countries_active = 'None'
    
    
    def __init__(self, parent=None):        
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon(self.icon_off), parent)
        self.setToolTip(f'NordVPN Connected To: {self.countries_active}')
        
        menu = QtWidgets.QMenu( parent)
        
        self.statusAction = menu.addAction(f"Connected to: {self.countries_active}")
        self.statusAction.setDisabled(True)
        
        menu.addSeparator() # =================== #
        
        toggleAction = menu.addAction("VPN Toggle")
        toggleAction.triggered.connect(self.vpn_toggle)
        self.activated.connect(self.vpn_toggle)
        
        # TODO add country selection
        # TODO populate automatically
        # TODO remember last used
        # TODO add favorites? How?
        menuNetworkMode = menu.addMenu('Country')
        modeUDPAction = menuNetworkMode.addAction('Germany')
        modeTCPAction = menuNetworkMode.addAction('USA')
        
        menu.addSeparator() # =================== #
        
        # TODO add UDP mode switching
        menuNetworkMode = menu.addMenu('Protocol')
        modeUDPAction = menuNetworkMode.addAction('UDP')
        modeTCPAction = menuNetworkMode.addAction('TCP')
        
        menu.addSeparator() # =================== #
        
        exitAction = menu.addAction("Quit")
        exitAction.triggered.connect(self.exit_app)
        
        self.setContextMenu(menu)
        
        self.check_connected(False)
    
        
    def exit_app(self):
        sys.exit()
        #QtCore.QCoreApplication.exit()
        
        
    def check_connected(self, print_msg=True):
        print("Checking the connection...", end="")
        if debug:
            print("Connected to NordVPN!")
            return True
        
        connected = False
        
        cmd = "nordvpn status"
        msg = execute_command(cmd, print_msg)
        
        if msg.find("Connected") >= 0:
            connected = True
            print("Connected to NordVPN!")
            self.setIcon(QtGui.QIcon(self.icon_on))
            #self.showMessage("Connected!", f"NordVPN connected to country: {self.countries_active}", QtGui.QIcon(self.icon_on), 1000)
            #showMessage(const QString &title, const QString &message, const QIcon &icon, int millisecondsTimeoutHint = 10000)
        else:            
            connected = False
            print("NOT connected to NordVPN!!")
            self.setIcon(QtGui.QIcon(self.icon_off))
            #self.showMessage("Disonnected!", f"NordVPN disconnected!", QtGui.QIcon(self.icon_off), 1000)
        
        self.setToolTip(f'NordVPN Connected To: {self.countries_active}')
        self.statusAction.setText(f"Connected to: {self.countries_active}")
        return connected
        
        
    def vpn_connect(self, country=''):
        print(f"Connecting to NordVPN {self.countries_active.capitalize()}... ", end='')
        self.countries_active = country
        
        cmd = f"nordvpn connect {self.countries_active}"
        msg = execute_command(cmd, print_output=True)
        
        self.flag_connected = self.check_connected(False)
    
    
    def vpn_disconnect(self):
        print("Disconnecting from NordVPN.")
        self.countries_active = 'None'
        
        cmd = "nordvpn disconnect"
        msg = execute_command(cmd, print_output=True)
        
        self.flag_connected = self.check_connected(False)
        
    
    def vpn_toggle(self):
        print('='*10, 'Toggling VPN connection.', '='*10)
        self.flag_connected = self.check_connected(False)
        
        if not self.flag_connected:
            self.vpn_connect('Germany')
        else:
            self.vpn_disconnect()
            
        print("="*50)


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    w = QtWidgets.QWidget()
    trayIcon = NordSystemTrayIcon(w)
    
    trayIcon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    
    main()

