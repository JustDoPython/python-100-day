import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

# 3.1 示例
df = pd.DataFrame(dict(time=np.arange(500), value=np.random.randn(500).cumsum()))
sns.relplot(x="time", y="value", kind="line", data=df)

df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
sns.relplot(x="x", y="y", sort=False, kind="line", data=df)

# 3.2 示例
fmri = sns.load_dataset("fmri")
print(fmri)

sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri)

sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", hue="region", style="event", kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", hue="region", style="event", dashes=False, markers=True, kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", hue="event", style="event", kind="line", data=fmri)

sns.relplot(x="timepoint", y="signal", hue="region", units="subject", estimator=None, kind="line", data=fmri.query("event == 'stim'"))

# 3.3 示例
dots = sns.load_dataset("dots").query("align == 'dots'")
print(dots)

sns.relplot(x="time", y="firing_rate", 
            hue="coherence", style="choice", 
            kind="line", data=dots)
			
palette = sns.cubehelix_palette(n_colors=6)  # 数据集中 coherence 变量有6个数值，所以 n_colors=6
sns.relplot(x="time", y="firing_rate", hue="coherence", style="choice", palette=palette, kind="line", data=dots)

from matplotlib.colors import LogNorm
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            hue_norm=LogNorm(),
            kind="line", data=dots)
			
sns.relplot(x="time", y="firing_rate",
            size="coherence", style="choice",
            kind="line", data=dots)
			
sns.relplot(x="time", y="firing_rate",
           hue="coherence", size="choice",
           kind="line", data=dots)
		   
# 3.4 示例
df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)

g.fig.autofmt_xdate()






