Trabajo Práctico Clasificación

# Integrantes:

* Augusto Kark
* Lucas Garcia

# ---

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer


data = load_breast_cancer()

df = pd.DataFrame(data=data.data, columns=data.feature_names)

df.info()


