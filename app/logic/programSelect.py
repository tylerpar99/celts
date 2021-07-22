from app.models.term import Term
from app.controllers.admin import admin_bp
from app.logic.getAllFacilitators import getAllFacilitators
from flask import flash, redirect, url_for, g

def eventElements():
    listOfTerms = Term.select()
    facilitators = getAllFacilitators()
    eventElementsDict = {"term": listOfTerms, "facilitators": facilitators}

    return eventElementsDict

def programTemplates(programChoice, createEventsDict):

    if programChoice == "allVolunteerTraining":
        allVolunteerTraining = {   "isRequired": "checked",
                                    "isRecurring": "hidden",
                                    "isService": "",
                                    "isTraining": "checked",
                                    "program": "All Volunteer Training"}
        return allVolunteerTraining

    if programChoice == "studentLedProgramsTraining":
        studentLedProgramsTraining = {  "isRequired": "checked",
                                        "isService": "checked",
                                        "isRecurring": "checkbox",
                                        "isTraining": "checked",
                                        "program": "Student Led Programs Training"
                                        }
        return studentLedProgramsTraining


    else:
        generalCreateEventsDict = {     "isRequired": "",
                                        "isService": "",
                                        "isRecurring": "checkbox",
                                        "isTraining": "",
                                        "program": createEventsDict.get("program")
                                        }
        return generalCreateEventsDict
