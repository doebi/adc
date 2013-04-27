import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('general')
config.set('general', 'author', 'Max Mustermann')

config.add_section('document')
config.set('document', 'documentname', '')
config.set('document', 'date', '')
config.set('document', 'coursename', '')
config.set('document', 'source-language', '')
config.set('document', 'idea', 'idea.txt')


with open('../.adc/.config', 'wb') as configfile:
  config.write(configfile);
