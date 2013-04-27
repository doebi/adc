#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import time
import ConfigParser
from datetime import date

numOfEx = 5 

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
author = config.get('global', 'author')

date = config.get('document', 'date')
documentname = config.get('document', 'documentname')
coursename = config.get('document', 'coursename')

#defining data for use in template
nameSpace = {
             'author': author,
             'course': coursename,
             'date': date,
             'documentname': documentname,
             'exercises': getExercises(),
             'numOfEx': numOfEx,
            }

#define template
t = Template(file="templates/default.template", searchList=[nameSpace])

#writing template to file
f.write(str(t)) 
f.close
