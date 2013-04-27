import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('document')
config.set('document', 'author', 'Max Mustermann')
config.set('document', 'documentname', 'Uebung 5')
config.set('document', 'date', '2012-04-29j ')
config.set('document', 'coursename', 'ADF')
config.set('document', 'idea', 'idea.txt')
config.set('document', 'folderpattern', 'ex*')

with open('../.adc/.config', 'wb') as configfile:
  config.write(configfile);
