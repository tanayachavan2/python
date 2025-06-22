import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv("marks.csv") # Reads the marks.csv file into a DataFrame df

# Print first few rows
print("📊 Student Marks Data:")
print(df.head())

# Plot 1: Bar chart of total marks per student
df["Total"] = df[["Math", "Science", "English", "History"]].sum(axis=1)  #Adds a new column called Total ,It adds up Math + Science + English + History for each student (axis=1 means row-wise)

plt.figure(figsize=(8,5))    #Creates a figure window that is 8 inches wide and 5 inches tall.

sns.barplot(
    x="Name", 
    y="Total",
    data=df,
    hue="Name",
    palette="pastel",
    legend=False
    )    
#palette="pastel" sets light, soft colors 
#can be used so that Tells Seaborn to apply a different color for each name using hue Hides the legend using legend=False


plt.title("Total Marks per Student")   #Adds a title and axis labels 

plt.ylabel("Marks")

plt.xlabel("Student")

plt.ylim(0, 400)   #Limits Y-axis from 0 to 400

plt.grid(True)  #Adds grid lines for readability

plt.tight_layout()  #prevents label cutoff

plt.show()   #displays the plot


# Plot 2: Subject-wise average marks (line plot)
subject_avgs = df[["Math", "Science", "English", "History"]].mean()

plt.figure(figsize=(7,4))

subject_avgs.plot(
    kind='line', 
    marker='o', 
    color='green')   #Each point = one subject's average ,marker='o' adds circles on data points color='green' sets line color

plt.title("Average Marks per Subject")

plt.ylabel("Average Marks")

plt.grid(True)

plt.tight_layout()

plt.show()

# Plot 3: Heatmap of student performance
plt.figure(figsize=(7,5))

sns.heatmap(
    df.drop("Total", axis=1).set_index("Name"), 
    annot=True, 
    cmap="YlGnBu")   #Drops the "Total" column ,Sets student names as the row labels, annot shows the numbers on the grid,"YlGnBu" is a blue-green color scale
plt.title("Student Performance Heatmap")  # shows all scores as color grid

plt.tight_layout()

plt.show()

