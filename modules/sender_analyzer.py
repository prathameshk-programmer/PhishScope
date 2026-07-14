import re


FREE_EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com"
]


def analyze_sender(email_data):

    sender = email_data["sender"].lower()

    result = {

        "score": 0,

        "level": "Safe",

        "findings": []

    }


    # Extract domain

    match = re.search(
        r"@([\w\.-]+)",
        sender
    )


    if match:

        domain = match.group(1)


        if domain in FREE_EMAIL_DOMAINS:

            result["score"] += 20

            result["findings"].append(
                "Sender uses a free email provider"
            )



    else:

        result["score"] += 15

        result["findings"].append(
            "Unable to identify sender domain"
        )



    if "noreply" in sender or "security" in sender:

        result["score"] += 5

        result["findings"].append(
            "Sender name may impersonate a trusted service"
        )



    if result["score"] >= 40:

        result["level"] = "High"

    elif result["score"] >= 20:

        result["level"] = "Medium"

    elif result["score"] > 0:

        result["level"] = "Low"



    return result