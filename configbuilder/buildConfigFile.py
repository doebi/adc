import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('document')
config.set('document', 'author', '')
config.set('document', 'documentname', '')
config.set('document', 'date', '')
config.set('document', 'coursename', '')
config.set('document', 'source-language', '')
config.set('document', 'idea', 'idea.txt')

with open('../.adc/.config', 'wb') as configfile:
  config.write(configfile);
