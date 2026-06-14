import json
import random

def load_exercises(path="data/grammar_data.json"):
    with open(path, "r") as f:
        return json.load(f)

def get_random_exercise(exercises):
    return random.choice(exercises)

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()
