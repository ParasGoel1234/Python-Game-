from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
iris = datasets.load_iris()
print(list(iris.keys()))
X = iris['data'][:, 3:]
y = (iris['target'] == 2).astype(np.int)
# print(X)
# print(y)
clf = LogisticRegression()
clf.fit(X,y)
example = clf.predict(([[2.6]]))
print(example)
x_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:, 1], "g-")
plt.show()

# print(iris['DESCR'])
# features = iris.data
# labels = iris.target
# print(features[0], labels[0])
