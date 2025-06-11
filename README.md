def introduction_generator():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    interest = input("What are you interested in? ")
    goal = input("What is your goal? ")

    intro = (
        f"Hi, my name is {name}. I'm {age} years old and I live in {city}. "
        f"I'm passionate about {interest}, and my goal is to {goal}. "
        "Nice to meet you!"
    )

    print("\nGenerated Introduction:")
    print(intro)

# Run the function
introduction_generator()
