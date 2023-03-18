# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
phool = sns.load_dataset("iris")
phool

# draw a line  plot
sns.lineplot(x="sepal_length", y="sepal_width", data=phool)
plt.show()


# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
phool = sns.load_dataset("iris")
phool

# draw a line  plot
sns.lineplot(x="sepal_length", y="sepal_width", data=phool)
plt.title("phoolon ka plot")
plt.xlim(2)
plt.ylim(1)
plt.show()

# Size of figure
# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
phool = sns.load_dataset("iris")
# change figure
plt.figure(figsize=(5,3))

# draw a line  plot
sns.lineplot(x="sepal_length", y="sepal_width", data=phool)
plt.title("phoolon ka plot")
plt.set_style("dark")






