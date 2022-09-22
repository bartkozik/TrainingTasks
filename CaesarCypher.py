def caesarCipher(s, k):
    # Write your code here
    low_alf = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    up_alf = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
    password = ""
    for letter in s:
        if letter in low_alf:
            password += low_alf[(low_alf.index(letter) + k) % 26]  # "a-z"
        elif letter in up_alf:
            password += up_alf[(up_alf.index(letter) + k) % 26]  # "A-Z"
        else:
            password += letter  # "-"
    return password
