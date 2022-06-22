import sys

if (len(sys.argv) != 4):
    print("Input incorrect")
else:
    sequence = sys.argv[1]
    sequence = sequence.replace(" ", "")
    sequence = sequence.lower()
    index_to_change = int(sys.argv[2])
    letter_to_chane = str(sys.argv[3]).lower()

    start = sequence[:index_to_change-1]
    end = sequence[index_to_change:]
    new_sequence = start + letter_to_chane + end

    print(new_sequence)
