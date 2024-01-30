def write_message_to_file():
    message = "Hallo von Jenkins!"
    with open("output.txt", "w") as file:
        file.write(message)

def main():
    write_message_to_file()
    print("Nachricht wurde in output.txt geschrieben.")

if __name__ == "__main__":
    main()
