import pytest
from survey import AnonymousSurvey

@pytest.fixture
def lang_survey():
    question = "What is the first language you have learnt?"
    lang_survey = AnonymousSurvey(question)
    return lang_survey

# testing the single response
def test_stored_reponse(lang_survey):
    lang_survey.store_response('English')
    assert 'English' in lang_survey.responses

#testing the three responses
def test_multi_stored_responses(lang_survey):
    responses = ['English','Kannada','Hindi']
    for response in responses:
        lang_survey.store_response(response)
        assert response in responses
