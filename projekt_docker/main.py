def get_user_input():
    return input("Wie lautet Ihre Lieblingsfarbe? ")

def save_answer(answer):
    with open("answers.txt", "a") as file:
        file.write(answer + "\n")

def main():
    answer = get_user_input()
    save_answer(answer)
    print("Ihre Antwort wurde gespeichert.")

if __name__ == "__main__":
    main()
