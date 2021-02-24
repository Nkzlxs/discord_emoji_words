#! /usr/bin/python3

import clipboard
import mappings
import sys
MAX_ALLOWABLE_CHARACTERS = 2000
EMOJI_ID = ""
EMOJI_SIZE = 20
INITIAL_PLACEHOLDER = ""
SPACING = " "*6


def main(arg):
    if len(arg) < 4:
        exit("Need as least 3 arguments,{Emoji ID}, {Initial Placeholder}, {String to convert to pixel art}")

    EMOJI_ID = str(arg[1])
    INITIAL_PLACEHOLDER = str(arg[2]) + "\n"
    input_str = str(arg[3])

    outputs = []
    for c in input_str:
        outputs.append(mappings.CHARACTERS[c])

    restructured_output = ""
    for n in range(5):
        for a in range(len(outputs)):
            if len(outputs[a]) > n:
                restructured_output += outputs[a][n].replace("0",'\x00').replace("1",'\x01')

                if a != len(outputs)-1:
                    restructured_output += "\x00"
                else:
                    restructured_output += '\n'

    current_char_len = 0
    current_char_len += len(INITIAL_PLACEHOLDER)
    current_char_len += 5  # 5 "\n"
    current_char_len += restructured_output.count("\x00")*len(SPACING)
    current_char_len += restructured_output.count("\x01")*len(EMOJI_ID)
    current_char_len += restructured_output.count("\x01")*EMOJI_SIZE

    if current_char_len > MAX_ALLOWABLE_CHARACTERS:
        print(f"Generated pixel text len:({current_char_len}) is too big!!\nIt can't be printed to Discord Chat!!")

    try:
        clipboard.copy(
            INITIAL_PLACEHOLDER + \
                restructured_output
                    .replace("\x01",EMOJI_ID)
                    .replace("\x00", SPACING)
        )
        print("Pixel text have been copied!!")
    except Exception as e:
        raise(e)


if __name__ == '__main__':
    main(sys.argv)
