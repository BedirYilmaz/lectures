import pandas as pd

path = r"C:\Users\3yanl\Code\lectures\lecture10\Mappe 1.xlsx"

workbook = pd.read_excel(path)

print(set(workbook[1].tolist()) - set(workbook[9].tolist()))
print(set(workbook[1].tolist()).intersection(workbook[9].tolist()))