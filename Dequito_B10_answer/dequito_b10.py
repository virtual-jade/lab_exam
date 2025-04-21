import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

values = {"Count" : 0, "Size Est (cm)" : 0}
output = data.fillna(value=values)

output.to_csv("b10_output1.csv", index = False)