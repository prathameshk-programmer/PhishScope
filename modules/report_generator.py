import os

from datetime import datetime


import matplotlib.pyplot as plt



from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle,

    Image

)


from reportlab.lib.styles import (

    getSampleStyleSheet,

    ParagraphStyle

)


from reportlab.lib.pagesizes import A4


from reportlab.lib import colors





REPORT_FOLDER = "reports"






# ================================
# CREATE THREAT GRAPH
# ================================


def create_threat_chart(

    sender,

    urls,

    keywords,

    headers,

    attachments

):


    chart_folder = os.path.join(

        REPORT_FOLDER,

        "charts"

    )



    os.makedirs(

        chart_folder,

        exist_ok=True

    )



    chart_path = os.path.join(

        chart_folder,

        "threat_analysis.png"

    )



    categories = [

        "Sender",

        "URLs",

        "Keywords",

        "Headers",

        "Attachments"

    ]



    values = [

        sender.get("score",0),

        urls.get("score",0),

        keywords.get("score",0),

        headers.get("score",0),

        attachments.get("score",0)

    ]



    plt.figure(

        figsize=(7,4)

    )


    plt.bar(

        categories,

        values

    )



    plt.ylim(

        0,

        100

    )


    plt.title(

        "PhishScope Threat Factor Analysis"

    )


    plt.ylabel(

        "Threat Score"

    )


    plt.xticks(

        rotation=25

    )



    plt.tight_layout()



    plt.savefig(

        chart_path,

        dpi=300

    )



    plt.close()



    return chart_path







# ================================
# GENERATE PDF
# ================================



def generate_report(


    filename,


    email,


    sender,


    urls,


    keywords,


    headers,


    attachments,


    iocs,


    risk


):



    os.makedirs(

        REPORT_FOLDER,

        exist_ok=True

    )




    pdf_name = filename.replace(

        ".eml",

        ".pdf"

    )



    path = os.path.join(

        REPORT_FOLDER,

        pdf_name

    )






    doc = SimpleDocTemplate(


        path,


        pagesize=A4,


        rightMargin=50,


        leftMargin=50,


        topMargin=50,


        bottomMargin=50


    )







    styles = getSampleStyleSheet()






    title_style = ParagraphStyle(

        "title",

        parent=styles["Title"],

        alignment=1,

        fontSize=26,

        textColor=colors.HexColor("#D4AF37")

    )






    heading_style = ParagraphStyle(

        "heading",

        parent=styles["Heading2"],

        textColor=colors.HexColor("#D4AF37")

    )






    normal_style = ParagraphStyle(

        "normal",

        parent=styles["Normal"],

        fontSize=10,

        leading=15

    )





    content=[]






    # CREATE GRAPH



    chart = create_threat_chart(

        sender,

        urls,

        keywords,

        headers,

        attachments

    )







    # COVER



    content.append(

        Paragraph(

            "◈ PHISHSCOPE",

            title_style

        )

    )



    content.append(

        Paragraph(

            "CYBER INTELLIGENCE PLATFORM",

            normal_style

        )

    )



    content.append(

        Spacer(1,30)

    )




    content.append(

        Paragraph(

            "PHISHING EMAIL SECURITY ASSESSMENT REPORT",

            heading_style

        )

    )




    content.append(

        Paragraph(

            f"Generated: {datetime.now()}",

            normal_style

        )

    )





    content.append(

        Spacer(1,30)

    )









    # THREAT SCORE



    score_table = Table(

        [

            [

            "Threat Score",

            str(risk["score"]) + "/100"

            ],


            [

            "Risk Level",

            risk["level"]

            ]

        ],


        colWidths=[180,200]

    )




    score_table.setStyle(

        TableStyle(

            [

            (

            "GRID",

            (0,0),

            (-1,-1),

            0.5,

            colors.grey

            ),



            (

            "BACKGROUND",

            (0,0),

            (0,-1),

            colors.HexColor("#E8DCC4")

            )

            ]

        )

    )



    content.append(score_table)






    content.append(

        Spacer(1,25)

    )







    # GRAPH



    content.append(

        Paragraph(

            "Threat Visualization",

            heading_style

        )

    )



    content.append(

        Image(

            chart,

            width=400,

            height=220

        )

    )







    content.append(

        Spacer(1,20)

    )









    # EMAIL DATA



    content.append(

        Paragraph(

            "Email Intelligence",

            heading_style

        )

    )





    email_table = Table(

        [

            [

            "Sender",

            email["sender"]

            ],


            [

            "Receiver",

            email["receiver"]

            ],


            [

            "Subject",

            email["subject"]

            ]

        ],


        colWidths=[120,300]

    )





    email_table.setStyle(

        TableStyle(

            [

            (

            "GRID",

            (0,0),

            (-1,-1),

            .5,

            colors.grey

            )

            ]

        )

    )





    content.append(email_table)







    # HELPER FUNCTION



    def add_section(title,items):


        content.append(

            Paragraph(

                title,

                heading_style

            )

        )


        for item in items:


            content.append(

                Paragraph(

                    "• "+str(item),

                    normal_style

                )

            )


        content.append(

            Spacer(1,15)

        )







    add_section(

        "Sender Analysis",

        sender["findings"]

    )



    add_section(

        "Keyword Findings",

        keywords["findings"]

    )



    add_section(

        "Header Analysis",

        headers["findings"]

    )







    # URL SECTION



    content.append(

        Paragraph(

            "URL Intelligence",

            heading_style

        )

    )





    for item in urls["urls"]:


        content.append(

            Paragraph(

                item["url"],

                normal_style

            )

        )






    # IOC SECTION



    ioc_list=[]



    for url in iocs["urls"]:


        ioc_list.append(

            "URL: "+url

        )



    for ip in iocs["ips"]:


        ioc_list.append(

            "IP: "+ip

        )




    add_section(

        "Indicators Of Compromise",

        ioc_list

    )







    add_section(

        "Security Recommendations",

        risk["recommendations"]

    )







    content.append(

        Spacer(1,30)

    )





    content.append(

        Paragraph(

            "PHISHSCOPE © 2026 | Confidential Cybersecurity Report",

            normal_style

        )

    )






    doc.build(

        content

    )



    return path