from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
class ContactForm(FlaskForm):
    First Name = TextField(" First Name")
    Last Name = TextField("Last Name")
    Email = TextField("Email")
    Message = TextAreaField("Message")
    submit = SubmitField("Send")
    ###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template
from forms import ContactForm
from flask import request
import pandas as pd
###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'secretKey'
###############################################
#       Render Contact page                   #
###############################################
@app.route('/contacts.html', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contat
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
         First name =  request.form[" First Name"]
        Last Name = request.form["Last Name"]
        Email = request.form["Email"]
        Message = request.form["Message"]
        Submit= request.form["Submit"]
        res = pd.DataFrame({'First name':First Name, 'Last Name':Last Name, 'Email':EMail ,'message':message, 'Submit':submit}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("The data are saved !")
    else:
        return render_template('contact.html', form=form)
###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)