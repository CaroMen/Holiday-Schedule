import csv
import pandas as pd
import numpy as np

# CREATE DATAFRAME FROM CSV FILE
schedule_info = pd.read_csv('Holiday_Schedule_Ranking_2019.csv',
                            index_col=0, squeeze=True).T

print(schedule_info)

schedule = pd.read_csv('Holiday_Schedule_Ranking_2019.csv', index_col=0)

for column in schedule.columns:
    schedule[column].values[:] = 0

schedule_info = schedule_info.T

print(schedule_info)

N = 4

schedule_info = schedule_info.mask(schedule_info.rank(
    axis=1, method='min', ascending=True) > N, 0)
print(schedule_info)

N_Two = 3
schedule_info2 = schedule_info.mask(schedule_info.rank(
    axis=0, method='min', ascending=False) < N_Two, 0).drop_duplicates(subset=None, keep=False, inplace=False)
print(schedule_info2)
