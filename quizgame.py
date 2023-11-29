
def question(question, possible_answers, answer, score):
    print(f'{question}\n{possible_answers}')
    player_answer = input()
    if player_answer == answer:
        print("correct!")
        score += 1
    else:
        print(f"wrong, the correct answer was {answer}")
    return score

def quiz():
    score = 0
    
    score = question("what is 9 + 9?", "a) 21\nb) 18\nc) 99", "b", score)

    score = question("what is 9 + 10?", "a) 21\nb) 18\nc) 19", "c", score)

    print(F"your final score is {score}")
    
if __name__ == "__main__":
    quiz()
