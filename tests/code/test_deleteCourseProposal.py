import pytest
from peewee import DoesNotExist
from app.logic.deleteCourseProposal import deleteCourseProposal


@pytest.mark.integration
def test_deleteCourseProposal():

    deleteCourse = deleteCourseProposal(2)

    assert deleteCourse
