def bit_set(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal // 2
    return binary
