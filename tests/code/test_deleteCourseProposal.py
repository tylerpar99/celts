import pytest
from peewee import DoesNotExist
from app.logic.deleteCourseProposal import deleteCourseProposal
from app.models.course import Course

@pytest.mark.integration
def test_deleteCourseProposal():
    numCourse = len(Course.select())
    deleteCourse = deleteCourseProposal(2)
    updatedNumCourse = len(Course.select())

    assert updatedNumCourse == numCourse - 1
