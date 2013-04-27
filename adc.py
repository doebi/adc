#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import time
from datetime import date

numOfEx = 10

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

#defining data for use in template
nameSpace = {
             'author': 'Max Mustermann',
             'course': 'ADF2 / PRO2 SS 13',
             'date': date.today().isoformat(),
             'documentname': 'Uebung #',
             'exercises': getExercises(),
             'numOfEx': numOfEx,
            }

#define template
t = Template(file="templates/default.template", searchList=[nameSpace])

#writing template to file
f.write(str(t)) 
f.close
