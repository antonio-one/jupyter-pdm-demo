from matplotlib import pyplot as plt


def set_plot_opts():
    plt.style.use("seaborn-darkgrid")
    plt.rcParams["figure.figsize"] = (16, 9)
    plt.rcParams["figure.max_open_warning"] = 40
