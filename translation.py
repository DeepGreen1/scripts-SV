import sys

def changes():
    index_to_change = int(sys.argv[2])
    letter_to_chane = str(sys.argv[3]).lower()

    start = sequence[:index_to_change-1]
    end = sequence[index_to_change:]
    new_sequence = start + letter_to_chane + end

    return new_sequence

start = "atg"
stop = ["taa", "tag", "tga"]

if (not (len(sys.argv) == 2 or len(sys.argv) == 4)):
    print("Sequence incorrecte")
else:
    sequence = sys.argv[1]
    sequence = sequence.replace(" ", "")
    sequence = sequence.lower()

    if(len(sys.argv) == 4):
        sequence = changes()
        print("New sequence: " + sequence)

    start_index = -1
    for i in range(len(sequence)):
        three = sequence[i:i+3]
        if (three == start):
            start_index = i
            print("Start index: " + str(i+1))
            break
    if (start_index == -1):
        print("No start present")
    else:
        for j in range(len(sequence)):
            next_three = sequence[i+j:i+j+3]
            if (next_three in stop):
                nb_AA = int((i+j-start_index)/3)
                print("Stop index: " + str(i+j+1))
                print("Number of AA: " + str(nb_AA))
                break
