from app.models.course import Course

def deleteCourseProposal(course_id):

    courseID = Course.get_by_id(course_id)
    # the status id of 2 (pending) or status id of 4 (reuqires edit)
    course = Course.get(Course.id == courseID and Course.status_id == 2 or Course.status_id == 4)
    course.delete_instance(recursive=True)
