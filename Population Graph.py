import matplotlib.pyplot as plotter
pieLabels = 'Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia'
populationShare = [59.69, 16, 9.94, 7.79, 5.68, 0.54]
figureObject, axesObject = plotter.subplots()
explodeTuple = (0.1, 0.0, 0.0, 0.0, 0.0, 0.8)
axesObject.pie(populationShare, explode=explodeTuple,labels=pieLabels,autopct='%1.2f',startangle=90)
axesObject.axis('equal')
plotter.show()
