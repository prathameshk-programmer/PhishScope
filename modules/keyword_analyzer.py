SUSPICIOUS_WORDS = {


    "urgent": 10,

    "verify": 10,

    "password": 15,

    "account": 5,

    "login": 10,

    "payment": 10,

    "suspended": 15,

    "click here": 15,

    "winner": 10

}



def analyze_keywords(text):


    text = text.lower()


    result = {

        "score": 0,

        "level": "Safe",

        "findings": []

    }



    for word, points in SUSPICIOUS_WORDS.items():


        if word in text:


            result["score"] += points


            result["findings"].append(

                f"Suspicious keyword detected: {word}"

            )



    if result["score"] >= 40:

        result["level"] = "High"

    elif result["score"] >= 20:

        result["level"] = "Medium"

    elif result["score"] > 0:

        result["level"] = "Low"



    return result