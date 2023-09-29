import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("Employee.csv")
df = pd.DataFrame(data)
dfh = df.head(20)
dfh.plot(x="Education", y="ExperienceInCurrentDomain", kind="bar",title="Employee dataset")
plt.show()