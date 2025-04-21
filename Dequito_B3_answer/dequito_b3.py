import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

output = data[data["Genus"].str.match("Pomacentrus", case=False)]

output.to_csv("b3_output1.csv", index=False)