import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

output = pd.DataFrame(data)

output.to_csv("b1_output1.csv", index=False)
