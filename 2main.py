import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, chi2_contingency
import matplotlib.gridspec as gridspec

# Loading  the dataset
df = pd.read_csv("2data.csv")

# Performing statistical tests
non_suspicious = df[df['Is_Suspicious'] == 0]['Login_Duration_Min']
suspicious = df[df['Is_Suspicious'] == 1]['Login_Duration_Min']
t_stat, t_p = ttest_ind(non_suspicious, suspicious)

device_table = pd.crosstab(df['Device_Type'], df['Is_Suspicious'])
chi2_stat, chi_p, dof, expected = chi2_contingency(device_table)

# Setting up all figure
plt.figure(figsize=(18, 10))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 2])

# -----------------------------------------------
#  Dataset Table (first 10 rows)
# -----------------------------------------------
ax0 = plt.subplot(gs[0, :])
ax0.axis('tight')
ax0.axis('off')
table_data = df.head(10)
table = ax0.table(cellText=table_data.values,
                  colLabels=table_data.columns,
                  cellLoc='center',
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
ax0.set_title("Dataset Preview (Top 10 Rows)", fontsize=14, weight='bold', pad=10)

# -----------------------------------------------
#  T-Test Plot
# -----------------------------------------------
ax1 = plt.subplot(gs[1, 0])
sns.boxplot(ax=ax1, x='Is_Suspicious', y='Login_Duration_Min', data=df)
ax1.set_title("T-Test: Login Duration", fontsize=13, weight='bold')
ax1.set_xlabel("Is Suspicious (0 = No, 1 = Yes)")
ax1.set_ylabel("Login Duration (minutes)")

# -----------------------------------------------
#  Chi-Square Plot
# -----------------------------------------------
ax2 = plt.subplot(gs[1, 1])
sns.countplot(ax=ax2, x='Device_Type', hue='Is_Suspicious', data=df)
ax2.set_title("Chi-Square: Device Type vs Suspicious", fontsize=13, weight='bold')
ax2.set_xlabel("Device Type")
ax2.set_ylabel("Login Count")
ax2.legend(title="Is Suspicious")

# -----------------------------------------------
# Finalizing layout
# -----------------------------------------------
plt.tight_layout()
plt.show()