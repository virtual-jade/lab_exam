import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

ave_count = data.groupby("Replicate", "Interval")["Count"].mean()

output = pd.DataFrame({"Replicate" : ["Replicate"], "Interval" : ["Interval"], "Average Count" : ave_count})

output.to_csv("b9_output1.csv", index=False)