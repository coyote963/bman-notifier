import threading
import json
from sqlscripts.notify import notify_users
from matchupdater import  request_match
from example import start_parser
from helpers import get_socket
from rcontypes import rcon_event, rcon_receive
from sqlscripts.discord_webhook import execute_webhook
from sqlscripts.parsediscordconfigs import urlsvl, urlsvlmissions


playerdict = {}


def callback(event_id, message_string):
    functionarray = [handle_take_mission,
        handle_scoreboard_request,
        handle_match_request,
        handle_fail_mission,
        handle_complete_mission,
        send_svlchat_to_discord]
    for f in functionarray:
        f(event_id, message_string)

def handle_match_request(event_id, message_string):
    if event_id == rcon_event.request_data.value:
        js = json.loads(message_string)
        case = int(js['CaseID'])
        if case == rcon_receive.request_match.value:
            print('notifying with ' + js['Players'])
            notify_users(int(js['Players']))

def handle_take_mission(event_id, message_string):
    if event_id == rcon_event.survival_take_mission.value:
        js = json.loads(message_string)
        content = js['PlayerID'] + " took " + js['Mission'] + " for $" + js['Reward']
        execute_webhook(content, urlsvlmissions)

def handle_fail_mission(event_id, message_string):
    if event_id == rcon_event.survival_fail_mission.value:
        js = json.loads(message_string)
        content = js['PlayerID'] + " failed " + js['Mission'] + " for $" + js['Reward']
        execute_webhook(content, urlsvlmissions)

def handle_complete_mission(event_id, message_string):
    if event_id == rcon_event.survival_fail_mission.value:
        js = json.loads(message_string)
        content = js['PlayerID'] + " completed " + js['Mission'] + " for $" + js['Reward']
        execute_webhook(content, urlsvlmissions)

def handle_scoreboard_request(event_id, message_string):
    if event_id == rcon_event.request_data.value:
        js = json.loads(message_string)
        if int(js['CaseID']) == rcon_receive.request_scoreboard.value:
            print(js)



def send_svlchat_to_discord(event_id, message_string):
    if event_id == rcon_event.chat_message.value:
        js = json.loads(message_string)
        execute_webhook(js['Message'],urlsvl)




if __name__ == "__main__":
    sock = get_socket()
    x = threading.Thread(target = start_parser, args = (sock, callback))
    x.start()
    y = threading.Thread(target = request_match, args = (sock,))
    y.start()
    x.join()
    y.join()