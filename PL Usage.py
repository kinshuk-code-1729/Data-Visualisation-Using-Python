import matplotlib.pyplot as plt
import numpy as np
prog_languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(prog_languages))
performance = [10,7,6,4,2,1]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, prog_languages)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()
