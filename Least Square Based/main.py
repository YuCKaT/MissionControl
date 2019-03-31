import json
import datetime
from operator import itemgetter

with open('views4.json','r') as d:
          all_data = json.load(d)

last_revit_date = all_data['viewStats'][-1]['createdOn'][:10]+ " " + all_data['viewStats'][-1]['createdOn'][12:-9]
initial_revit_date = all_data['viewStats'][0]['createdOn'][:10]+ " " + all_data['viewStats'][0]['createdOn'][12:-9]
current_totalViews = all_data['viewStats'][-1]['totalViews']
delta_time = (datetime.datetime.strptime(last_revit_date,'%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(initial_revit_date,'%Y-%m-%d %H:%M:%S')).seconds

d.close()

count = 1
import json
import datetime

with open('views4.json','r') as z:
        project_data = json.load(z)


if count == 1:
    revit_data = project_data['viewStats']
else:
    revit_data.appended(project_data['viewStats'])
z.close()


# Set the parameter
x_time = []
y_totalViews = []
totalViews_from_data = []
delta_x = 0
D= {}
for e in revit_data:
    a_time = e['createdOn'][:10]+ " " + e['createdOn'][12:-9]
    time = datetime.datetime.strptime(a_time,'%Y-%m-%d %H:%M:%S')
    y_totalViews.append(e['totalViews'])
    if count == 1:
        delta_time = 0
        x_time.append(delta_time)
        initial_time = time
        count += 1
    elif count >= 2:
        delta_time = float((time - initial_time).seconds)
        x_time.append(delta_time)
        count += 1
        #Calculate ideal curve



def revit_machine(current_date, x_time, y_totalViews):
    x_sum = 0.0
    y_sum = 0.0
    xx_sum = 0.0
    yy_sum = 0.0
    xy_sum = 0.0
    length = len(x_time)
    for f in range(len(x_time)):
        x_sum = x_sum + x_time[f-1]
        y_sum = y_sum + float(y_totalViews[f-1])
        xx_sum = xx_sum + x_time[f-1]**2
        yy_sum = yy_sum + y_totalViews[f-1]**2
        xy_sum = xy_sum + x_time[f-1] * y_totalViews[f-1]

    a = ( length * xy_sum - x_sum * y_sum) / (length * xx_sum - x_sum** 2 )
    b = (xx_sum * y_sum - xy_sum * x_sum) / (length * xx_sum - x_sum ** 2 )
    #Culculate ideal number
    ideal_total_Views = a * current_date + b
    return ideal_total_Views

for j in range(len(x_time)):
    totalViews_from_data.append(revit_machine(x_time[j-1], x_time, y_totalViews))

D = x_time + y_totalViews + totalViews_from_data

file = open('Inputdata.txt', 'w')
file.writelines(str(D))
file.close()

previous_data_totalView = revit_machine(delta_time, x_time, y_totalViews)


if current_totalViews > previous_data_totalView:
    print("This project file should be purged")

else:
    print("Greate job!!")
