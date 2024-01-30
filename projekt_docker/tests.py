from main import write_message_to_file
import os

def test_write_message_to_file():
    write_message_to_file()
    assert os.path.isfile("output.txt")
    with open("output.txt", "r") as file:
        content = file.read()
    assert content == "Hallo von Jenkins!"
