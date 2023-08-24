import pandas as pd
from datetime import date

exampleData = {"date": [date(2023, 8, 21), date(2023, 8, 24)], "good score": [2, 1],"bad score": [1, 1], "final score": [1, 0]}
habitsHistory = pd.DataFrame(exampleData).set_index(["date"])

print(habitsHistory)
habitsHistory.drop(date.today(), inplace=True)
print(habitsHistory)