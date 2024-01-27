from survey import AnonymousSurvey

# define the question and make a survey
question = "What is your first langauge you have learnt"
lang_survey = AnonymousSurvey(question)

# showing the question and storing the responses
lang_survey.show_question()
print("Want to quit the survey enter 'q':")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    lang_survey.store_response(response)

# displaying the responses
print("Thank you for sharing your thoughts.")
lang_survey.show_result()
