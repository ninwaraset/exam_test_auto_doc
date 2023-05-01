import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
df1 = pd.read_excel('EX1.xlsx' ,sheet_name=[0, 'Sheet5'])
 
# print(dataframe1)
print(df1['Sheet5'])



x = df1['Sheet5']['x_a']*1000
y = df1['Sheet5']['y_a']*1000
z = df1['Sheet5']['z_a']*1000

mean_x = st.mean(x)
mean_y = st.mean(y)
mean_z = st.mean(z)


# print(x)
# print(mean_x)
print("")
print("------------------------")
print("Error x (mm)")
e_x = x-mean_x
e_x = round(e_x,2)
print(e_x)

# print("")
# print("------------------------")
# print("Error y (mm)")
# e_y = y-mean_y
# e_y = round(e_y,2)
# print(e_y)


# print("")
# print("------------------------")
# print("Error z (mm)")
# e_z = z-mean_z
# e_z = round(e_z,2)
# print(e_z)

fig = plt.gcf()
ax = fig.gca()
circle1 = plt.Circle((0,0),10,ls = "--", color='m', fill=False)
# circle3 = plt.Circle((x_list[idx_vtx_tri],y_list[idx_vtx_tri]), 0.35, color='g', fill=False)

# ax = plt.gca()
# ax.cla() # clear things for fresh plot
ax.add_patch(circle1)



for i in range(len(x)):
    # plt.plot(x[i],0,("b."))
    plt.plot(e_x[i],0,("b."))
    # print((x[i]-mean_x[i]))

    # print(str(round((x[i]-mean_x),3))+" mm")

# plt.plot(mean_x,0,"rX")



plt.show()