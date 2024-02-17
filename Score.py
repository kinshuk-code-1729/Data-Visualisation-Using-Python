import matplotlib.pyplot as plt

sem = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
sgpa = [9.48, 9.48, 9.79, 7.42, 7.96, 8.29, 8.79]
cpga = [9.48, 9.48, 9.59, 9.01, 8.79, 8.70, 8.72]
plt.plot(sem, sgpa, 'b', label='SGPA', linestyle='dashed', linewidth=3)
plt.plot(sem, cpga, 'y', label='CPGA', linestyle='dashdot', linewidth=3)
plt.xlabel('Semesters')
plt.ylabel('CGPA and SGPA')
plt.title("Kinshuk's Engineering Score")
plt.grid(True)
plt.legend()
plt.show()
