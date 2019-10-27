import threading
import json
from sqlscripts.notify import notify_users
from matchupdater import  request_match
from example import start_parser
from helpers import get_socket
from rcontypes import rcon_event, rcon_receive
def handle_match_request(event_id, message_string):
    if event_id == rcon_event.request_data.value:
        js = json.loads(message_string)
        case = int(js['CaseID'])
        if case == rcon_receive.request_match.value:
            print('notifying with ' + js['Players'])
            notify_users(int(js['Players']))

            

if __name__ == "__main__":
    sock = get_socket()
    x = threading.Thread(target = start_parser, args = (sock, handle_match_request))
    x.start()
    y = threading.Thread(target = request_match, args = (sock,))
    y.start()
    x.join()
    y.join()