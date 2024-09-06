from scipy.signal import find_peaks
from matplotlib import pyplot as plt
import numpy as np


"""
Geometric functions
"""


def find_local_minimum(arr, range_acceptability):
    """
    Finds a local minimum within a range of acceptability
    """
    output_list = []
    high_range, low_range = range_acceptability
    peaks, _ = find_peaks(-arr)
    for peak in peaks:
        if low_range < arr[peak] < high_range:
            output_list.append(peak)
    return output_list, arr[output_list]


def euclidean_distance(a, b):
    """
    Returns the distance in a 2d euclidean space between a and b
    """
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def angle_between(u, v):
    """
    Retrieves the angle between u and v
    using the definition of cross product.
    """

    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    norm_cross = np.linalg.norm(np.cross(u, v))
    
    # clipping between -1 and 1
    sin_theta = np.clip(norm_cross / (norm_u * norm_v), -1.0, 1.0) 

    return np.degrees(np.arcsin(sin_theta))


"""
Helper functions
"""


def retrieve_matrix(coordinates_to_track, point, filter=None):
    """
    Returns a matrix of coordinates extracted from the video
    """

    if not filter:
        filter = range(len(coordinates_to_track[point]['x']))
    
    return (
        np.matrix([
            list(np.array(coordinates_to_track[point]['x'])[filter]),
            list(1 - np.array(coordinates_to_track[point]['y'])[filter])
        ]).transpose()   
    )


"""
Plotting functions
"""


def impact_points_plot(mid_foot_x, idx_impact, mid_foot_at_impact):
    """
    Plots impact points
    """
    plt.figure(figsize=(10, 4))
    plt.plot(mid_foot_x, color='lightblue') 
    plt.axhline(y=min(mid_foot_x), color='#FF69B4', linestyle='-')      # Pink line
    plt.axhline(y=min(mid_foot_x) - 0.05, color='#FF69B4', linestyle='--')  # Violet-pink line
    plt.axhline(y=min(mid_foot_x) + 0.05, color='#FF69B4', linestyle='--')  # Light pink line
    plt.plot(idx_impact, mid_foot_at_impact, 'o')
    plt.show()


def distribution_plot(arr, title, nbins=9):
    """
    Abstract distribution plot
    """
    plt.figure(figsize=(10, 4))
    plt.hist(arr, bins=nbins, color='lightpink', edgecolor='white')  
    plt.axvline(x=np.median(arr), color='red', linestyle='--')  
    plt.title(title, fontsize=12)
    plt.xlabel("Values", fontsize=10)
    plt.ylabel("Frequency", fontsize=10)
    plt.show()


def overstride_plot(displacement_foot_hip):
    """
    Plots the distribution of overstride
    """
    distribution_plot(displacement_foot_hip,
                      "Distribution of displacements / overstrides (in cm)",
                      nbins=9)


def angle_plot(angles, title):
    """
    Plots the distribution of overstride
    """
    distribution_plot(angles,
                      title,
                      nbins=9)
