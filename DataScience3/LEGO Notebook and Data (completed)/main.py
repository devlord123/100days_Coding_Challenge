import pandas as pd
import matplotlib.pyplot as plt


color_dt = pd.read_csv('data/colors.csv')
total_color = color_dt.name.nunique()
trans = color_dt.is_trans.value_counts()
print(trans)

set_dt = pd.read_csv('data/sets.csv')
theme_dt = pd.read_csv('data/themes.csv')
print(set_dt.sort_values('year').head)
print(set_dt[set_dt.year == 1949])
print(set_dt.sort_values('num_parts', ascending=False).head())

sets_by_year = set_dt.groupby('year').count()


themes_by_year = set_dt.groupby('year').agg({
    'theme_id': pd.Series.nunique
})

themes_by_year.rename(columns={
    'theme_id': 'nr_themes'
}, inplace= True)

parts_per_set = set_dt.groupby('year').agg({
    'num_parts': pd.Series.mean
})

#------------Number of Sets per LEGO Theme----------
set_theme_count = set_dt.theme_id.value_counts()
# print(set_theme_count.head())
theme = theme_dt[theme_dt.name == 'Star Wars']
all_id = set_dt[set_dt.theme_id == 209]
print(all_id.groupby('year').agg({
    'theme_id': pd.Series.mean
}))

#-------------- MERGING TWO DATAFRAMES WITH .merge() method-------------------
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values
})

merged_df = pd.merge(
    set_theme_count,
    theme_dt,
    on='id'
)



#-------------- DATA VISUALIZATION -------------------

#---------PLOTTING BOTH GRAPH ON DIFFERENT AXIS------------
axis1 = plt.gca()
axis2 = axis1.twinx()


axis1.set_xlabel('Year')
axis1.set_ylabel('Number of Sets', color='red')
axis2.set_ylabel('Number of Themes', color='green')

#-------------------DISPLAYING EACH GRAPHS-------------------
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14, rotation=90)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
axis1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], 'b')
axis2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'g')

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])


# BAR CHART
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()