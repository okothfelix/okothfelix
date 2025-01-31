from . import frontend_bp
from flask import render_template, redirect, url_for, session, request, send_from_directory
import os
import secrets
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def email_notification_section(send_to, activation_link, name, message='', flag=0, subject=""):
    msg = MIMEMultipart()
    msg['From'] = 'okothfelix85@gmail.com'
    msg['To'] = 'okothfelix85@gmail.com'
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "PORTFOLIO USER ENQUIRY : " + str(secrets.token_hex(10))
    msg.attach(MIMEText(message))
    # context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    # SSL connection only working on Python 3+/
    smtp = smtplib.SMTP('smtp.swahiliafrique.com', 587)
    smtp.starttls()
    smtp.login('okothfelix85@gmail.com', 'Obierofelix_1')
    smtp.sendmail('accounts@swahiliafrique.com', 'okothfelix85@gmail.com', msg.as_string())
    smtp.quit()


@frontend_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@frontend_bp.route('/download')
def download():
    return send_from_directory(os.getcwd(), "felix_cv.pdf", as_attachment=True, mimetype='application/pdf')


@frontend_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['email']
        message = request.form['message']
        mail = name + ".\n\n" + address + ".\n\n" + message + ".\n"
        thread_obj = threading.Thread(target=email_notification_section, args=['', mail, 2])
        thread_obj.start()
        return render_template('contacts.html', contact_flag=True, back=request.referrer)
    else:
        account_result_set = False
        if 'account-result-set' in session:
            account_result_set = True
            session.pop('account-result-set')
        return render_template('contacts.html', account_result_set=account_result_set)


@frontend_bp.route('/case-studies', methods=['GET'])
def case_studies():
    return render_template('case-studies.html')


@frontend_bp.route('/case-studies/maarifa-education', methods=['GET'])
def case_studies_maarifa_education():
    return render_template('maarifa-education.html')


@frontend_bp.route('/case-studies/one-space-mall', methods=['GET'])
def case_studies_one_space_mall():
    return render_template('one-space-mall.html')


@frontend_bp.route('/case-studies/maarifa-polling', methods=['GET'])
def case_studies_maarifa_polling():
    return render_template('maarifa-polling.html')


@frontend_bp.route('/case-studies/maarifa-faith', methods=['GET'])
def case_studies_maarifa_faith():
    return render_template('maarifa-faith.html')


@frontend_bp.route('/case-studies/service-delivery', methods=['GET'])
def case_studies_maarifa_services():
    return render_template('service-delivery.html')