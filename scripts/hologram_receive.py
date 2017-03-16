# hologram_receive.py - Hologram Python SDK command line interface (CLI) for inbound messages.
#
# Author: Hologram <support@hologram.io>
#
# Copyright 2016 - Hologram (Konekt, Inc.)
#
# LICENSE: Distributed under the terms of the MIT License
#
import argparse
import sys
import hjson
import time

sys.path.append(".")
sys.path.append("..")

import Hologram
from Hologram.CustomCloud import CustomCloud
from Hologram.HologramCloud import HologramCloud

script_description = '''
This hologram_receive program listens on a given host and port for incoming connections
'''

def parseArguments():

    parser = argparse.ArgumentParser(description=script_description)

    parser.add_argument('--host', nargs = '?', default = '0.0.0.0')

    parser.add_argument('-p', '--port', type = int, nargs = '?', default = 4010)

    parser.add_argument('-t', '--timeout', type = int, nargs = '?', default = -1,
                        help = 'The number of seconds before the socket is closed. Default is to block indefinitely.')

    return parser.parse_args()

def main():

    args = parseArguments()
    credentials = dict()

    customCloud = CustomCloud(None,
                              receive_host = args.host,
                              receive_port = args.port,
                              enable_inbound = True)

    if args.timeout != -1:
        print 'waiting for ' + str(args.timeout) + ' seconds...'
        time.sleep(args.timeout)
    else:
        while True:
            time.sleep(1)

    customCloud.closeReceiveSocket()
    recv = customCloud.consumeReceivedMessage()
    print "Receive buffer: " + str(recv)

if __name__ == "__main__": main()