# Chelcea Claudiu Marian

This is a CV presentation website developed for the Introduction in Informatics Course.

The server side was implemented using Python and Flask and the webpages were build with
HTML & CSS and bootstrap.

The website also features an functioning contact form that will send me an email with
the given input from the form.

For privacy reasons, the login information from the code, file: main.py, lines 15-16
are placed as dummy_gmail@gmail.com and dummy_gmail_password.
For the form to work correctly, you have to change those lines with an actual gmail account.

The email structure will be as follows:

Name: <name_completed_in_the_form>
Company: <company_completed_in_the_form>
Email: <email_completed_in_the_form>
Phone number: <phone_number_completed_in_the_form>

Contact reason: <contact_reason_completed_in_the_form>
Message: <message_completed_in_the_form>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mandatory:
1.pip3 install flask
2.pip3 install flask_mail
3.in main.py, lines 15-16, input a real gmail account

Start the server:python3 main.py

Website pages:
http://127.0.0.1:5000/Home
http://127.0.0.1:5000/Contact

