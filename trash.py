import logging
import os
import subprocess
from flask import Flask
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@app.route('/')
def homepage():
    return "Hi there, how ya doin?"
#uncomment this subprocess line below to invoke the PS script at the time of execution.
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./TabCMDEmail.ps1\";"])


#Welcome Message function
@ask.launch
def launch():
    speech_text = 'Welcome to the Tableau Skills Kit, you can call me Daddy'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./TabCMDEmail.ps1\";"])





#Simple Report Function
#@ask.intent("SimpleReport")

#def yes();
#yes_text = render_template('Lorenzo is sexy')

#return statement(yes_text)



if __name__ == '__main__':
    app.run(debug=True)

