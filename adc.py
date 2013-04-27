#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import os
import time
import fnmatch
import ConfigParser
from datetime import date

numOfEx = 5 

def getFiles(path, pattern):
      return [i for r, NIL, items in os.walk(path) for i in items if fnmatch.fnmatch(i, pattern)];

def getFolders(path, pattern):
      return [i for r, items, NIL in os.walk(path) for i in items if fnmatch.fnmatch(i, pattern)];

def getExercises():
    exercises = list()
    for i in range(numOfEx):
        exercise = dict()
        exercise['title'] = 'Blablabla'
        exercise['solutionText'] = 'Blablabla'
        exercise['sourceFile'] = 'source.pas'
        exercises.append(exercise)
    return exercises

#open file for writing
f = open('compiled.tex', 'w')

#reading data from configfile
config = ConfigParser.RawConfigParser()
config.read('.configure')

#set data
globalConfig = dict(config.items('global'))
documentConfig = dict(config.items('document'))

#defining data for use in template
nameSpace = {
             'author': globalConfig['author'],
             'course': documentConfig['coursename'],
             'date': documentConfig['date'],
             'documentname': documentConfig['documentname'],
             'exercises': getExercises(),
             'numOfEx': numOfEx,
            }

#define template
t = Template(file="templates/default.template", searchList=[nameSpace])

#writing template to file
f.write(str(t)) 
f.close
