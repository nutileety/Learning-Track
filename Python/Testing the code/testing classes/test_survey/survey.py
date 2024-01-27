class AnonymousSurvey:
    def __init__(self,question):
        # store a question and preparing to store responses
        self.question = question
        self.responses = []

    def show_question(self):
        # showing the servey question
        print(self.question)

    def store_response(self,new_response):
        # storing the responses in a list
        self.responses.append(new_response)

    def show_result(self):
        # showing the resopnsing of the user by loopin each response in list
        print("The Responses are:")
        for response in self.responses:
            print(f"{response}")
