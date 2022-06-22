import tkinter as tk
from math import inf

def print_table(rows, indexes):
    first_line = "\t"
    for i in range(len(indexes)):
        val = indexes[i]
        val_incremented = ""
        for i in val:
            val_incremented += str(int(i)+1)
        first_line += val_incremented + "\t"
    print(first_line)

    for i in range(len(rows)):
        val = indexes[i]
        val_incremented = ""
        for v in val:
            val_incremented += str(int(v)+1)
        line = val_incremented + "\t"
        for j in range(len(rows)):
            line += str(rows[i][j]) + "\t"
        print(line)

def compute_full(rows):
    full_table = rows.copy()
    n = len(rows)
    for i in range(n-1):
        for j in range(i+1, n):
            full_table[j][i] = rows[i][j]
    return full_table

def compute_tree(rows, indexes):
    iteration = 1
    while(len(indexes) > 2):
        print("== Iteration " + str(iteration) + " ==")
        print_table(rows, indexes)
        rows, indexes = compute_iteration(rows, indexes)
        iteration += 1
    print("")
    print("== Finished ==")
    print_table(rows, indexes)

def compute_iteration(rows, indexes):
    n = len(rows)
    min_val = inf
    index_row = -1
    index_column = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if(rows[i][j] < min_val):
                min_val = rows[i][j]
                index_row = i
                index_column = j

    exclude = [indexes[index_row], indexes[index_column]]
    s_indexes = str(indexes[index_row]) + str(indexes[index_column])

    val1 = indexes[index_row]
    val_incremented1 = ""
    for v in val1:
        val_incremented1 += str(int(v)+1)
    val2 = indexes[index_column]
    val_incremented2 = ""
    for v in val2:
        val_incremented2 += str(int(v)+1)

    print_indexes = val_incremented1 + "-" + val_incremented2
    print("=> Min val: " + str(min_val) + " for species " + print_indexes)
    print("=> Tree value: " + str(int(min_val/2)))
    print("")

    new_indexes = []
    for i in indexes:
        if(i not in exclude):
            new_indexes.append(i)
    new_indexes.append(s_indexes)

    full_table = compute_full(rows)
    new_rows = []
    for i in range(n-1):
        col = [0 for i in range(n-1)]
        new_rows.append(col)

    for i in range(n-2):
        for j in range(i+1, n-1):
            valx = indexes.index(new_indexes[i])
            if(new_indexes[j] not in indexes):
                val1 = indexes.index(indexes[index_row])
                val2 = indexes.index(indexes[index_column])
                val = int((full_table[valx][val1] + full_table[valx][val2])/2)
            else:
                valy = indexes.index(new_indexes[j])
                val = full_table[valx][valy]
            new_rows[i][j] = val

    return new_rows, new_indexes

def scrap_data(entries):
    rows = []
    for e in entries:
        s_entry = e.get()
        s_entry = s_entry.strip()
        s_entry = s_entry.split(' ')
        map_entry = map(int, s_entry)
        int_entry = list(map_entry)
        rows.append(int_entry)
    indexes = [str(i) for i in range(len(rows))]
    compute_tree(rows, indexes)

def make_table(nb):
    frame2 = tk.LabelFrame(app, text="Data on species", padx=15, pady=15)
    frame2.grid(row=1, column=0)

    inputs_entries = []
    default_text = ""
    for i in range(nb):
        default_text += '0 '
    for i in range(1, nb+1):
        ent = tk.Entry(frame2)
        ent.insert(0, default_text)
        ent.pack(side=tk.TOP)
        inputs_entries.append(ent)

    b2 = tk.Button(frame2, text="Compute", command=lambda: scrap_data(inputs_entries))
    b2.pack()

def get_nb():
    nb = int(ent_nb.get())
    make_table(nb)

if __name__ == '__main__':
    app = tk.Tk()
    app.title("UPGMA")

    frame1 = tk.LabelFrame(app, text="Number of species", padx=15, pady=15)
    frame1.grid(row=0, column=0)
    ent_nb = tk.Entry(frame1)
    ent_nb.pack()
    b1 = tk.Button(frame1, text="Set numbers", command=get_nb)
    b1.pack()

    app.mainloop()