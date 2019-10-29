from configparser import ConfigParser
import sys
parser = ConfigParser()
parser.read('sqlscripts/discordsettings.ini')
if len(parser.sections()) < 1:
    print("Error in discordsettings file")
    sys.exit()
filelocation = parser.get('connections', 'filelocation')
token = parser.get('connections', 'token')
url = parser.get('connections', 'url')