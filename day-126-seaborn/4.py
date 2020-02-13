import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

# 4.1 示例
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", hue="smoker",
            col="time", data=tips)
			
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", estimator=None, data=fmri)
			
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=3, aspect=.75, linewidth=2.5,
            kind="line", data=fmri.query("region == 'frontal'"))