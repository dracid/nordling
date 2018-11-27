#!/bin/sh

clear

# TODO implement checking if dependencies are met: python3, pyqt, nordvpn
# TODO if dependencies not met, print a message and quit
echo "Checking dependencies met..."
echo "Success!"

# Copy application files to somewhere where they will be executed from
echo "Copying the executable files..."
rm ~/bin/Nordling -r
mkdir -p ~/bin/Nordling
cp ./src ~/bin/Nordling/ -r
cp ./launch_nordling.sh ~/bin/Nordling/

# Copy desktop file to here:   ~/.local/share/applications
echo "Copying the Desktop file..."
cp ./resources/Nordling.desktop  ~/.local/share/applications/

# Copy icons to ~/.local/share/icons/hicolor/
echo "Copying the icons..."
cp ./resources/32x32  ~/.local/share/icons/hicolor/ -r
cp ./resources/64x64  ~/.local/share/icons/hicolor/ -r

echo "Check you desktop environment launcher for Nordling. Enjoy!"
