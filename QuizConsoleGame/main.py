questions = (
    "1. Who is considered the national hero of the Philippines?",
    "2. When did the Philippines gain independence from Spanish colonization?",
    "3. What is the oldest city in the Philippines?",
    "4. Who was the first President of the Philippines?",
    "5. What event marked the beginning of World War II in the Philippines?",
    "6. Which Philippine national hero is known as the 'Sublime Paralytic'?",
    "7. What is the significance of the EDSA People Power Revolution?",
    "8. Who led the Katipunan, a revolutionary society against Spanish colonization?",
    "9. What is the name of the treaty that ceded the Philippines to the United States in 1898?",
    "10. Who was the first Filipino woman to become President of the Philippines?",
    "11. What is the name of the ancient script used by early Filipinos?",
    "12. Which Philippine president declared martial law in 1972?",
    "13. What battle during World War II is known as the 'Great Raid'?",
    "14. Who is known as the 'Father of Philippine Revolution'?",
    "15. What is the national flower of the Philippines?",
    "16. Which Philippine province is known for the Banaue Rice Terraces?",
    "17. What is the longest-running armed conflict in Philippine history?",
    "18. Who composed the music for the Philippine national anthem?",
    "19. What is the name of the famous ship that brought the first Filipinos to North America in 1587?",
    "20. Who was the leader of the Moro Islamic Liberation Front (MILF) in the late 20th century?",
)

options = (
    ("A. Jose Rizal", "B. Andres Bonifacio", "C. Emilio Aguinaldo", "D. Manuel Quezon"),
    ("A. 1888", "B. 1896", "C. 1898", "D. 1901"),
    ("A. Cebu City", "B. Manila", "C. Intramuros", "D. Vigan"),
    ("A. Manuel Quezon", "B. Emilio Aguinaldo", "C. Ferdinand Marcos", "D. Corazon Aquino"),
    ("A. Attack on Pearl Harbor", "B. Battle of Bataan", "C. Bombing of Manila", "D. Battle of Leyte Gulf"),
    ("A. Andres Bonifacio", "B. Jose Rizal", "C. Apolinario Mabini", "D. Emilio Aguinaldo"),
    ("A. Establishment of the First Philippine Republic", "B. Assassination of Ninoy Aquino", "C. People Power Revolution", "D. Declaration of Martial Law"),
    ("A. Andres Bonifacio", "B. Emilio Aguinaldo", "C. Apolinario Mabini", "D. Jose Rizal"),
    ("A. Treaty of Paris", "B. Treaty of Tordesillas", "C. Treaty of Versailles", "D. Treaty of Manila"),
    ("A. Gloria Macapagal-Arroyo", "B. Corazon Aquino", "C. Imelda Marcos", "D. Benigno Aquino III"),
    ("A. Alibata", "B. Baybayin", "C. Kulitan", "D. Hanunoo"),
    ("A. Ferdinand Marcos", "B. Corazon Aquino", "C. Gloria Macapagal-Arroyo", "D. Joseph Estrada"),
    ("A. Battle of Corregidor", "B. Battle of Leyte Gulf", "C. Bataan Death March", "D. Raid at Cabanatuan"),
    ("A. Andres Bonifacio", "B. Emilio Aguinaldo", "C. Jose Rizal", "D. Marcelo H. del Pilar"),
    ("A. Sampaguita", "B. Orchid", "C. Rose", "D. Sunflower"),
    ("A. Benguet", "B. Ifugao", "C. Mountain Province", "D. Palawan"),
    ("A. Moro Rebellion", "B. Communist Insurgency", "C. Filipino-American War", "D. Japanese Occupation"),
    ("A. Jose Rizal", "B. Andres Bonifacio", "C. Julian Felipe", "D. Juan Luna"),
    ("A. San Juan Bautista", "B. Santa Maria", "C. Santa Ana", "D. San Lorenzo"),
    ("A. Francisco Dagohoy", "B. Sultan Kudarat", "C. Nur Misuari", "D. Hashim Salamat"),
)

answers = ("A","C","B","B","A","A","C","A","A","B","B","A","D","A","A","B","B","C","C","D",)

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")