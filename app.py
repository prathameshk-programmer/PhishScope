from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file
)

import os

from modules.parser import parse_email
from modules.sender_analyzer import analyze_sender
from modules.url_analyzer import analyze_urls
from modules.keyword_analyzer import analyze_keywords
from modules.header_analyzer import analyze_headers
from modules.attachment_analyzer import analyze_attachments
from modules.ioc_extractor import extract_iocs
from modules.risk_engine import calculate_risk
from modules.report_generator import generate_report


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)



# ==========================
# HOME
# ==========================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# ==========================
# UPLOAD EMAIL
# ==========================

@app.route(
    "/upload",
    methods=["POST"]
)

def upload_email():


    if "email" not in request.files:

        return "No file uploaded"



    file = request.files["email"]



    if file.filename == "":

        return "No file selected"



    path = os.path.join(

        UPLOAD_FOLDER,

        file.filename

    )


    file.save(path)



    return redirect(

        url_for(

            "dashboard",

            filename=file.filename

        )

    )



# ==========================
# DASHBOARD
# ==========================

@app.route("/dashboard")
def dashboard():


    filename = request.args.get(
        "filename"
    )


    filepath = os.path.join(

        UPLOAD_FOLDER,

        filename

    )


    # Parse Email

    email_data = parse_email(
        filepath
    )


    # Analysis Modules

    sender_result = analyze_sender(
        email_data
    )


    url_result = analyze_urls(
        email_data["body"]
    )


    keyword_result = analyze_keywords(
        email_data["body"]
    )


    header_result = analyze_headers(
        email_data["headers"]
    )


    attachment_result = analyze_attachments(
        email_data["attachments"]
    )


    ioc_result = extract_iocs(
        email_data
    )



    # Risk Calculation

    risk_result = calculate_risk(

        sender_result,

        url_result,

        keyword_result,

        header_result,

        attachment_result

    )



    # Generate PDF

    report_path = generate_report(

        filename,

        email_data,

        sender_result,

        url_result,

        keyword_result,

        header_result,

        attachment_result,

        ioc_result,

        risk_result

    )

    chart_data = {
    "sender": sender_result.get("score",0),
    "urls": url_result.get("score",0),
    "keywords": keyword_result.get("score",0),
    "headers": header_result.get("score",0),
    "attachments": attachment_result.get("score",0)
}



    return render_template(

        "dashboard.html",

        email=email_data,

        sender=sender_result,

        urls=url_result,

        keywords=keyword_result,

        headers=header_result,

        attachments=attachment_result,

        iocs=ioc_result,

        risk=risk_result,

        report=report_path,

        chart_data=chart_data

    )



# ==========================
# DOWNLOAD REPORT
# ==========================

@app.route("/download")
def download_report():

    path = request.args.get(
        "path"
    )

    return send_file(

        path,

        as_attachment=True

    )



if __name__ == "__main__":

    app.run(
        debug=True
    )