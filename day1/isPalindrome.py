def wordflipper(input):
    a = len(input)
    i = 0
    output = ''
    while i < a:
        b = a - i
        output += input[b - 1]
        i += 1
    return output

def palindromecheck(input):
    flipped = wordflipper(input)

    if flipped == input:
        print("Yup, it's a Palindrome")
    else:
        print("Nope, not a palindrome")
