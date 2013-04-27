#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import os
import time
import fnmatch
import ConfigParser
from datetime import date

numOfEx = 3

def getExercises():
    exercises = list()
    for i in range(numOfEx):
        exercise = dict()
        exercise['title'] = 'Blablabla'
        exercise['solutionText'] = 'Blablabla'
        exercise['sourceFile'] = 'source.pas'
        exercises.append(exercise)
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
    config.set('document', 'coursename', 'ADF oder so')
    config.set('document', 'idea', 'idea.txt')
    config.set('document', 'exercice-pattern', 'ex*')

    with open('.adc/.config', 'w') as configfile:
        config.write(configfile);

#Generate Latex File
def generateTex():
    config = getConfig()

    #open file for writing
    f = open('compiled.tex', 'w')

    #defining data for use in template
    nameSpace = {
                 'author': config['author'],
                 'course': config['coursename'],
                 'date': config['date'],
                 'documentname': config['documentname'],
                 'exercises': getExercises(),
                }

    #define template
    t = Template(file=".adc/templates/default.template", searchList=[nameSpace])

    #writing template to file
    f.write(str(t))
    f.close

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

#generate Tex File
generateTex()
