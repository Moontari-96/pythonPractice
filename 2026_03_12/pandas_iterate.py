score_dict = {
    "student": ["Tom", "Lisa", "Sarah"],
    "score": [80, 90, 95]
}

# # Iterating thru
# [print(col) for (col, _) in score_dict.items()]
# for col in score_dict:
#     print(col)

import pandas as pd

score_df = pd.DataFrame(score_dict)
# print(score_df)
# # for (key, value) in score_df.items():
# #     print(key)
# #     print(value)

# # loop through rows
# for (i, row) in score_df.iterrows():
#     print(f"{row.student} : {row.score}")

score_df['result'] = score_df['score'].apply(lambda x: '합격' if x >= 80 else '불합격')
print(score_df)