from email import policy
from email.parser import BytesParser



def parse_email(filepath):

    with open(
        filepath,
        "rb"
    ) as file:

        message = BytesParser(
            policy=policy.default
        ).parse(file)



    data = {

        "sender": message.get(
            "From",
            "Unknown"
        ),

        "receiver": message.get(
            "To",
            "Unknown"
        ),

        "subject": message.get(
            "Subject",
            "No Subject"
        ),

        "body": "",

        "headers": {},

        "attachments": []

    }



    for key,value in message.items():

        data["headers"][key] = value



    if message.is_multipart():


        for part in message.walk():


            disposition = str(
                part.get(
                    "Content-Disposition"
                )
            )


            if "attachment" in disposition:


                filename = part.get_filename()


                if filename:

                    data["attachments"].append(
                        filename
                    )


            elif part.get_content_type() == "text/plain":


                try:

                    data["body"] += part.get_content()

                except:

                    pass



    else:

        data["body"] = message.get_content()



    return data