import pandas as pd
import matplotlib
matplotlib.use('Agg')
import os
import matplotlib.pyplot as plt


def signal_step_graph(data, col, x_col, filepath, filename):
    plt.rcParams['axes.xmargin'] = 0

    df = pd.DataFrame(data, columns=col)
    df.fillna(0, inplace=True)
    df.set_index(x_col, drop=True, inplace=True)
    data_col = df.columns.tolist()

    # 그래프 코드
    colors = ['rosybrown', 'lightcoral', 'darkgreen', 'lime', 'lightseagreen', 'teal', 'aqua', 'cadetblue', 'steelblue', 'slategray', 'purple', 'magenta', 'crimson', 'navy', 'lightsteelblue',
              'salmon', 'peru', 'saddlebrown', 'sandybrown', 'red', 'olive', 'yellow', 'darkred', 'deeppink', 'indigo', 'mediumorchid', 'darkorange', 'tan', 'dodgerblue', 'cyan', 'forestgreen']
    fig = plt.figure(figsize=(24, 24))
    axs = fig.add_gridspec(len(data_col), hspace=0.1).subplots(sharex=True, sharey=False)

    for i in range(len(data_col)):
        sig_name = data_col[i].replace('In: ', '').replace('Out: ', '')
        axs[i].step(df.index.values, df[data_col[i]], c=colors[i], label=sig_name, where='post', linewidth=3.0)
        axs[i].set_ylabel(sig_name)
        min_val = df[data_col[i]].min()
        if min_val < 0:
            axs[i].set_ylim(bottom=min_val-1)
        else:
            axs[i].set_ylim(bottom=0)

    # Hide x labels and tick labels for all but bottom plot
    for ax in axs:
        ax.legend(loc='upper right')
        ax.label_outer()

    plt.locator_params(axis='x', nbins=5)
    plt.xlabel('Time[sec]')

    plt.savefig('{}/{}.png'.format(filepath, filename))
