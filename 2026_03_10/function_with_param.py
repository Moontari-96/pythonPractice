# function with param(passing the data)
# def travel():
#     print("Hello there!")
#     print("Are you excited?")

# travel()
    
# def travel_to_country(country: str):
#     print("Hello there!")
#     print(f"You are going to travel to {country}")
#     print("Are you excited?")

# # travel_to_country(country="USA")
# travel_to_country("USA")

# country => parameter
# "USA" => argument

def travel_to_country(country: str, name: str):
    print(f"Hello {name}!")
    print(f"You are going to travel to {country}")
    print("Are you excited?")

# # # positional argument
# travel_to_country("USA", "Joon")
# travel_to_country("Joon", "USA")
# keyword argument
# travel_to_country(country="USA", name="Joon")
# travel_to_country(name="Joon", country="USA")