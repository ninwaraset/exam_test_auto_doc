import pandas as pd
import matplotlib.pyplot as plt

# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
df1 = pd.read_excel('EX2.xlsx' ,sheet_name=[0, 'Sheet3'])
 
# print(dataframe1)
print(df1['Sheet3'])
# print(df1['Sheet3']['x'])
label = df1['Sheet3']['result']
x = df1['Sheet3']['x']
y = df1['Sheet3']['y']
note = df1['Sheet3']['note']
mirror = 0
list_work_x = []
list_work_y = []
# print(label)
# print(label[1])
for i in range(len(label)):
    # print(str(i+1)+" : "+str(label[i]))
    if note[i] == "*":
        plt.plot(x[i],y[i],'m|')
    else:
        if label[i] == 1:
            plt.plot(x[i],y[i],'b.')
            list_work_x.append(x[i])
            list_work_y.append(y[i])
            if mirror == 1 :
                plt.plot(-x[i],y[i],marker='+',color="c")
        elif label[i]== 0:
            plt.plot(x[i],y[i],'rx')
            if mirror == 1 :
                plt.plot(-x[i],y[i],marker='1',color="orange")
        else:
            plt.plot(x[i],y[i],'gP')
fig = plt.gcf()
ax = fig.gca()
center_x = ((max(list_work_x)+min(list_work_x))/2)*0
center_y = ((max(list_work_y)+min(list_work_y))/2)+0
center_y = round(center_y,3)
print("center : "+str((center_x,center_y)))
plt.plot(center_x,center_y,"k*")
shift_text = [-0.09,0.05]
plt.text(center_x+shift_text[0],center_y+shift_text[1],(center_x,center_y),color = "k",fontsize="small",alpha =0.5)
# plt.text(center_x,center_y,(center_x,center_y),color = "r",fontsize="small",alpha =0.5,multialignment='center')


fig = plt.gcf()
ax = fig.gca()
circle1 = plt.Circle((center_x,center_y), 0.45,ls = "--", color='m', fill=False)
circle2 = plt.Circle((center_x,center_y), 0.5,ls = "-.", color='c', fill=False)
circle3 = plt.Circle((center_x,center_y), 0.60,ls = "dotted", color='y', fill=False)



ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

plt.show()

