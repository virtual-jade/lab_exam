import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

output = data[data["Visibility (m)"] > 8]

output.to_csv("b8_output1.csv", index=False)