from app.models.course import Course
def deleteCourseProposal(courseID):
    courseID = Course.get_by_id(courseID)
    print("Course ID",courseID)
    courses = Course.select()

    print(list(courses))
    for course in courses:
        print(type(course), "type of course")
        print(course.courseName)
        print("course ID",type(course.id),type(courseID.id))
        print("Course Status ID",type(course.status_id))

        if course.id == courseID.id and course.status_id == 2:
            print("Inside the for loop ")
            # course.delete_instance()
            print("deletion was successul")
