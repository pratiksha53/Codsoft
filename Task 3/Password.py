import random
import string

def create_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
   
    password = [random.choice(string.digits), random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase), random.choice(string.punctuation)]
    
  
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
   
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 4:
            print("Password length must be at least 5 characters.")
        else:
            password = create_pass(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
