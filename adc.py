#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import os
import time
import fnmatch
import ConfigParser
from datetime import date

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
    os.makedirs('.adc')
    open('.adc/.config', 'w').close()

#setup defaults if not exists
if not os.path.exists('.adc'):
    init()

generateTex()
