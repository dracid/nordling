#!/bin/sh


echo "Testing if Python3, PyQt and NordVPN are installed..."
# TODO implement checking if dependencies are met: python3, pyqt, nordvpn
# TODO if dependencies not met, print a message and quit
if true
then
    echo "Success!"
    # TODO get python 3 automatically
    #python3_var='/home/dracid/anaconda3/bin/python3'
    #echo $python3_var
    #$python3_var ./src/nordling.py

    # Seems like this works just fine:
    python3 ./src/nordling.py

fi
