import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

scientific_name = data["Scientific Name"].unique()

total_count = data.groupby("Scientific Name")["Count"].sum()

output = pd.DataFrame({"Scientific Names" : scientific_name, "Total Count" : total_count})

output.to_csv("b4_output1.csv", index=False)

print(output)