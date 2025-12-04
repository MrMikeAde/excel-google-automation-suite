import matplotlib.pyplot as plt

def plot_column(df, column, output_path):
    plt.figure()
    df[column].plot(kind='bar')
    plt.savefig(output_path)
    plt.close()
