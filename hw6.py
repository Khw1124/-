for i in range(2, 10, 4):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}\t{i+1} x {j} = {(i+1)*j}\t{i+2} x {j} = {(i+2)*j}\t{i+3} x {j} = {(i+3)*j}")
        if j == 9 and i != 6:
            print()
