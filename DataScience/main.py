import pandas

pandas.options.display.float_format = '{:,.2f}'.format
data = pandas.read_csv('salaries_by_college_major.csv')
log = data.isna()
# print(log)
# print(data.tail())

clean_df = data.dropna()
"""Question 1"""
major = clean_df['Undergraduate Major'][8]
print(major)
earning = clean_df['Mid-Career Median Salary'][8]
print(earning)

"""Question 2"""
print()
college = clean_df['Undergraduate Major'][49]
print(college)
collegEarn = clean_df['Mid-Career Median Salary'][49]
print(collegEarn)

"""3"""
print()
col = clean_df['Undergraduate Major'][18]
print(col)

edu = clean_df['Mid-Career Median Salary'][18]
print(edu)

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())

print()
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())


print()
top5 = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)

print(top5[['Undergraduate Major']].head())

print()
greatSpread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)


print(greatSpread[['Undergraduate Major', 'Mid-Career Median Salary']].head())

""" Using groupby Method"""
print()
groups = clean_df.groupby('Group').count()
print(groups)