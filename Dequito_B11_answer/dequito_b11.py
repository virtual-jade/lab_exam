import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

output = data.drop_duplicates(subset=['Date', 'Site', 'Scientific Name'])

output.to_csv("b11_output1.csv", index = False)