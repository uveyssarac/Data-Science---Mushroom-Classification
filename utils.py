import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.impute import SimpleImputer
def draw_decision_boundaries(X, y, X_test, y_test, clf, legends):
    # Create color maps
    cmap_light = ListedColormap(['#FFFFAA', '#EFEFEF'])
    cmap_bold = ['#EEEE00', '#000000']

    h = 0.02  # step size in the mesh
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].

    

    
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        palette=cmap_bold,
        hue=legends,
        alpha=1.0,
        edgecolor="black",
        s=50
    )

    plt.title(f"Train Score: {clf.score(X, y):.2f}, Test Score: {clf.score(X_test, y_test):.2f}")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())