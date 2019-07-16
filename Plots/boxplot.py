import matplotlib.pyplot as plt

  
value1 = list(ans['Sklearn'][0].values())
value2=list(ans4['Shogun'][0].values())
value3=list(ans2['GPy'][0].values())
value4=list(ans2['GPytorch'][0].values())
value5=list(ans2['GPflow'][0].values())
value6=list(ans3['ot'][0].values())
  
plt.figure()
box_plot_data=[value1,value2,value3,value4,value5,value6]
plt.boxplot(box_plot_data)
plt.xlabel('libraries')
plt.ylabel('EMRMSE')
plt.boxplot(box_plot_data,patch_artist=True,labels=['Sklearn','Shogun','GPy','GPytorch','GPflow','Openturns'])
plt.show()

