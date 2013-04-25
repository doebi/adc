#!/usr/bin/python
#tool for automatic generation of documentation

from Cheetah.Template import Template
import time
from datetime import date

#open file for writing
f = open('compiled.tex', 'w')

#defining data for use in template
nameSpace = {
             'author': 'Max Mustermann',
             'course': 'ADF2 / PRO2 SS 13',
             'date': date.today().isoformat()
             'documentname': 'Übung #'
             'documentname': 'Übung #'
            }

#define template
t = Template(file="templates/default.tex", searchList=[nameSpace])

#writing template to file
f.write(str(t))
f.close
