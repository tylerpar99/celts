from flask import request, render_template
from flask import json, jsonify
from app.models.program import Program
from app.models.user import User
from app.models.interest import Interest

from app.controllers.main import main_bp

current_user = User.get(User.username == "escalerapadronl") #FIXME: Remove once authentication is built

@main_bp.route('/volunteerIndicateInterest', methods = ['GET'])
def volunteerIndicateInterest():
    programs = Program.select()
    interests = Interest.select().where(Interest.user_id == current_user.username)
    interests_ids = [interest.program_id for interest in interests]
    return render_template('volunteerIndicateInterest.html',
                           title="Volunteer Interest",
                           user = current_user,
                           programs = programs,
                           interests = interests,
                           interests_ids = interests_ids)

@main_bp.route('/addInterest/<program_id>/<userID>', methods = ['POST'])
def addInterest(program_id, userID):
    """
    This function updates the interest table by adding a new row when a user
    shows interest in a program
    """
    try:
        Interest.get_or_create(program = program_id, user = current_user.username)
        return jsonify({"Success": True})
    except Exception as e:
        print("Error Updating Interest: ", e)
        return jsonify({"Success": False}),500

@main_bp.route('/deleteInterest/<program_id>/<userID>', methods = ['POST'])
def deleteInterest(program_id, userID):
    """
    This function updates the interest table by removing a row when the user
    removes interest from a program
    """
    try:
        deleted_interest = Interest.get(Interest.program == program_id and Interest.user == current_user.username)
        deleted_interest.delete_instance()
        return jsonify({"Success": True})
    except Exception as e:
        print("Error Updating Interest: ", e)
        return jsonify({"Success": False}),500
