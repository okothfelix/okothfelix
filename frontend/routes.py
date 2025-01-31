from . import frontend_bp
from flask import render_template, send_from_directory
import os


@frontend_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@frontend_bp.route('/download')
def download():
    return send_from_directory(os.getcwd(), "felix_cv.pdf", as_attachment=True, mimetype='application/pdf')


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