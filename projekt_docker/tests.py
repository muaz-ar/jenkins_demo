import os
from main import save_answer

def test_save_answer():
    test_answer = "Test Antwort"
    save_answer(test_answer)
    assert os.path.isfile("answers.txt")
    with open("answers.txt", "r") as file:
        saved_answer = file.readline().strip()
    assert saved_answer == test_answer
    os.remove("answers.txt")  # Aufräumen nach dem Test
