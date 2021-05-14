# initials
columns = 6
rows = 8
bg = 0
cursor = "*"
field = [[bg for i in range(columns)] for j in range(rows)]


def infinite_sequence(fig, piece):
    # piece starting coordinates
    row = 0
    i = 0
    fig[row][i] = piece

    # primary block
    last_i = len(fig[row]) - 1
    while True:
        temp = fig[row][i]

        # collision on the right
        if i == last_i:
            row += 1
            i = -1
        # collision on the bottom
        if row == len(fig):
            row = 0

        yield fig

        if i < last_i:
            fig[row - 1][last_i] = fig[row - 1][last_i - 1]
        fig[row][i] = fig[row][i + 1]
        fig[row][i + 1] = temp
        i += 1


#  creating string
def str_out(gen):
    res = ""
    for r in gen:
        res = res + "\n"
        for c in r:
            res += f"{c}"

    return res


# executing
c = infinite_sequence(field, cursor)
flag = True
while flag:
    step = input("Enter = next step; Space = exit: ")
    if step == " ":
        flag = False
    print(str_out(next(c)))
