
import sys


def get_next_start(here: int = 1) -> int:
    next_start = 1
    match (here):
        case 1 | 2:
            next_start = 3
        case 3 | 4 | 5:
            next_start = 6
    return next_start


def encode_it(word: str) -> str:
    new_word = word.strip() + "\r"
    return new_word


def main():
    get_next_character: bool = True
    with open("source.txt", "r") as f:
        lines: list = f.readlines()

    encoded_word = list(map(encode_it, lines))

    for word in encoded_word:

        char_lst = list(word)
        get_next_character = True
        state = 1
        next_start = 1

        print(word)
        while True:
            if get_next_character:
                character = str.encode(char_lst.pop(0))

            match state:
                case 1:
                    if (character >= b'a' and character <= b'z') or \
                            (character >= b'A' and character <= b'Z'):
                        state = 2
                        get_next_character = True
                    else:
                        next_start = get_next_start(next_start)
                        state = next_start
                        get_next_character = False
                        # print("NOT an Identifier, MOVED TO NEXT")
                case 2:
                    if (character >= b'a' and character <= b'z') or \
                        (character >= b'A' and character <= b'Z') or \
                            (character >= b'0' and character <= b'9'):
                        get_next_character = True
                    elif character == b'\r':
                        # print("Acceptable!")
                        print("String type >", "Identifier")
                        break
                    else:
                        next_start = get_next_start(next_start)
                        state = next_start
                        get_next_character = False
                        # print("NOT an Identifier, MOVED TO NEXT")
                case 3:
                    if character >= b'1' and character <= b'9':
                        state = 4
                        get_next_character = True
                    else:
                        next_start = get_next_start(next_start)
                        state = next_start
                        get_next_character = False
                        # print("NOT a INTEGER, MOVED TO NEXT")
                case 4:
                    if character >= b'0' and character <= b'9':
                        get_next_character = True
                    elif character == b'.':
                        state = 5
                        get_next_character = True
                    elif character == b'\r':
                        # print("Acceptable!")
                        print("String type >", "Integer")
                        break
                    else:
                        next_start = get_next_start(next_start)
                        state = next_start
                        get_next_character = False
                        # print("NOT a INTEGER, MOVED TO NEXT")

                case 5:
                    if character >= b'0' and character <= b'9':
                        pass
                    elif character == b'\r':
                        # print("Acceptable!")
                        print("String type >", "Float")
                        break
                    else:
                        next_start = get_next_start(next_start)
                        state = next_start
                        get_next_character = False
                        # print("NOT EVEN a FLOAT, MOVED TO NEXT")
                case 6:
                    if character == b' ':
                        # print("EMPTY SPACE!")
                        state = 6
                        get_next_character = True
                    else:
                        print("NOT Acceptable!")
                        break

    sys.exit()


if __name__ == '__main__':
    main()
