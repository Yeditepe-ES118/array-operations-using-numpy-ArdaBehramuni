import numpy as np

def stat():
    
    data = np.loadtxt("populations.txt", skiprows=1)
    
    hare = data[:,1]
    
    min_year_hare = data[np.argmin(hare),0]

    lynx_avg = np.mean(data[:,2])

    new_data = np.hstack((data, (np.sum(data[:, 1:], axis=1)).reshape(21, 1)))

    new_data[:, 3][new_data[:, 3] < 40000] = 0
    
    return data, hare, min_year_hare, lynx_avg, new_data
    
    
data = np.loadtxt("populations.txt", skiprows=1)
    
hare = data[:,1]

min_year_hare = data[np.argmin(hare),0]

lynx_avg = np.mean(data[:,2])

new_data = np.hstack((data, (np.sum(data[:, 1:], axis=1)).reshape(21, 1)))

new_data[:, 3][new_data[:, 3] < 40000] = 0