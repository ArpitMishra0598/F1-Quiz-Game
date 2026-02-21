import time
import threading

def timed_input(prompt, timeout=15):
    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\n Time's up for this question!")
        return None
    return answer[0]


def run_quiz(questions, nerd_mode=False):
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)

        if nerd_mode:
            user_answer = timed_input("Your answer (A/B/C/D): ", 15)
        else:
            user_answer = input("Your answer (A/B/C/D): ")

        if user_answer is None:
            print(f" Skipped! Correct answer: {q['answer']}")
        elif user_answer.upper() == q['answer']:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['answer']}")

    return score


# ================= EASY (10 Questions) =================
easy_questions = [
    {"question": "Which company makes Ferrari F1 engines?",
     "options": ["A. Mercedes", "B. Ferrari", "C. Renault", "D. Honda"],
     "answer": "B"},

    {"question": "How many drivers are in an F1 team?",
     "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
     "answer": "B"},

    {"question": "What color is Ferrari traditionally?",
     "options": ["A. Blue", "B. Yellow", "C. Red", "D. Black"],
     "answer": "C"},

    {"question": "Who is a 7-time world champion?",
     "options": ["A. Max Verstappen", "B. Lewis Hamilton", "C. Lando Norris", "D. Charles Leclerc"],
     "answer": "B"},

    {"question": "What does DRS stand for?",
     "options": ["A. Drag Reduction System", "B. Driver Racing Speed", "C. Downforce Racing System", "D. Dynamic Racing Setup"],
     "answer": "A"},

    {"question": "Which country hosts the Monaco GP?",
     "options": ["A. France", "B. Italy", "C. Monaco", "D. Spain"],
     "answer": "C"},

    {"question": "Which tyre brand supplies F1?",
     "options": ["A. Michelin", "B. Pirelli", "C. Bridgestone", "D. Goodyear"],
     "answer": "B"},

    {"question": "How many points for race win?",
     "options": ["A. 18", "B. 20", "C. 25", "D. 30"],
     "answer": "C"},

    {"question": "How many teams are on the current grid (approx)?",
     "options": ["A. 8", "B. 9", "C. 10", "D. 12"],
     "answer": "C"},

    {"question": "Which session decides pole position?",
     "options": ["A. Practice", "B. Sprint", "C. Warmup", "D. Qualifying"],
     "answer": "D"}
]

# ================= MEDIUM (10 Questions) =================
medium_questions = [
    {"question": "Who won the 2021 World Championship?",
     "options": ["A. Hamilton", "B. Verstappen", "C. Bottas", "D. Perez"],
     "answer": "B"},

    {"question": "Which team is based in Brackley?",
     "options": ["A. Ferrari", "B. Red Bull", "C. Mercedes", "D. McLaren"],
     "answer": "C"},

    {"question": "What engine does Red Bull currently use?",
     "options": ["A. Ferrari", "B. Mercedes", "C. Renault", "D. Honda"],
     "answer": "D"},

    {"question": "Which driver is known as 'The Iceman'?",
     "options": ["A. Kimi Raikkonen", "B. Alonso", "C. Vettel", "D. Ricciardo"],
     "answer": "A"},

    {"question": "Which track is called Temple of Speed?",
     "options": ["A. Silverstone", "B. Monza", "C. Spa", "D. Suzuka"],
     "answer": "B"},

    {"question": "Youngest race winner?",
     "options": ["A. Vettel", "B. Verstappen", "C. Leclerc", "D. Alonso"],
     "answer": "B"},

    {"question": "Which circuit has Eau Rouge?",
     "options": ["A. Monaco", "B. Spa", "C. Suzuka", "D. Baku"],
     "answer": "B"},

    {"question": "Hybrid era started in?",
     "options": ["A. 2012", "B. 2013", "C. 2014", "D. 2015"],
     "answer": "C"},

    {"question": "Which team is Papaya colored?",
     "options": ["A. Ferrari", "B. McLaren", "C. Alpine", "D. Haas"],
     "answer": "B"},

    {"question": "Home race of Mercedes?",
     "options": ["A. British GP", "B. German GP", "C. Italian GP", "D. Austrian GP"],
     "answer": "B"}
]

# ================= HARD (10 Questions) =================
hard_questions = [
    {"question": "Who won 2016 title?",
     "options": ["A. Hamilton", "B. Rosberg", "C. Vettel", "D. Button"],
     "answer": "B"},

    {"question": "First night race?",
     "options": ["A. Abu Dhabi", "B. Singapore", "C. Bahrain", "D. Qatar"],
     "answer": "B"},

    {"question": "Who won 2008 title?",
     "options": ["A. Massa", "B. Hamilton", "C. Raikkonen", "D. Alonso"],
     "answer": "B"},

    {"question": "Schumacher first title year?",
     "options": ["A. 1992", "B. 1994", "C. 1996", "D. 1998"],
     "answer": "B"},

    {"question": "Which team became Aston Martin?",
     "options": ["A. Force India", "B. Lotus", "C. Toro Rosso", "D. Sauber"],
     "answer": "A"},

    {"question": "Driver with most poles?",
     "options": ["A. Schumacher", "B. Hamilton", "C. Senna", "D. Vettel"],
     "answer": "B"},

    {"question": "Alonso debut team?",
     "options": ["A. Renault", "B. Minardi", "C. Ferrari", "D. McLaren"],
     "answer": "B"},

    {"question": "Which track has 130R corner?",
     "options": ["A. Suzuka", "B. Monza", "C. Spa", "D. Silverstone"],
     "answer": "A"},

    {"question": "Brawn GP won championship in?",
     "options": ["A. 2008", "B. 2009", "C. 2010", "D. 2011"],
     "answer": "B"},

    {"question": "Last Williams win?",
     "options": ["A. Bottas", "B. Maldonado", "C. Massa", "D. Rosberg"],
     "answer": "B"}
]

# ================= NERD TEST (10 Questions - 15 sec each) =================
nerd_questions = [
    {"question": "1982 World Champion?",
     "options": ["A. Prost", "B. Lauda", "C. Rosberg", "D. Piquet"],
     "answer": "C"},

    {"question": "Which team introduced F-duct?",
     "options": ["A. Ferrari", "B. Red Bull", "C. McLaren", "D. Mercedes"],
     "answer": "C"},

    {"question": "Most points without race win?",
     "options": ["A. Hulkenberg", "B. Heidfeld", "C. Perez", "D. Grosjean"],
     "answer": "B"},

    {"question": "First title for Senna was with?",
     "options": ["A. McLaren", "B. Lotus", "C. Williams", "D. Ferrari"],
     "answer": "A"},

    {"question": "Sakhir GP used which layout?",
     "options": ["A. Full", "B. Outer", "C. Endurance", "D. Short"],
     "answer": "B"},

    {"question": "Ferrari last constructors title?",
     "options": ["A. 2006", "B. 2007", "C. 2008", "D. 2009"],
     "answer": "C"},

    {"question": "First Indian F1 driver?",
     "options": ["A. Narain Karthikeyan", "B. Karun Chandhok", "C. Jehan Daruvala", "D. None"],
     "answer": "A"},

    {"question": "Which driver had 9 consecutive wins (2013)?",
     "options": ["A. Hamilton", "B. Vettel", "C. Alonso", "D. Rosberg"],
     "answer": "B"},

    {"question": "Which year was refueling banned?",
     "options": ["A. 2008", "B. 2009", "C. 2010", "D. 2011"],
     "answer": "C"},

    {"question": "Which circuit hosted 70th Anniversary GP?",
     "options": ["A. Silverstone", "B. Spa", "C. Monza", "D. Austria"],
     "answer": "A"}
]


# ================= MAIN =================
print("🏎️ Welcome to the F1 Quiz Game!")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Nerd Test (15 sec per question)")

choice = input("Choose difficulty (1-4): ")

if choice == "1":
    score = run_quiz(easy_questions)
elif choice == "2":
    score = run_quiz(medium_questions)
elif choice == "3":
    score = run_quiz(hard_questions)
elif choice == "4":
    print("\n Nerd Test Mode Activated! 15 seconds per question!")
    score = run_quiz(nerd_questions, nerd_mode=True)
else:
    print("Invalid choice.")
    exit()

print(f"\n Final Score: {score}/10")

if score == 10:
    print(" F1 GOD LEVEL UNLOCKED!")
elif score >= 7:
    print(" Hardcore F1 Fan!")
elif score >= 4:
    print(" Solid Knowledge!")
else:
    print(" Time to rewatch some races!")