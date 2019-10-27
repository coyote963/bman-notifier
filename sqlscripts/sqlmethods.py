import sqlite3
from sqlite3 import Error
from sqlscripts.parsediscordconfigs import url, filelocation, token

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(filelocation)
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
    conn.commit()

def get_notified_discordusers(conn):
    """
    Return the discord users
    :param conn:
    :param lastnotifiedby:
    :return:
    """
    sql = '''SELECT id, threshold FROM discordusers WHERE 
                lastnotified < datetime('now','localtime', '-20 minutes');'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def get_discord_user(conn, discord_id):
    sql = ''' SELECT * FROM discordusers WHERE
                id=?'''
    cur = conn.cursor()
    cur.execute(sql, (discord_id,))
    return cur.fetchone()

def delete_discord_user(conn, discord_id):
    sql = 'DELETE FROM discordusers WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (discord_id,))
    conn.commit()

def get_all_user(conn):
    sql = ''' SELECT * FROM discordusers'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def update_threshold(conn, discord_id, new_threshold):
    sql = '''UPDATE discordusers
                SET threshold = ?
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (new_threshold, discord_id))
    conn.commit()

def update_lastnotified(conn, discord_id):
    sql = '''UPDATE discordusers
                SET lastnotified = datetime('now')
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (discord_id,))
    conn.commit()