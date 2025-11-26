"""
Monte Carlo sampling for Fuzzy Gap Statistic
"""

import numpy as np


class MonteCarloSampling:
    """
    Monte Carlo sampling class
    """

    def __init__(self):
        """Initialize Monte Carlo sampler"""
        pass

    def sample_uniform(self, data: np.ndarray) -> np.ndarray:
        """
        Sample uniformly from the bounding box of the data

        Args:
            data: Original data (n_samples, n_features)

        Returns:
            sampled_data: Sampled data with same shape
        """
        n_samples, n_features = data.shape

        # Get min and max for each feature
        mins = np.min(data, axis=0)
        maxs = np.max(data, axis=0)

        # Sample uniformly
        sampled_data = np.random.uniform(
            low=mins,
            high=maxs,
            size=(n_samples, n_features)
        )

        return sampled_data