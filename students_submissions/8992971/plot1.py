import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")

x = df['Age']
y = df['Cholesterol']

#############LINE GRAPH######################

plt.figure(figsize=(10, 6))
plt.plot(df['Age'], df['Cholesterol'], marker='o', linestyle='-', color='b')
plt.title('Age vs. Cholesterol (Line Plot)')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.grid(True)
plt.show()


#########################BAR PLOT##########################


sex_counts = df['Sex'].value_counts()
plt.figure(figsize=(8, 6))
sex_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Males and Females')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()



#############HISTOGRAM##########################################


plt.figure(figsize=(10, 6))
plt.hist(df['Blood Pressure'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Blood Pressure')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


################SCATTER PLOT############################################

plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Cholesterol'], color='red', alpha=0.5)
plt.title('Age vs. Cholesterol (Scatter Plot)')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.grid(True)
plt.show()



