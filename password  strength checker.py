import string

print("Welcome to Password Strength Checker")
# Asking for password
password = input("Enter password: ")

# Initiating Characters
Lowercase = False
Uppercase = False
Symbol = False
Digits = False

# Looping through Password
for c in password:
    if c in string.ascii_lowercase:
        Lowercase = True
    elif c in string.ascii_uppercase:
        Uppercase = True
    elif c in string.punctuation:
        Symbol = True
    elif c in string.digits:
        Digits = True

# Assigning Values into the characters list
characters = [Lowercase, Uppercase, Symbol, Digits]

# Assigning Score
password_score = 0
password_lenghth = len(password)

# Check if password is in 10k file
with open("Password Strength Checker/10k most common.txt", "r") as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print(
        "Password was found in Google's common password list file. Do not Use!. Score:0"
    )
else:
    # Assigning Length Score
    if password_lenghth > 8:
        password_score += 1
    if password_lenghth > 12:
        password_score += 1
    if password_lenghth > 18:
        password_score += 1
    if password_lenghth > 20:
        password_score += 1

    print(
        f"Password is {password_lenghth} characters long. Adding {password_score} points!"
    )

    # Assigning Different Character Score
    if sum(characters) == 1:
        password_score += 1
    elif sum(characters) == 2:
        password_score += 2
    elif sum(characters) == 3:
        password_score += 3
    elif sum(characters) == 4:
        password_score += 4

    # Check for three consecutive characters
    count = 1
    previous_char = None

    for c in password:
        if c == previous_char:
            count += 1
            if count == 3:
                print(
                    "Password chracter repeats three times or more. Subtracting 1 point!"
                )
                password_score -= 1
                break
        else:
            count = 1
            previous_char = c
    else:
        print("No three consecutive characters found adding 1 point!")
        password_score += 1

    # Assigning grades
    if password_score <= 4:
        print(f"Password is weak!. Please change it. Score: {password_score}/8 ")
    elif password_score == 5:
        print(f"Password is okay. Score: {password_score}/8 ")
    elif password_score == 6:
        print(f"Password is good. Score: {password_score}/8 ")
    elif password_score == 7:
        print(f"Password is very Good!. Score: {password_score}/8 ")
    elif password_score == 8:
        print(f"Password is excellent!. Score: {password_score}/8 ")
