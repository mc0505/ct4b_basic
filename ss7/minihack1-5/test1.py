import random
import operator
def random_problems():
    operators={
        "-": operator.sub,
        "+": operator.add,
    }

    num_1 = random.randint(1,50)
    num_2 = random.randint(1,50)
    num_3 = random.randint(1,50)
    operation = random.choice(list(operators.keys()))
    answer1 = operators.get(operation) (num_1,num_2)
    answer2= operators.get(operation)(answer1, num_3)
    c= (f"{answer1} {operation} {num_3} = {answer2}")
    a = (f"Is {num_1} {operation} {num_2} = {answer1}?")
    b = (f"Is {num_1} {operation} {num_2} = {answer2}?")
    n= [a,b]
    print(random.choice(n))
    
def true_or_false():
    answer = random_problems()
    choices = ["T","F"]
    guess = input("Is the problem (T)rue of (F)alse? ")
    return  guess == answer

"""def game():
    print("Freaking Math!!\n")
    while True:
        if 
        
        print("Correct!"
game()"""
