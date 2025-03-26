def set(i : int) -> None:
    for j in range(8):
        if i & (1 << j):
            print(j, end=' ')
    print()