letter_dictionary = dict([
    (".-", "a"),
    ("-...", "b"),
    ("-.-.", "c"),
    ("-..","d"),
    (".", "e"),
    ("..-.","f"),
    ("--.","g"),
    ("....", "h"),
    ("..","i"),
    (".---","j"),
    ("-.-","k"),
    (".-..","l"),
    ("--","m"),
    ("-.","n"),
    ("---","o"),
    (".--.","p"),
    ("--.-","q"),
    (".-.","r"),
    ("...","s"),
    ("-","t"),
    ("..-","u"),
    ("...-","v"),
    (".--","w"),
    ("-..-","x"),
    ("-.--","y"),
    ("--..", "z"),
    ("|"," "),
    ("..--..","?"),
    (".----.", "'"),
    ("-....-", "-"),
    ("--..--",","),
    (".-.-.-","."),
    ("---...",":")
])
while True:
    morse_input = input("""type here your morse code> 
type /help for further info... """)

    if morse_input == "/quit":
        quit()

    elif morse_input == "/help":
        print("every character ought to be followed by a space, use | to divide words")

    morse_character_list = morse_input.split(" ")
    for character in morse_character_list:
        letter = letter_dictionary.get(character)
        print(letter, end="")

    print("\n")
