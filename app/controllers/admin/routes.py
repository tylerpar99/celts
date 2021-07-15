from flask import request, render_template
from flask import Flask, redirect, flash
from app.models.event import Event
from app.logic.trackVolunteerHours import prereqParticipants

from app.controllers.admin import admin_bp
from app.models.eventParticipant import EventParticipant

@admin_bp.route('/testing', methods=['GET'])
def testing():
    return "<h1>Hello</h1>"

@admin_bp.route('/<programID>/<eventID>/track_hours', methods=['GET'])
def trackVolunteerHoursPage(programID, eventID):

    eventParticipantsData = (EventParticipant.select(EventParticipant)
                                .join(Event)
                                .where((EventParticipant.event == eventID) & (Event.program == programID)))

    prereqEvents = Event.select().where(Event.program == programID)

    prlist = [prereq.id for prereq in prereqEvents if prereq.isPrerequisiteForProgram]
    attendedPreq = prereqParticipants(programID, prlist)

    return render_template("/events/trackVolunteerHours.html",
                            eventParticipantsData = list(eventParticipantsData.objects()),
                            attendedPreq=attendedPreq,
                            prlist = prlist )
