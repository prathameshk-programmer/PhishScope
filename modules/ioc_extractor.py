import re
from urllib.parse import urlparse



def extract_iocs(email_data):


    text = (

        email_data["body"]

        + " "

        + email_data["sender"]

    )


    urls = re.findall(

        r"https?://[^\s]+",

        text

    )


    emails = re.findall(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        text

    )


    ips = re.findall(

        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",

        text

    )



    domains=[]


    for url in urls:


        try:

            domain = urlparse(url).netloc

            domains.append(domain)

        except:

            pass



    return {


        "urls": list(set(urls)),


        "domains": list(set(domains)),


        "emails": list(set(emails)),


        "ips": list(set(ips))


    }