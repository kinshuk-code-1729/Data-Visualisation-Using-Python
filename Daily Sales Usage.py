import matplotlib.pyplot as plt
sales1 = [1, 3, 8, 9, 11]
sales2 = [2, 5, 9, 11, 13]
line_chart1 = plt.plot(range(1,6), sales1,'--')
line_chart2 = plt.plot(range(1,6), sales2,':')
plt.title('Daily sales of Salesman1 and Salesman2')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.legend(['Sales of salesman 1', 'Sales of salesman 2'], loc=4)
plt.show()
