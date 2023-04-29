"""
    DATA SCIENCE WITH PYTHON LIBRARIES SUCH AS [PANDAS, NUMPY]
    DATA VISUALIZATION WITH PYTHON LIBRARIES SUCH AS MATPLOITLIB
"""
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("Results.csv", names=['DATE', 'TAGS', 'POSTS'], header=0)
data.DATE = pd.to_datetime(data.DATE)
# print(data.head)
# print(data.tail)
# print(data.groupby('TAGS').sum())
# print("Minimum language is ")
# print(data.groupby('TAGS').count().idxmin())
# print(data)

reshaped_df = data.pivot(index='DATE', columns='TAGS', values='POSTS')
reshaped_df.fillna(0, inplace=True)

# print(reshaped_df.count())
# print(reshaped_df)

# checkNan = reshaped_df.isna().values.any()
# print(checkNan)


#----------------DATA VISUALIZATION -------------------#

print("Welcome To MatPlotLib")

# plt.figure(figsize=(10,5))
# plt.xlabel('Date', fontsize=10)
# plt.ylabel('Post numbers', fontsize=10)
# plt.ylim(0, 35000)
# for col in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[col],
#              linewidth=1, label=reshaped_df[col].name)


# USE ROLLING() AND MEAN() FOR BETTER VISUALIZATION OF DATA BY CALCULATING THE AVERAGE IN WINDOW.
roll_df = reshaped_df.rolling(window=5).mean()
plt.figure(figsize=(10,5))
plt.xlabel('Date', fontsize=10)
plt.ylabel('Post numbers', fontsize=10)
plt.ylim(0, 35000)
for col in roll_df.columns:
    plt.plot(roll_df.index, roll_df[col],
             linewidth=1, label=roll_df[col].name)

plt.legend(fontsize=9)
plt.show()

