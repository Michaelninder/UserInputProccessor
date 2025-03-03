
def get_user_input():
  name = input("What's your name? ")
  age = input("How old are you? ")
  favorite_color = input("What's your favorite color? ")  
  
  return name, age, favorite_color

def process_input(name, age, favorite_color):
    print(f"\nHello, {name}! Let's do some cool calculations based on your data.")

    try:
        age = int(age)
    except ValueError:
        print("Oops! That doesn't seem to be a valid age.")
        return

    days_alive = age * 365
    print(f"You've been alive for approximately {days_alive} days!")

    if favorite_color.lower() == 'blue':
        print("Blue is such a calming and cool color!")
    elif favorite_color.lower() == 'red':
        print("Red is a bold and energetic color!")
    else:
        print(f"{favorite_color.capitalize()} is a fantastic color!")
