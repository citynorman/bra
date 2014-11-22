from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

from flask import request

# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code')
    area_code = IntegerField('Area Code/Exchange')
    number = TextField('Number')


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.')
    choice3 = RadioField('Label', choices=[('value','description'),('value_two','whatever')])
    choice1 = HiddenField('You cannot see this', description='Nope')

    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

    # subforms
    #mobile_phone = FormField(TelephoneForm)

    # you can change the label as well
    #office_phone = FormField(TelephoneForm, label='Your office phone')

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
        form = ExampleForm()
        data=None
        if request.method == 'POST':
            #print request.form['field1']
            print form.field1.data
            print 'post'
            data={'name':form.choice1.data}
        if form.validate_on_submit(): #to get error messages to the browser
            pass
        else:
            print 'invalid'
        return render_template('index.html', form=form,data=data)

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
