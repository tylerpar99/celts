from app.models.course import Course
def deleteCourseProposal(courseID):
    courseID = Course.get_by_id(courseID)
    courses = Course.select()
    # course = Course.select().where(Course.id == courseID and Course.status_id ==2)
    # print("Course",course.courseName)
    # q = Course.delete().where(Course.id == courseID and Course.status_id ==2)
    # q.execute()
    for course in courses:
        if course.id == courseID.id and course.status_id == 2:
            print("Inside the for loop ")
            # course.delete_instance()
            course = Course.get(Course.id ==courseID)
            course.delete_instance()
            print("deletion was successul")
        else:
            print("Not this time")
