#make a dictionary that the keys are question and the items are the answers
quiz = {
    "question1":{
        "question": "What is the capital of France",
        "answer": "Paris"
    },
    "question 2":{
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "question 3":{
        "question": "What is the capital of Italy",
        "answer": "Rome"
        
    },
    "question 4":{
        "question": "What is the capital of Spain",
        "answer": "Madrid"
        
    },
    "question 5":{
        "question": "What is the capital of Portugal",
        "answer": "Lisbon"
        
    },
    "question 6":{
        "question": "What is the capital of Switzerland",
        "answer": "Bern"
        
    },
    "question 7":{
        "question": "What is the capital of Austia",
        "answer": "Vienna"
    },
}
#this is the deafault score variable and it's zero
score = 0
#here we create a for loop 
for key, value in quiz.items():
#here it prints our question
    print(value["question"])
#here it prints the answer with ? and prompts us for our input
    answer = input("Answer? ")
#here we want to make sure the player doesn't lost point just because he wrote the asnwer with lower case  
    if answer.lower() == value["answer"].lower():
#here it prints correct if the answer is correct
        print("Correct")
#here we add 1 to the score variable 
        score = score + 1
#here it prints our total score
        print("Your score is " + str(score))
#here we make the case that the player lost and it prints wrong and the score stays the same
    else:
        print("Wrong")
        print("Your answer is:" + value["answer"])
        print("Your score is" + str(score))

