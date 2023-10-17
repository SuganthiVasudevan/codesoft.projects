import random
import string

def generate_password(length,complexity):
    
    characters = ""
    
    if complexity == "low":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid.Please choose 'low', 'medium', or 'high'."

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the  length of the password: "))
    complexity = input("Enter complexity (low, medium, high): ").lower()
    
    password = generate_password(length, complexity)
    
    if "Invalid" not in password:
        print("Generated Password:", password)
    else:
        print(password)

if __name__ == "__main__":
    main()