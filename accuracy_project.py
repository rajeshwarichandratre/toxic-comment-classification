import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import itertools


objects = ('MultinomialNB','SVM','KNN','XGBoost','LSTM')
y_pos = np.arange(len(objects))
performance = [89.01, 89.69, 89.97, 91.34, 96.37]

colors = itertools.cycle(['m','c','y','g','b'])
for i in range(len(performance)):
    plt.bar(y_pos[i], performance[i], color=next(colors))

plt.xticks(y_pos, objects)
plt.ylabel('ROC')
plt.title('ROC values for different models')

plt.show()