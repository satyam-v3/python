questions = [
    ["What is the capital of India?", "Mumbai", "Chennai", "New Delhi", "Kolkata", "None", 3],
    ["What is the colour of an Emerald?", "Blue", "Green", "Red", "Yellow", "None", 2],
    ["Which animal is known as 'Ship of the Desert'?", "Horse", "Camel", "Elephant", "Lion", "None", 2],
    ["Who wrote the Indian national anthem 'Jana Gana Mana'?", "Mahatma Gandhi", "Rabindranath Tagore", "Sarojini Naidu", "Subhash Chandra Bose", "None", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "None", 2],
    ["Which Indian city is known as the 'Silicon Valley of India'?", "Hyderabad", "Mumbai", "Bengaluru", "Pune", "None", 3],
    ["Who was the first woman to win a Nobel Prize?", "Mother Teresa", "Indira Gandhi", "Marie Curie", "Jane Austen", "None", 3],
    ["Which element is said to keep bones strong?", "Oxygen", "Calcium", "Iron", "Sodium", "None", 2],
    ["In which year did India gain independence from British rule?", "1942", "1945", "1947", "1950", "None", 3],
    ["Who is known as the 'Father of the Indian Constitution'?", "Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Sardar Patel", "None", 3],
    ["Which Indian classical dance form originated in Tamil Nadu?", "Kathak", "Bharatanatyam", "Kathakali", "Odissi", "None", 2],
    ["Which is the largest freshwater lake in India?", "Wular Lake", "Dal Lake", "Chilika Lake", "Loktak Lake", "None", 1],
    ["Who is the author of the Harry Potter series?", "J. K. Rowling", "J. R. R. Tolkien", "George R. R. Martin", "Suzanne Collins", "None", 1],
    ["Which Mughal emperor commissioned the construction of the Taj Mahal?", "Akbar", "Jahangir", "Shah Jahan", "Aurangzeb", "None", 3],
    ["What is the name of the first satellite launched by India?", "INSAT-1A", "Aryabhata", "Bhaskara", "Rohini", "None", 2],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for ₹{levels[i]}")
    print(f"{i + 1}: {question[0]}")
    print(f"\ta. {question[1]}      b. {question[2]}")
    print(f"\tc. {question[3]}      d. {question[4]}\n")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))

    if reply == 0:
        money = levels[i - 1] if i > 0 else 0
        break

    if reply == question[-1]:
        print(f"Correct answer! You have won ₹{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer!")
        money = 0 if i < 5 else 10000 if i < 10 else 320000
        break

print(f"Your take-home money is ₹{money}\n")
