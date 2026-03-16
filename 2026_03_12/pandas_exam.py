import pandas as pd

data = pd.read_csv("sample.csv")

# DataFrame : General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column
# print(type(data))
# print(data.to_dict())

# # Series : 1D labeled homogeneously-typed array
# print(type(data['Name']))
# print(data['Name'].to_list())

# # sum / max
# print(sum(data['ID'].to_list()))
# print(data['ID'].max())

# differct way to access to the column
# print(data.JoinDate)

# row data
# print(data[data.Name == "Gildong Hong"])
# print(data[data.ID == data.ID.max()])

# from scratch
grade = {
    "students": ["A", "B", "C"],
    "scores": [90, 80, 85]
}
data =pd.DataFrame(grade)
print(data)
data.to_csv("grade.csv")