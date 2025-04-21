import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

abundant_sp = data.groupby("Scientific Name")["Count"].sum().max()

output = pd.DataFrame({"Abundant Species" : ["Scientific Name"], "Abundant Species" : abundant_sp})

output.to_csv("b6_output1.csv", index=False)