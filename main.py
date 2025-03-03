
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
