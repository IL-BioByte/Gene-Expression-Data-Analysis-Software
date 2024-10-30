####BAR PLOTS####
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df):
    df.plot(kind='bar')
    plt.title('Gene Expression Levels')
    plt.ylabel('Normalized Expression')
    plt.xlabel('Sample ID')
    plt.show()

###PCA###

import pandas as pd
df = pd.read_excel('data/gene-expression-fake-data.xlsx')
treatment = df['Treatment']
X = df.iloc[:, 1:]
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize the data
X_scaled = StandardScaler().fit_transform(X)

# Perform PCA
pca = PCA()
principal_components = pca.fit_transform(X_scaled)

# Create a DataFrame with the principal components
pca_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(pca.n_components_)])
pca_df['Treatment'] = treatment

import matplotlib.pyplot as plt
import seaborn as sns

# Create the biplot
plt.figure(figsize=(10, 7))

# Scatter plot for the PCA results
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Treatment', palette='Dark2', s=100)

# Add ellipses
from matplotlib.patches import Ellipse
from scipy.stats import chi2

def draw_ellipse(ax, mean, cov, color, label=None):
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    angle = np.arctan2(eigenvectors[0, 1], eigenvectors[0, 0])
    angle = np.degrees(angle)
    width, height = 2 * np.sqrt(chi2.ppf(0.95, 2)) * np.sqrt(eigenvalues)

    ell = Ellipse(mean, width, height, angle=angle, color=color, alpha=0.5, label=label)
    ax.add_patch(ell)

for treatment in pca_df['Treatment'].unique():
    subset = pca_df[pca_df['Treatment'] == treatment]
    mean = subset[['PC1', 'PC2']].mean().values
    cov = np.cov(subset[['PC1', 'PC2']].T)
    draw_ellipse(plt.gca(), mean, cov, color=sns.color_palette('Dark2')[treatment])

plt.title('PCA Biplot')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Treatment')
plt.grid()
plt.savefig('PCA_Biplot.jpeg', dpi=300)
plt.show()
