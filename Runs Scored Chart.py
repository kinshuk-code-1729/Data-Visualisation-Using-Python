import matplotlib.pyplot as plt

runs = [77, 22, 42, 103]
players = ['Rohit Sharma', 'M.S.Dhoni', 'Jaspreet Bumrah', 'Virat Kohli']
cols = ['c', 'm', 'r', 'b']
plt.pie(runs, labels=players, colors=cols, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')
plt.title('Runs Scored Chart')
plt.show()
