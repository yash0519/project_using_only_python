questions = [
    ["1.Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["2.What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["3.Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["4.What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["5.Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["6.What is the square root of 64?", "8", "10", "6", "12", 1],
    ["7.Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["8.Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["9.What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["10.Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["11.What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

price=[0,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,]

i=0
sum=0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    any=int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    
    if any == question[5]:
        print("Correct Answer") 
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break 
    i=i+1
    sum=sum+price[i]
    print(f"you won {sum}")