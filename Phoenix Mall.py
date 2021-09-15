import matplotlib.pyplot as plt
qdata=[100,200,250,150]
lb=['Q1SALE','Q2SALE','Q3SALE','Q4SALE']
plt.pie(qdata, labels=lb,explode=[0.2,0,0,0] )
plt.title('PHOENIX MALL')
plt.show()
