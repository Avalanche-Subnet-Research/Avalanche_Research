import matplotlib.pyplot as plt

def plot_results(data):
    # Check if data is a list of dictionaries
    if isinstance(data, list) and all(isinstance(d, dict) for d in data):
        for d in data:
            for key, values in d.items():
                plt.plot(values, label=key)
        plt.legend()
    else:
        # Handle the case where data is a list of lists
        for idx, series in enumerate(data):
            plt.plot(series, label=f'Series {idx+1}')
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Simulation Results')
    plt.legend()
    plt.show()
