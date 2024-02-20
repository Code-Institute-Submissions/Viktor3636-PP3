def table_board():
    print("   A   B   C   D   E   F   G   H")
    print(" +" + "---+" * 8)
    for i in range(1, 9):
        print(f"{i}| {' | '.join(['_'] * 8)} |")
        print(" +" + "---+" * 8)

table_board()
