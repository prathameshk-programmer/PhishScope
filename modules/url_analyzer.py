import re
from urllib.parse import urlparse



SUSPICIOUS_TLDS = [

    ".xyz",
    ".top",
    ".click",
    ".online"

]


def analyze_urls(text):


    urls = re.findall(

        r"https?://[^\s]+",

        text

    )


    result = {

        "score": 0,

        "level": "Safe",

        "urls": [],

        "findings": []

    }



    for url in urls:


        issues = []

        score = 0


        domain = urlparse(url).netloc



        if url.startswith("http://"):

            score += 10

            issues.append(
                "Uses insecure HTTP connection"
            )



        for tld in SUSPICIOUS_TLDS:


            if domain.endswith(tld):

                score += 20

                issues.append(
                    "Suspicious domain extension"
                )



        result["score"] += score



        result["urls"].append({

            "url": url,

            "issues": issues

        })



    if result["score"] >= 40:

        result["level"] = "High"

    elif result["score"] >= 20:

        result["level"] = "Medium"

    elif result["score"] > 0:

        result["level"] = "Low"



    return result