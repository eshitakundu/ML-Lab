# ML-Lab

Machine Learning lab assignments — end-to-end Jupyter notebooks covering supervised and
unsupervised learning on real datasets, plus a couple of standalone sorting exercises.

Each assignment follows the same shape: load the data → exploratory data analysis →
preprocessing → model training → evaluation and visualisation.

## Contents

| Assignment | Topic | Notebook | Dataset(s) |
|---|---|---|---|
| 1 | Linear Regression (univariate & multivariate) | `Linear Regression/Linear Regression.ipynb` | `Used_Car_Dataset.csv`, `Housing.csv`, `Fuel_Consumption_2000-2022.csv` |
| 2 | Decision Tree classification | `Decision Tree/drug.ipynb` | `drug.csv` |
| 3 | K-Means clustering | `k-means clustering/cust.ipynb` | `Cust_Segmentation.csv` |
| 4 | Hierarchical (agglomerative) clustering | `hierarchical/Vehicle.ipynb` | `cars_clustering.csv` |
| — | Sorting algorithms | `merge_sort.py`, `quick_sort.py` | — |

## Assignments

### 1. Linear Regression

Predicts used-car price, house price and vehicle fuel consumption. For every dataset the
notebook runs EDA (info/describe, missing values, IQR outlier detection, distribution and
correlation plots) and then fits both a **univariate** and a **multivariate** model.

Alongside scikit-learn's `LinearRegression`, it implements **gradient descent from scratch**
(`gradient_descent()` with a cost history and a `1e-6` convergence tolerance) so the closed-form
and iterative solutions can be compared. Models are scored with MSE, MAE and R².

- `Used_Car_Dataset.csv` — 1,000 rows: year, mileage, engine size, owners, fuel efficiency → `Price_INR`
- `Housing.csv` — 545 rows: area, bedrooms, bathrooms, stories, amenities → `price`
- `Fuel_Consumption_2000-2022.csv` — 22,555 rows: make, model, engine size, cylinders, transmission, fuel type → consumption & emissions

### 2. Decision Tree

Given a patient's health profile (age, sex, blood pressure, cholesterol, sodium-to-potassium
ratio), predicts which of `DrugA`, `DrugB`, `DrugC`, `DrugX` or `DrugY` should be prescribed.

Categorical features are `LabelEncoder`-encoded, the data is split 80/20, and a
`DecisionTreeClassifier` is trained and evaluated with accuracy, a classification report,
macro precision/recall/F1, and a confusion matrix. The fitted tree is rendered with `plot_tree`.

- `drug.csv` — 199 rows, 6 columns

### 3. K-Means Clustering

Segments bank customers by demographic and financial features (age, education, years employed,
income, card debt, other debt, debt-to-income ratio).

Non-informative columns are dropped, features are standardised, and clustering is run **twice**:

- **Euclidean** — scikit-learn `KMeans`, with the Elbow Method (k = 1…9) confirming k = 3
- **Manhattan** — a hand-rolled K-Means using `scipy.spatial.distance.cdist` with the L1 metric

Both are compared by silhouette score and visualised in 2D and 3D. On this dataset the Manhattan
variant yields better-separated clusters, likely because L1 is more robust to outliers.

- `Cust_Segmentation.csv` — 849 rows, 10 columns

### 4. Hierarchical Clustering

Groups vehicles by their specifications (sales, resale value, price, engine size, horsepower,
wheelbase, width, length, curb weight, fuel capacity, MPG).

Cleaning handles the dataset's `$null$` placeholders by coercing them to `NaN` and filling them
with a `KNNImputer` (k = 5). After standardisation, dendrograms are plotted for **single**,
**complete** and **average** linkage, and `AgglomerativeClustering` with average linkage cuts the
tree into 4 clusters, which are then profiled by their per-feature means.

- `cars_clustering.csv` — 158 rows, 16 columns

### Sorting algorithms

Two small standalone scripts — recursive `merge_sort` and `quick_sort` implementations, each with
a demo call at the bottom.

```bash
python merge_sort.py
python quick_sort.py
```

## Getting started

Developed against **Python 3.13** using a local `venv` kernel.

```bash
git clone <repo-url>
cd ML-Lab

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install pandas numpy matplotlib seaborn scikit-learn scipy notebook
```

Then launch Jupyter and open any notebook:

```bash
jupyter notebook
```

Notebooks read their data with paths relative to their own folder (e.g. `Datasets/drug.csv`), so
run each one with its assignment directory as the working directory — which is what Jupyter does
by default when you open a notebook in place.

## Repository layout

```
ML-Lab/
├── Linear Regression/
│   ├── Linear Regression.ipynb
│   └── Datasets/
│       ├── Used_Car_Dataset.csv
│       ├── Housing.csv
│       └── Fuel_Consumption_2000-2022.csv
├── Decision Tree/
│   ├── drug.ipynb
│   └── Datasets/drug.csv
├── k-means clustering/
│   ├── cust.ipynb
│   └── Datasets/Cust_Segmentation.csv
├── hierarchical/
│   ├── Vehicle.ipynb
│   └── Datasets/cars_clustering.csv
├── merge_sort.py
└── quick_sort.py
```

## Tech stack

`pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `scipy`
