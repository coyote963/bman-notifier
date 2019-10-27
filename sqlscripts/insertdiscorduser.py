import sqlite3
from sqlite3 import Error
from datetime import datetime
from parsediscordconfigs import url, filelocation, token

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 

def create_discorduser(conn, discorduser):
    """
    Create a new discorduser
    :param conn:
    :param discorduser:
    :return:
    """
 
    sql = ''' INSERT INTO discordusers(id,threshold,created,lastnotified)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, discorduser)
    return cur.lastrowid
 
 
def execute_initial():
    database = filelocation
    uids = [
        "468495772539813919",
        "393131973448564757",
        "264420350274568192",
        "302527330679652363"
    ]
    # create a database connection
    conn = create_connection(database)
    with conn:
        for i in range(len(uids)):
            create_discorduser(conn, (uids[i], 5, str(datetime.now()), str(datetime.now())))

