# with open("sample.txt") as f:
#     f.read()

# # FileNotFound
# try:
#     with open("sample.txt") as f:
#         f.read()
# except FileNotFoundError:
#     print("FileNotFoundError occurs")

# # KeyError
# try:
#     dict = {"k": "v"}
#     print(dict['no'])
# except KeyError as error_message:
#     print("KeyError occurs")
#     print(error_message)

# # IndexError
# try:
#     country_list = ["USA", "South Korea", "Japan"]
#     pick_country = country_list[3]
# except IndexError:
#     print("IndexError occurs")

# TypeError
# try:
#     print(1 + "a")
#     dict = {"k": "v"}
#     print(dict['no'])
# except TypeError:
#     print("TypeError occurs")
# else:
#     print("this got triggered due to no error found")
# finally:
#     print("always running this")

# # try: something may go wrong
# # except: catch the error if there is an exception
# # else: do this if no excpetion happens
# # finally: always run either you have error or not

# # if there is first exception, the rest does not move forward

# Raise Exception
# custom error(user defiend error)
class GradeOutOfBoundError(Exception):
    def __init__(self, grade, message):
        print(grade)
        print(message)
        # do something here

try:
    grade = int(input("Type your score from 0 to 100: "))
    if grade < 0 or grade > 100:
        raise GradeOutOfBoundError(
            grade=grade,
            message="Grade should be between 0 to 100")
except GradeOutOfBoundError:
    pass