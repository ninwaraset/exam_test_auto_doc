import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20])

for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.show()
