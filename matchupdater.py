from rcontypes import rcon_receive
from helpers import send_packet, get_socket
import sys

import threading
# a process that calls for the match every 10 seconds
def request_match(sock):
    send_packet(sock, '"abc" "cde"', rcon_receive.request_match.value)
    print("sending")
    threading.Timer(10, request_match, (sock,)).start()

