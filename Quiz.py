from QuestionsClass import Question
questions_prompt = [
    "What is the capital of Bangladesh?\n (a)Dhaka\n (b)Chittagong\n (c) Comilla\n",
    "Who is the president of Bangladesh?\n (a)Abal\n (b)Abdul Hamid\n (c)Shekh Hasina\n",
    "What University is the 'no 1' private university in Bangladesh?\n (a) Berak University\n (b)BRAK Universiti\n (c)BrAc UnIvErSiTy\n"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c")
]

def run_test(questionss):
    score_count = 0
    for question in questionss:
        answer = input(question.prompt)
        if answer == question.answer:
            score_count += 1
    print("You got " + str(score_count) + " / " + str(len(questions)))

run_test(questions)