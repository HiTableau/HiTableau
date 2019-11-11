#This is the Tableau Python app

import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import shutil



app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#Set display image to default
output_file = 'tableau_output.png'
shutil.copy('default_image.png', output_file)

#Welcome Message function
@ask.launch

def welcome():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)


#Simple Report Functino
@ask.intent("SimpleReport")

def display_report(report_name):
    print('Simple Report') #Show report that is running in log
    report_msg = render_template('report_confirm', report_name=report_name) #Set report confirmation response
    session.attributes['report_name'] = report_name

    #Set static output file name

    #Overwrite output with earnings file
    if report_name == 'earnings':
        print('Getting Earnings Report.')
        shutil.copy('earnings_report.png', output_file)
    
    #Overwrite output with sales file
    if report_name == 'sales':
        print('Getting Sales Report.')
        shutil.copy('sales_report.png', output_file)

    #Speak confirmation
    return statement(report_msg)

#Filtered Report Function
@ask.intent("FilteredReport")

def filtered_report(report_name, year, month):
    print('Filtered Report') #Show report that is running in log
    
    #If statement for if year filter is passed
    if year is not None:
        report_msg = render_template('filter_report_confirm', report_name=report_name, filter=year)
        session.attributes['report_name'] = report_name
        session.attributes['filter'] = year

        if report_name == 'earnings':
            shutil.copy('earnings_report.png', output_file)
        
        if report_name == 'sales':
            f'Getting {report_name} Report for {year}.'
            shutil.copy(f'sales_report_{year}.png', output_file)

    #If statement for if month filter is passed
    if month is not None:
        report_msg = render_template('filter_report_confirm', report_name=report_name, filter=month)
        session.attributes['report_name'] = report_name
        session.attributes['filter'] = month

        if report_name == 'earnings':
            f'Getting {report_name} Report for {month}.'
            shutil.copy(f'earnings_report_{month}.png', output_file)
        
        if report_name == 'sales':
            f'Getting {report_name} Report for {month}.'
            shutil.copy(f'sales_report_{month}.png', output_file)

    return statement(report_msg) 

if __name__ == '__main__':

    app.run(debug=True)
