import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

obs = data["Observer"].unique()

output = pd.DataFrame({"Observers" : obs})

output.to_csv("b7_output1.csv", index=False)