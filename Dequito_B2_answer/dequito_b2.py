import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

data.lower.apply(lambda x: x.replace(" ", "_"))

data.to_csv("b1_output1.csv", index=False)