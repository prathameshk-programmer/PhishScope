
def calculate_risk(

    sender,

    urls,

    keywords,

    headers,

    attachments

):


    score = (

        sender["score"]

        +

        urls["score"]

        +

        keywords["score"]

        +

        headers["score"]

        +

        attachments["score"]

    )



    if score >= 80:

        level = "Critical"


    elif score >= 50:

        level = "High"


    elif score >= 25:

        level = "Medium"


    elif score > 0:

        level = "Low"


    else:

        level = "Safe"



    recommendations = []



    if score > 0:

        recommendations.append(

            "Do not click suspicious links"

        )


        recommendations.append(

            "Verify sender identity before responding"

        )


        recommendations.append(

            "Avoid opening unknown attachments"

        )


    else:


        recommendations.append(

            "No major threats detected"

        )



    return {


        "score": score,


        "level": level,


        "recommendations": recommendations


    }