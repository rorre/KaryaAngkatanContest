def main(a1, a2):
    # ord("A") is 65, since A is 64 then
    # just reduce it by 64.

    # In other programming language it would probably
    # be best to ensure that the number won't exceed
    # int limit but we're in Python so, yeah.
    n1 = 1
    for c in a1:
        n1 *= ord(c) - 64

    n2 = 1
    for c in a2:
        n2 *= ord(c) - 64

    n1 = n1 % 47
    n2 = n2 % 47

    if n1 == n2:
        return "PERGI"
    else:
        return "TETAP"


if __name__ == "__main__":
    input()  # We literally don't care about the first input
    print(main(input(), input()))
