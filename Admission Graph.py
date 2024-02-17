import matplotlib.pyplot as pl
import numpy as np

boy = [28, 45, 10, 30]
girl = [14, 20, 36, 50]
X = np.arange(4)  # creates a list of 4 values [0,1,2,3]
pl.bar(X, boy, width=0.2, color='r', label="boys")
pl.bar(X + 0.2, girl, width=0.2, color='b', label="girls")
pl.legend(loc="upper left")
pl.title("Admissions per week")
pl.xlabel("week")
pl.ylabel("admissions")
pl.show()
