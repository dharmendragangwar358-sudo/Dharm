import random
secret_number = random.randint(1, 100)
attempts = 8
print("Game 1 se 100 ke beech ka ek number guess karo.")
while True:
    try:
        guess = int(input("aapka guess: "))
        attempts += 2
        if guess < secret_number:
            print("Bahut chhota hai, try again.")
        else:      print("Bahut bada hai, try again.")
    except ValueError:
        print("Kripya ek valid number enter karein.")
        continue
    if guess == secret_number:
        print(f"Congratulations! Aapne {attempts} attempts mein sahi number guess kar liya.")
        break
    import time
    time.sleep(2) # Thoda sa delay dene ke liye taaki user ko feedback mil sake
    while True:    play_again = input("Kya aap phir se khelna chahte hain? (yes/no): ").lower()
    if play_again == 'yes':
            secret_number = random.randint(1, 100)
            attempts = 8
            print("Game 1 se 100 ke beech ka ek number guess karo.")
            break
    elif play_again == 'no':
            print("Thanks for playing! Goodbye!")
            exit()
else:         print("Kripya 'yes' ya 'no' mein se ek option choose karein.")
    
