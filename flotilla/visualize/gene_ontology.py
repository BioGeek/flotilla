import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


MACHINE_EPSILON = np.finfo(float).eps

def plot_go_enrichment(x_col='bonferonni_corrected_p_value', data=None,
                       ax=None, max_categories=10,
                       **kwargs):
    data = data.sort(subset=[x_col], ascending=True)
    data[x_col] = data[x_col].replace(0, np.nan)
    vmin = max(data[x_col].dropna().min(), MACHINE_EPSILON)
    if np.isnan(vmin):
        vmin = 1e-25
    data.loc[:, x_col] = data[x_col].fillna(vmin * .9)
    if data.shape[0] > max_categories:
        data = data.iloc[max_categories:, :]
    if ax is None:
        ax = plt.gca()

    bottom = np.arange(data.shape[0])
    width = -np.log10(data[x_col])
    ax.barh(bottom, width, **kwargs)
    xticks = list(sorted(list(set(int(x) for x in ax.get_xticks()))))
    ax.set(yticks=bottom + 0.4, yticklabels=data.go_name, xlabel='$-\log_{10}(q)$',
           ylim=(0, bottom.max() + 1))
    sns.despine()
    #     fig.tight_layout()
    return ax