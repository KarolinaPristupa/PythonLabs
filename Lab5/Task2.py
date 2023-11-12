import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    'your_column': np.random.randn(1000),
    'number_of_rooms': np.random.randint(1, 4, size=1000),
    'district': np.random.choice(['A', 'B', 'C'], size=1000)
}

df = pd.DataFrame(data)
df.to_csv('real_estate_dataset.csv', index=False)

df = pd.read_csv("real_estate_dataset.csv")

df_sample = df.sample(n=1000, random_state=42)

mis = df_sample.isnull().sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(x=df_sample['your_column'], ax=axes[0])
axes[1].set_title('Ящик с усами')

sns.histplot(np.log1p(df_sample['your_column']), bins=30, kde=True, ax=axes[1])
axes[1].set_title('Гистограмма на логарифмической шкале')

plt.show()

r_c = df_sample['number_of_rooms'].value_counts()
pivot_table = pd.pivot_table(df_sample, values='your_column', index='district', columns='number_of_rooms', aggfunc='count')

df_sample.to_csv('TASK2.csv', index=False)



