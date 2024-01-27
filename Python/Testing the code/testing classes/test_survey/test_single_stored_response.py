from survey import AnonymousSurvey

# testing the single response
def test_stored_reponse():
    question = "What is the first language you have learnt?"
    lang_survey = AnonymousSurvey(question)
    lang_survey.store_response('English')
    assert 'English' in lang_survey.responses

#testing the three responses
def test_multi_stored_responses():
    question = "What is the first languages you have learnt?"
    lang_survey = AnonymousSurvey(question)
    responses = ['English','Kannada','Hindi']
    for response in responses:
        lang_survey.store_response(response)
        assert response in responses
