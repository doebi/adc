import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('global')
config.set('global', 'name', 'Max Mustermann')

config.add_section('document')
config.set('document', 'documentname', '')
config.set('document', 'date', '')
config.set('document', 'coursename', '')

with open('config.txt', 'wb') as configfile:
  config.write(configfile);
