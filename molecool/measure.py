""" 
measure.py

This module is for which performs measurements

"""
import numpy as np

def calculate_distance(r_a, r_b):
    """
    Calculate the distance between two points.

    Parameters
    ---------- 
    r_a, r_b : np.ndarray
	The coordinates of each point.
    
    Return
    ------
    distance : float
        The distance between the two points.

    Example
    --------
    >>> r1 = nparray([0, 0, 0])
    >>> r2 = nparray([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """
    # This function calculates the distance between two points given as numpy arrays.
    if not isinstance(r_a, np.ndarray) or not isinstance(r_b, np.ndarray):
        raise TypeError("Input are np array not list")

    distance_vector = (r_a - r_b)
    distance = np.linalg.norm(distance_vector)
    return distance

def calculate_angle(r_a, r_b, r_c, degrees = False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    ab = r_b - r_a
    bc = r_b - r_c
    theta = np.arccos(np.dot(ab, bc) / (np.linalg.norm(ab)*np.linalg.norm(bc)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta




