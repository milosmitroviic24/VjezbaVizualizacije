import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 0. Ucitavanje dataset-a
titanic_df = pd.read_csv("Titanic-Dataset.csv")

# 1. Univarijantna analiza

# 1.a. histogram godina (Age)
# Prikaz cjelokupne raspodjele varijable Age
sns.histplot(x = 'Age', data = titanic_df, bins = 10, kde = True)
plt.title("Histogram of Age distribution")
plt.show()

# 1.b. bar plot za Pclass, Sex, Embarked
# Pclass
sns.countplot(x = "Pclass", data = titanic_df)
plt.title("Count values of Pclass")
plt.show()
# Sex
sns.countplot(x = "Sex", data = titanic_df)
plt.title("Count values of Sex")
plt.show()
# Embarked
sns.countplot(x = "Embarked", data = titanic_df)
plt.title("Count values of Embarked")
plt.show()

# 2. Bivarijantna analiza

# 2.a. boxplot: Age po Survived
sns.boxplot(data = titanic_df, x = "Survived", y = "Age")
plt.title("Boxplot Age per Survived")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()

# 2.b. countplot: Survived po Sex
sns.countplot(data = titanic_df, x = "Survived", hue = "Sex")
plt.title("Countplot: Survived per Sex")
plt.xlabel("Sex")
plt.ylabel("Survived values")
plt.show()

#2.c. barplot: Prosjecan Fare po Pclass
sns.barplot(data = titanic_df, x = "Pclass", y = "Fare", ci = None, estimator = 'mean')
plt.title("Average Fare by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Average Fare")
plt.show()

# 3. Multivarijantna analiza

# 3.a. Heatmap korelacije numerickih kolona
mc = titanic_df.corr(numeric_only = True)
sns.heatmap(mc, annot = True, cmap = 'coolwarm')
plt.title("Correlation matrix of numeric attributes")
plt.show()

# 3.b. Scatterplot Age vs Fare, colored by Survived value
sns.scatterplot(data = titanic_df, x = "Age", y = "Fare", hue = "Survived")
plt.title("Scatterplot Age vs Survived, colored by Survived")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()