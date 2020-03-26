import pandas as pd 
Sahabat = pd.Series(['Ali', 'Umar', 'Usman', 'Abu Bakar'])
print(Sahabat)

#series dengan index
khalifah  = pd.Series(['Ali',  'Umar', 'Usman', 'Abu Bakar'],
index = ["4th", "2nd", "3rd", "1st"])
print(khalifah )