def facies(max_depth):
    """
    
    """

    facies_data = [
        {'name': 'Terrestrial', 'type': 'land', 'width': 1, 'min': 1, 'max': 2},
    
        {'name': 'Grainstone', 'type': 'uniform', 'min': -0.01, 'max': max_depth / 15, 'width': 0.8},
        {'name': 'Packstone', 'type': 'uniform', 'min': max_depth / 15, 'max': max_depth / 10, 'width': 0.6},
        {'name': 'Wackestone', 'type': 'uniform', 'min': max_depth / 10, 'max': max_depth / 6.5, 'width': 0.4},
        {'name': 'Mudstone', 'type': 'uniform', 'min': max_depth / 6.5, 'max': max_depth / 4.5, 'width': 0.3},
        {'name': 'Shallow Marine', 'type': 'uniform', 'min': max_depth / 4.5, 'max': max_depth / 3.5, 'width': 0.3},
    
        # Widened blue facies
        {'name': 'Intermediate Marine', 'type': 'uniform', 'min': max_depth / 3.5, 'max': max_depth / 2.0, 'width': 0.2},
        {'name': 'Deep Marine', 'type': 'uniform', 'min': max_depth / 2.0, 'max': max_depth, 'width': 0.2},
    ]
    return facies_data
