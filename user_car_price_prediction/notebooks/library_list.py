import pandas as pd ; pd.set_option("display.precision",8)
import numpy as np ; np.set_printoptions(precision=7)
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import os ; os.chdir("../")
from src.data.data_eda import *


# 시각화 설정
colors = [plt.cm.Dark2(i) for i in range(20)]
mpl.rcParams.update({'font.size':18,'axes.formatter.useoffset':False})

train, test = train_test_reader()