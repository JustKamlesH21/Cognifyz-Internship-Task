import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def simple_visualizations(csv_file):
    df = pd.read_csv(csv_file)

    # Age distribution histogram
    plt.hist(df['Age'], bins=20, edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig("age_distribution.png")
    plt.close()

    # Glucose vs BMI scatter plot colored by Outcome
    sns.scatterplot(data=df, x='BMI', y='Glucose', hue='Outcome')
    plt.title('Glucose vs BMI by Outcome')
    plt.savefig("glucose_bmi_scatter.png")
    plt.close()

if __name__ == "__main__":
    simple_visualizations('LeveL_3/diabetes.csv')
