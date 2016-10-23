# путь к файлу структур
structure_filepath = 'course-217-structure.csv'
# путь к файлу событий
events_filepath = 'course-217-events.csv'

import csv
from operator import itemgetter

data = []
data_sort = []
user_scores = []
start_times = []
finish_times = []
users = []
times = []
top = []

structure = []
step_costs = []
step_ids = []

user_id = 0
action = 1
step_id = 2
time = 3
step_id_s = 0
step_cost = 1
max_point = 24



with open(structure_filepath) as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        structure.append([int(row['step_id']),int(row['step_cost'])])

with open(events_filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        users.append(int(row['user_id']))
        data.append([int(row['user_id']),row['action'],int(row['step_id']),int(row['time'])])
        data_sort.append([int(row['user_id']),row['action'],int(row['step_id']),int(row['time'])])

users = set(users)
data_sort.sort(key = itemgetter(3))

data_len = len(data_sort)

for j in range(len(structure)):
    step_costs.append(structure[j][1])
    step_ids.append(structure[j][0])

for j in range(len(users)):
    user_scores.append([0,0,j+1])
    finish_times.append([0,j+1])
    start_times.append([1465181037,j+1])

start_times_len = len(start_times)


for current in range(data_len):
    user = data_sort[current][0]
    action = data_sort[current][1]
    step_id = data_sort[current][2]
    time = data_sort[current][3]
    times.append([time,user])
    step_index = step_ids.index(step_id)
    step_cost = step_costs[step_index]
    if time < start_times[user-1][0]:
                start_times[user-1][0] = time
    if action == 'passed' and step_cost != 0:
        user_scores[user-1][0] += step_cost
        user_scores[user-1][1] = time
        if user_scores[user-1][0] == max_point:
            finish_times[user-1][0] = time


for count in range(len(user_scores)):
    tmp_user = user_scores[count][2]
    if user_scores[count][0] >= max_point:
        time_difference = finish_times[count][0] - start_times[count][0]
        top.append([time_difference,tmp_user])

top.sort(key = itemgetter(0))

for i in range(10):
    if i != 9:
        print(top[i][1],", ",sep="",end="")
    else:
        print(top[i][1],sep="",end="")
