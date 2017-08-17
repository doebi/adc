#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import os
import time
import fnmatch
import subprocess
import ConfigParser
from datetime import date

def getExercises(pattern):
    exercises = list()  
 
    path = os.getcwd()
    for (path, dirs, files) in os.walk(path):
        for dir in dirs: 
            if fnmatch.fnmatch(str(dir).lower(), pattern.lower()):
                exercise = dict()
                exercise['title'] = dir
                exercise['solutionText'] = 'Blablabla'
                exercise['sourceFile'] = 'source.pas'
                exercises.append(exercise)
        break
    return exercises

def getConfig():
    #reading data from configfile
    config = ConfigParser.RawConfigParser()
    config.read('.adc/.config')
    documentConfig = dict(config.items('document')) 
    return documentConfig

def makeConfig():
    import ConfigParser

    config = ConfigParser.RawConfigParser()

    config.add_section('document')
    config.set('document', 'author', 'Max Mustermann')
    config.set('document', 'documentname', 'Uebung 3')
    config.set('document', 'date', '2013-04-29')
    config.set('document', 'course', 'ADF oder so')
    config.set('document', 'idea', 'idea.txt')
    config.set('document', 'exercice-pattern', 'ex*')

    with open('.adc/.config', 'w') as configfile:
        config.write(configfile);

#Generate Latex File
def generateTex():
    nameSpace = getConfig()

    #open file for writing
    filename = nameSpace['documentname'] + '_' + nameSpace['date'] + '.tex'
    f = open('.adc/' + filename, 'w')

    #defining data for use in template
    nameSpace['exercises'] = getExercises(nameSpace['exercice-pattern'])

    #define template
    t = Template(file=".adc/templates/default.template", searchList=[nameSpace])

    #writing template to file
    f.write(str(t))
    f.close
    
    #create pdf
    #subprocess.call(['pdflatex', '.adc/' + filename])


#Init
def init():
    if not os.path.exists('.adc'): 
        os.makedirs('.adc')
    open('.adc/.config', 'w').close()
    makeConfig()

#setup config if not exists
try:
   with open('.adc/.config'): pass
except IOError:
    init()

print("Hello World")

#generate Tex File
generateTex()
