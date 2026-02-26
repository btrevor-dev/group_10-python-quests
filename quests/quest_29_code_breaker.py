# Quest 29: The Code Breaker

secret_code = 42
attempts = 3

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter the secret code: "))

    if guess == secret_code:
        print("Access Granted. Welcome.")
        break
    else:
        print("Incorrect code.")

else:
    print("Access Denied. Too many failed attempts.")