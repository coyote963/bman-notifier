from configparser import ConfigParser

parser = ConfigParser()
parser.read('sqlscripts/discordsettings.ini')
print(parser.sections())
filelocation = parser.get('connections', 'filelocation')
token = parser.get('connections', 'token')
url = parser.get('connections', 'url')