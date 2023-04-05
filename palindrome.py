def palindrome():
    user_values = []
    list = int(input())
    for i in range(list):
        user_values.append(int(input()))
    check = True
    while check:
        for i in range(int(list / 2) + 1):
            x = 0
            y = -1
            if user_values[x] == user_values[y]:
                check = True
            else:
                check = False
                break
            break
        break

    if check == True:
        print("yes")
    else:
        print("no")


palindrome()
