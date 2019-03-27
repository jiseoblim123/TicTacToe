game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1]]

# for col, row in zip(list(reversed(range(len(game)))), range(len(game))):
#     print(col, row)

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])


# if game[2][0] == game[1][1] == game[0][2]:
#     print("Winner!!")