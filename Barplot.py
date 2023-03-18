# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
phool = sns.load_dataset("iris")
phool

# draw a line  plot
sns.barplot(x="species", y="sepal_width", data=phool)
#plt.title("phoolon ka plot")
plt.show()

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
phool = sns.load_dataset("iris")
phool

# draw a line  plot
sns.barplot(x="species", y="petal_length", data=phool)
#plt.title("phoolon ka plot")
plt.show()

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="who", y="alone", data=kashti)
plt.show()

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="who", y="alone", hue= "sex", data=kashti)
plt.show()



# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="sex", y="alone", hue= "who", data=kashti ,order=["female","male"])
plt.show()

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="sex", y="alone", hue= "who", data=kashti ,order=["female","male"] ,color= "red", ci=None)
plt.show()

# import libraries
import seaborn as sns
import numpy
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="class", y="fare", hue= "sex", data=kashti, estimator=median)
plt.show()

# import libraries
import seaborn as sns
import numpy
import matplotlib.pyplot as plt

# Load datasets
kashti = sns.load_dataset("titanic")
kashti

# draw a line  plot
sns.barplot(x="class", y="fare", hue= "sex", data=kashti, estimator=median, saturation=0.5 )
plt.show()

























