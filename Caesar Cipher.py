# from art import logo

# Entire Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(logo)
# User inputs to fit their needs.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    running = True
    while running:
        new_text = ""
        # Checking to see if the software will decode or encode
        if direction == "decode":
            action = "decoded"
            shift *= -1
        else:
            action = "encoded"

        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift

# This gives us the remainder and that is how many times it has been shifted total
                new_position = new_position % 26
# This is another way of doing the same thing.
# while new_position > len(alphabet):
# new_position -= len(alphabet)
                new_text += alphabet[new_position]
                # Just incase they want to add some symbols in the text
            else:
                new_text += letter
        print(f"The {action} message is: {new_text}")
        answer = input("Type \"yes\" if you want to go again. Otherwise type \"no\"\n").lower()

        # This is an option that lets them play again.
        if answer == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
        else:
            running = False
    print("Goodbye")

caesar(text, shift, direction)
