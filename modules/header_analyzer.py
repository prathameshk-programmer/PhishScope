
def analyze_headers(headers):


    result = {

        "score": 0,

        "level": "Safe",

        "findings": []

    }



    received = headers.get(
        "Received",
        ""
    )


    if not received:


        result["score"] += 10

        result["findings"].append(

            "Missing email routing information"

        )



    spf = headers.get(
        "Authentication-Results",
        ""
    ).lower()



    if "fail" in spf:


        result["score"] += 25

        result["findings"].append(

            "Email authentication failed"

        )



    if result["score"] >= 40:

        result["level"] = "High"


    elif result["score"] >= 20:

        result["level"] = "Medium"


    elif result["score"] > 0:

        result["level"] = "Low"



    return result