from sklearn.datasets import load_iris
from sklearn import tree
from IPython.display import Image
import pydotplus
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf)
# Create DOT data
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

# Show graph
graph.write_pdf("iris.pdf")
graph.write_png("iris.png")
