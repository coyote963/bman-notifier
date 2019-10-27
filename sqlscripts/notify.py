from sqlscripts import sqlmethods
from sqlscripts.discord_webhook import execute_webhook
from sqlscripts.parsediscordconfigs import filelocation

def notify_users(number_players):
    conn = sqlmethods.create_connection(filelocation)
    users = sqlmethods.get_notified_discordusers(conn)
    for i in range(len(users)):
        user_id = users[i][0]
        threshold = users[i][1]
        print(threshold)
        if threshold <= number_players:
            execute_webhook('<@' + str(user_id) + "> There is a lot of players in the svl")
            sqlmethods.update_lastnotified(conn, str(user_id))