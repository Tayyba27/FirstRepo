#import seaborn as sns
import pandas as pd

# import dat from file
chilla = pd.read_csv("data_chilla.CSV")
print(chilla)


# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
chilla = pd.read_csv("data_chilla.CSV")

# draw a line  plot
sns.lineplot(x="Gender", y="Age", data=chilla)
plt.title("Data Scientists")
plt.show()



# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets

chilla = pd.read_csv("data_chilla.CSV")
# draw a line  plot
sns.lineplot(x="Age", y="Gender", data=chilla)
plt.title("Data Scientists")
plt.show()

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
chilla = pd.read_csv("data_chilla.CSV")

# draw a line  plot
sns.lineplot(x="Gender", y="Age", hue= "Location" ,data=chilla)
plt.show()

 #import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
chilla = pd.read_csv("data_chilla.CSV")

# draw a line  plot
sns.lineplot(x="Age", y="Gender", hue= "Location", data=chilla ,color= "red",
           palette='pastel')
plt.show()

# import libraries
import seaborn as sns
from numpy import median
import matplotlib.pyplot as plt

# Load data
chilla = pd.read_csv("data_chilla.CSV")
# draw a line  plot
sns.lineplot(x="Gender", y="Age", hue= "Location", data=chilla, estimator=median)
plt.show()
















