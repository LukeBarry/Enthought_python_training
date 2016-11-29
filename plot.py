# First, we'll import pandas, a data processing and CSV file I/O library
import pandas as pd
import numpy as np

# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# load the data with pandas csv reader
demographics = pd.read_csv("C:\Users\lbarry\Desktop\All folders\ssd\ssd_all_inactive_2000-2016.csv") # the iris dataset is now a Pandas DataFrame
enrollment = pd.read_csv("C:\Users\lbarry\Desktop\All folders\enroll-withdraw\Enrollment Trends File\enrollment_10-27-16.csv")

# join the two csvs with pandas merge
enrollment_table = pd.merge(enrollment, demographics, how='inner', left_on='Alternate ID', right_on='Alternate ID')

# Let's see whats inside the data sets
'''enrollment_table.head()'''
'''enrollment.plot(kind="scatter", x="Entry Date", y="length of stay")'''
'''sns.jointplot(x="length of stay range", y="length of stay", data=enrollment_table)'''

enrollment_table.head()
enrollment_table["length of stay range"].value_counts()
enrollment_table.plot(kind="scatter", x="length of stay", y="Age")
