from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

from flask import request
import pandas as pd

class ChoiceForm(Form):
    choice1 = TextField('Q1')
    choice2 = TextField('Q2')
    choice3 = TextField('Q3')
    choice4 = TextField('Q4')
#    choice3 = RadioField('Label', choices=[('value','description'),('value_two','whatever')])
    #choice1 = HiddenField('You cannot see this', description='Nope')

    submit_button = SubmitField('Submit Form')

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/',methods=['GET','POST'])
    def index():
        form = ChoiceForm()
        data=None
        if request.method == 'POST':
            #get form answers
            data={'A':form.choice1.data,'B':form.choice2.data,'C':form.choice3.data,'D':form.choice4.data}
            
            #find right style
            style='full'
            
            if(data['D']=='D3'):
                style='minimizer'
            else:
                if(data['A']=='A1' or data['A']=='A2'):
                    style='full'
                else:
                    if(data['B']=='B1'):
                        style='full'
                    else:
                        if(data['C']=='C1'):
                            if(data['D']=='D1'):
                                style='demi'
                            else:
                                style='plunge'
                        else:
                            if(data['D']=='D1'):
                                style='balconette'
                            else:
                                style='plunge'
                                
                
            data=pd.read_csv('static/data/specs.csv')
            data=data[data.StyleOutput == style]
            
            return render_template('out.html', style=style,styledf=data.StyleOutput,links=data.linksPages,images=data.fileImages)
        else:
            return render_template('index.html', form=form)
        

    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
    
    @app.route('/shutdown')#, methods=['POST'])
    def shutdown():
        shutdown_server()
        return 'Server shutting down...'

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
