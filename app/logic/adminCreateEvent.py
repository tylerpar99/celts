from app.models import*
from app.models.term import Term
from app.models.user import User

def getTermDescription():

    termDescription = Term.select(Term.description)

    description = [des.description for des in termDescription.objects()]

    return description

def getFacilitators():

    facilitators = User.select(User).where((User.isFaculty == 1) | (User.isCeltsAdmin == 1) | (User.isCeltsStudentStaff == 1))

    listOfFacilitators = [fac for fac in facilitators.objects()]

    return listOfFacilitators