import os


DANGEROUS_FILES = [

    ".exe",
    ".bat",
    ".cmd",
    ".ps1",
    ".vbs",
    ".js"

]



def analyze_attachments(files):


    result = {

        "score":0,

        "level":"Safe",

        "findings":[],

        "files":[]

    }



    for file in files:


        issues=[]

        score=0


        extension = os.path.splitext(file)[1].lower()



        if extension in DANGEROUS_FILES:


            score += 40

            issues.append(

                "Dangerous executable attachment"

            )



        if ".pdf.exe" in file.lower():


            score += 40

            issues.append(

                "Double extension attack detected"

            )



        result["score"] += score



        result["files"].append({

            "name":file,

            "issues":issues

        })



    if result["score"] >= 40:

        result["level"]="High"


    elif result["score"] > 0:

        result["level"]="Medium"



    return result