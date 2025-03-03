# main.py

def get_user_input():
    name = input("What's your name? ")
    age = input("How old are you? ")
    favorite_color = input("What's your favorite color? ")
    hobby = input("What's your favorite hobby? ")
    favorite_food = input("What's your favorite food? ")
    dream_destination = input("If you could visit anywhere in the world, where would it be? ")
    return name, age, favorite_color, hobby, favorite_food, dream_destination

def process_input(name, age, favorite_color, hobby, favorite_food, dream_destination):
    print(f"\nHello, {name}! Let's do some fun calculations and insights with your details.")
    input("Press Enter to continue...")
    
    try:
        age = int(age)
    except ValueError:
        print("Oops! That doesn't seem to be a valid age. Let's try again later.")
        return
    
    # Calculate the number of days and hours the user has been alive
    days_alive = age * 365
    hours_alive = days_alive * 24

    print(f"\nYou've been alive for approximately {days_alive} days, or {hours_alive} hours!")
    input("Press Enter to continue...")

    print("\nLet's talk about your favorite color!")
    if favorite_color.lower() == 'blue':
        print("Blue is often associated with calmness and tranquility. It's a color of the sky and the ocean!")
    elif favorite_color.lower() == 'red':
        print("Red is a powerful and energetic color, often associated with passion, love, and strength!")
    else:
        print(f"{favorite_color.capitalize()} is a beautiful and unique color!")
    
    input("Press Enter to continue...")

    # Follow-up on the favorite color
    if favorite_color.lower() == 'blue':
        print("\nSince you love blue, I recommend you check out the calming art of Impressionism!")
    elif favorite_color.lower() == 'green':
        print("\nGreen is the color of nature! Maybe you'd enjoy a hike in a forest or a park.")
    
    input("Press Enter to continue...")

    # Hobbies and favorite food
    print(f"\nYour hobby is {hobby}. That's awesome! Hobbies are a great way to unwind and enjoy life.")
    print(f"Your favorite food is {favorite_food}. Yummy! Have you ever tried cooking it yourself?")
    
    input("Press Enter to continue...")

    # Age-related wisdom
    if age < 20:
        print("\nYou're in the exciting phase of life! There's so much to explore and learn.")
    elif 20 <= age < 40:
        print("\nThe 20s and 30s are all about building your path. Stay true to yourself and keep growing.")
    elif 40 <= age < 60:
        print("\nThe 40s and 50s offer wisdom and experience. You've lived through many valuable lessons.")
    else:
        print("\nYou are a treasure trove of experiences! You've seen so much and have a wealth of stories to share.")
    
    input("Press Enter to continue...")

    # Dream destination follow-up
    print(f"\nYour dream destination is {dream_destination}. That sounds amazing! Imagine the adventures you'd have there.")
    input("Press Enter to continue...")

    # Fun facts based on age
    if age < 30:
        print("\nYou're in the prime of your life! Now's the time to chase your dreams, take risks, and explore new things.")
    elif 30 <= age < 50:
        print("\nThis is the age of stability and self-discovery. You're laying down your roots and building a future.")
    elif age >= 50:
        print("\nYou've lived through quite a journey. Your wisdom and experiences are treasures for those around you.")
    
    input("Press Enter to continue...")

    # Philosophical Question
    print("\nIf you could change one thing about the world, what would it be? Let's think big!")
    input("Press Enter to continue...")

    print(f"\nBy the way, if you could teleport anywhere right now, where would it be? Maybe {dream_destination} will give you a clue about that!")

def main():
    name, age, favorite_color, hobby, favorite_food, dream_destination = get_user_input()
    process_input(name, age, favorite_color, hobby, favorite_food, dream_destination)

if __name__ == "__main__":
    main()
