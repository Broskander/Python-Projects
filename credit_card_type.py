def digit(x):
    return [int(y) for y in str(x)]


def checkLuhn(cc_num):
    digits = digit(cc_num)
    oddNum = digits[-1::-2]
    evenNum = digits[-2::-2]
    check = 0
    check += sum(oddNum)

    for i in (evenNum):
        check += sum(digit(i * 2))

    return check % 10


def is_valid(cc_int):
    cc_int = cc_int.strip()
    cc_length = (len(str(cc_int) + ""))
    cc_num = cc_int.strip()
    if (15 <= cc_length <= 16):
        if (checkLuhn(cc_num)):
            return cc_type(cc_num)
    else:
        return "Not a 15 or 16 digit number"


def cc_type(cc_num):
    type = str(cc_num)
    mastercard = ['50', '51', '52', '53', '54', '55']

    if (int(cc_num[0]) == 4) and (checkLuhn(cc_num)):
        return "Valid Visa credit card"
    elif mastercard.count(type[0:2]) > 0:
        return "Valid MasterCard credit card"
    elif ((int(cc_num[0:4]) == 6011) or (int(cc_num[0:3]) == 644) or (int(cc_num[0:2]) == 65)) and (checkLuhn(cc_num)):
        return "Valid Discover credit card"
    elif ((int(cc_num[0:2]) == 37) or (int(cc_num[0:2]) == 34) and (checkLuhn(cc_num))):
        return "Valid American Express credit card"
    else:
        return "Invalid credit card number"


def main():
    credit = input("Enter 15 or 16-digit credit card number: ")
    print(is_valid(credit))


main()


