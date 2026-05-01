# could do % wise personalities
# could do visualizations

def personality_quiz():

    scores = {
         "A":0,
         "B":0,
         "C":0,
         "D":0
    }

quiz = [
    {
        "question": "Where do you want to live in five years?",
        "answers": {
            "A": "A large, busy city.",
            "B": "A small, mysterious coastal town.",
            "C": "A cabin in the woods.",
            "D": "'Nowehere, I want to move around for a bit.'"
        }
    },
    {
        "question": "Where is your dream vacation?",
        "answers": {
            "A": "A touristy metropolitan area with fine dining and historical sites.",
            "B": "A cozy winter cabin with a group of people.",
            "C": "A book on a beach recliner near the shore.",
            "D": "An expensive mountain or tropical resort."
        }
    },
     {
        "question": "You have a bit of extra money to spend, what will you use it for?",
        "answers": {
            "A": "'Maybe some new clothes, high end one if I can afford them.'",
            "B": "'Gift shopping, maybe pay off some bills.'",
            "C": "'I think I'll hang on to my money for a bit and save up.'",
            "D": "'Tickets for travel!"
        }
    },
     {
        "question": "You have an exam. How are you preparing?",
        "answers": {
            "A": "Start preparing weeks before hand with flashcards and loads of caffine.",
            "B": "Set up a small study group and work together.",
            "C": "Start studying a few days in advance, you already know most of the material.",
            "D": "Ask the professor and your classmates what you should look at and focas on those topics."
        }
    },
     {
        "question": "What's your drink of choice?",
        "answers": {
            "A": "'Coffee, coffee and more coffee.'",
            "B": "'Just tea!'",
            "C": "'I feel like I should drink more water.'",
            "D": "'Any kind of energy drink.'"
        }
    },
     {
        "question": "How do you distress after a long day?",
        "answers": {
            "A": "'I dont, my body hasen't left fight or flight in three years.'",
            "B": "'Rest, chat with my friends, maybe shower.",
            "C": "'Game for a bit and watch a movie with snacks.'",
            "D": "'Going out clubbing!'"
        }
    },
     {
        "question": "Where are you on Friday night?",
        "answers": {
            "A": "'Studying, I need to lock in.'",
            "B": "'Grabbing dinner with my friends and going to an event'",
            "C": "'Listening to music and drawing or reading.'",
            "D": "'Partying.'"
        }
    },
     {
        "question": "What's fantasy creature would you be?",
        "answers": {
            "A": "'Deffinetly a vampire, they live forever.'",
            "B": "'A forest fairy or gnome.''",
            "C": "'I'd like to be a mermaid.'",
            "D": "'100 percent a dragon.'"
        }
    },
     {
        "question": "How are you spending your sick day?",
        "answers": {
            "A": "'It'll be a good chance for me to finsih up some work.'",
            "B": "'I'm just going to take it easy, maybe work on a project.'",
            "C": "'I'm going to get some rest and have some soup.'",
            "D": "'I'm going to focas on getting better, I need to get out of here.'"
        }
    },
     {
        "question": "How quickly do you pick up new hobbies?",
        "answers": {
            "A": "'I'm already busy enough, I don't have time for new hobbies.'",
            "B": "'I like learning new stuff, I'll usually practice a few times a week'",
            "C": "'I already love the things I do, I don't need more.'",
            "D": "'I'll pick up a new activity often and do it for a few weeks.'"
        }
    },
     {
        "question": "What is your inital reaction upon seeing a ghost?",
        "answers": {
            "A": "'Thats not possible, I know theres an explanation.'",
            "B": "'I know theres a likley explanation, but I'm still terrified.'",
            "C": "'I mean, nothing really makes sense anyway.'",
            "D": "'Oh bet. I knew they were real.'"
        }
    },
     {
        "question": "How do you listen to music?",
        "answers": {
            "A": "'I need specialized playlists for every event.'",
            "B": "'I like musical playlists and songs that are sentimental.'",
            "C": "'I listen to whatevers good.'",
            "D": "'I love listebning to knew stuff, I love a bunch of generes.'"
        }
    },
     {
        "question": "You have a few minutes until your next activity, how are spending it?",
        "answers": {
            "A": "Doom scrolling",
            "B": "Go for a walk",
            "C": "Just sit and chill",
            "D": "Find a snack for energy"
        }
    }
]

personalities = {
    "A": "Anxious, competitive, ambitious, forward-looking",
    "B": "People-oriented, organized, reliable, blunt",
    "C": "Patient, relaxed, empathetic, creative",
    "D": "Confident, energetic, adventurous, spontaneous"
}


print("Welcome to The Personality Quiz.")
print("This test will return a final percentage of personalities 1, 2, 3 and 4 after the final question is complete.")

#display each question and answer choices

for i, item in enumerate(quiz, start=1):
  print(f"Question{i}: {item['question']}") #prints actual question text and associated personality type
  for letter, text in item["answers"].items():
    print(f"{letter}. {text}") #print choice label and text

    while True: #while True loop for answers
        choice = input("Your choice (A/B/C/D): ").strip().upper() #allows user to input A, B, C or D as their choice
        if choice in item["answers"]: #determins validity if answer inputted is in range
            scores[choice] += 1
            break
        else:
          print("Bad choice. Choose A, B, C or D") #if answer is not valid

    print()

all_answers = len(quiz)
print("Final personality percentages")

#AI
percentages = {}
for letter, score in scores.item():
    percentage = (score / total_answers) * 100
    percentages[letter] = percentage
    bar = "#" * round(percentage / 5)   # simple text bar out of 20
    print(f"{letter}: {percentage:5.1f}%  {bar}")
    print(f"   {personalities[letter]}")

# Run the quiz
personality_quiz()
