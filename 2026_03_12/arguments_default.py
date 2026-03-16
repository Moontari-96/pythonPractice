# # Arguments with Default Values
def write_str_to_file(file, content, mode="w"):
    with open(file, mode=mode) as f:
        f.write(content)

write_str_to_file(
    file="sample.txt",
    content="Hello World!!!!!",
    mode="a")

# # Unlimited Positional Arguments
# # def unlimited_func(*args):
# #     print(args[2])
# # unlimited_func(1, 2, 3)

# def sum_all(*arg_list):
#     total = 0
#     for n in arg_list:
#         total += n
#     return total

# print(sum_all(1, 2, 3))

# **kwargs: Keyworded arguements
# def calc(**kwargs):
#     # print(kwargs)

# calc(n1=1, n2=3, func="add")


# def calc(func, **kwargs):
#     # for k, v in kwargs.items():
#     #     print(k)
#     #     print(v)

#     if func == "add":
#         return kwargs['n1'] + kwargs['n2']


# print(calc(n1=1, n2=3, func="add"))