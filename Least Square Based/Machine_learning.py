Class machine_learning:
    import json
    import datetime
    import numpy as np
    import matplotlib.pyplot as plt

    with open('views4.json','r') as d:
            project_data = json.load(d)
    If count == 1:
        revit_data = project_data['viewStats']
    else:
        revit_data.appended(project_data['viewStats'])
    d.close()
        # Set the parameter
    x_time = []
    y_totalViews = []
    delta_x = 0
    count = 1
    for e in revit_data:
        a_time = e['createdOn'][:10]+ " " + e['createdOn'][12:-9]
        time = datetime.datetime.strptime(a_time,'%Y-%m-%d %H:%M:%S')
        y_totalViews.append(e['totalViews'])
        if count == 1:
            delta_time = 0
            x_time.append(delta_time)
            initial_time = time
            count += 1
        elif count > 2:
            delta_time = float((time - initial_time).seconds)
            x_time.append(delta_time)
            count += 1
            #Calculate ideal curve
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
        b = (xx_su-m * y_sum - xy_sum * x_sum) / (length * xx_sum - x_sum ** 2 )

    def __init__(self, current_date):
        self.revit_machine(current_date) = current_date


        # create data base
    def revit_machine(self, current_date):
                #Culculate ideal number
                ideal_total_View = a * current_date + b
            return self.ideal_totalViews
