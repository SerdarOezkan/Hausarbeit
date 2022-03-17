import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_fullfillment(df_fullfillment:pd.DataFrame):
    x = df_fullfillment.index.map(convert_seconds_to_hours)
    y = df_fullfillment["mean"].values
    ci = df_fullfillment["std"].values
    ci_upper = (y + ci)
    ci_upper[ci_upper > 1.] = df_fullfillment.max(axis=1)[ci_upper > 1.]
    ci_lower = (y - ci)
    ci_lower[ci_lower < .0] = df_fullfillment.min(axis=1)[ci_lower < 0.]

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.plot(x, y, zorder=2, color="r")
    ax.fill_between(x, ci_lower, ci_upper, color='b', alpha=.1, zorder=1)
    plt.xlabel("Hours")
    plt.ylabel("Average Fulfillment")
    # plt.ylim(-.05, 1.05)
    plt.show()


def convert_seconds_to_hours(sec: int) -> int:
    """

    # TODO docstring
    :param sec:
    :return:
    """
    return int(sec / 3600)