import matplotlib.pyplot as plt
import seaborn as sns
#Sample Data 
hours=[1,2,3,4,5]
marks=[20,40,76,78,87]

#Scatterplot
sns.scatterplot(x=hours, y=marks)
plt.title('hours Study vs marks')
plt.xlabel('hours Stuied')  
plt.ylabel('marks obtained')
plt.show() 