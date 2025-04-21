import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

sci_name = data["Scientific Name"].unique()

ave_size = data.groupby("Scientific Name")["Size Est (cm)"].mean()

output = pd.DataFrame({"Species" : sci_name, "Average Size (cm)" : ave_size})

output.to_csv("b5_output1.csv", index=False)

