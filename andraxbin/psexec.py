#!/bin/bash

source /opt/ANDRAX/impacket/bin/activate

/opt/ANDRAX/impacket/bin/python3 /opt/ANDRAX/impacket/bin/psexec.py "$@"
