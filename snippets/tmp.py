f = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def infinite_sequence(fig, cur=1):
    row = 0
    i = 0
    fig[row][i] = cur
    last_i = len(fig[row])-1
    while True:
        temp = fig[row][i]
        if i == last_i:
            row += 1
            if row == 3:
                row = 0
            i = -1

        yield fig

        if i < last_i:
            fig[row-1][last_i] = fig[row-1][last_i-1]
        fig[row][i] = fig[row][i + 1]
        fig[row][i + 1] = temp
        i += 1


def str_out(gen):
    res = ""
    for r in gen:
        res += f"{r}\n"
    return res


c = infinite_sequence(f, 1)

flag = True
while flag:
    step = input("Enter: next step; Space = exit: ")
    if step == " ":
        flag = False
    print(str_out(next(c)))
