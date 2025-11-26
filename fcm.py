"""
Fuzzy C-Means clustering implementation
"""

import numpy as np


class FuzzyCMeans:
    """
    Fuzzy C-Means clustering algorithm
    """

    def __init__(self, n_clusters: int = 3, m: float = 2.0,
                 max_iter: int = 100, error: float = 1e-5):
        """
        Initialize FCM

        Args:
            n_clusters: Number of clusters
            m: Fuzziness parameter (default 2.0)
            max_iter: Maximum iterations
            error: Convergence threshold
        """
        self.n_clusters = n_clusters
        self.m = m
        self.max_iter = max_iter
        self.error = error

        self.centers = None
        self.u = None  # Membership matrix
        self.objective_value = None

    def _initialize_membership(self, n_samples: int) -> np.ndarray:
        """
        Initialize membership matrix randomly
        """
        u = np.random.rand(n_samples, self.n_clusters)
        u = u / np.sum(u, axis=1, keepdims=True)
        return u

    def _update_centers(self, X: np.ndarray, u: np.ndarray) -> np.ndarray:
        """
        Update cluster centers
        """
        um = u ** self.m
        centers = (um.T @ X) / np.sum(um.T, axis=1, keepdims=True)
        return centers

    def _update_membership(self, X: np.ndarray, centers: np.ndarray) -> np.ndarray:
        """
        Update membership matrix
        """
        n_samples = X.shape[0]
        u = np.zeros((n_samples, self.n_clusters))

        for i in range(n_samples):
            for j in range(self.n_clusters):
                distances = np.linalg.norm(X[i] - centers, axis=1)
                distances[distances == 0] = 1e-10  # Avoid division by zero

                u[i, j] = 1.0 / np.sum((distances[j] / distances) ** (2.0 / (self.m - 1)))

        return u

    def _calculate_objective(self, X: np.ndarray, u: np.ndarray,
                            centers: np.ndarray) -> float:
        """
        Calculate objective function value
        """
        um = u ** self.m
        distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
        obj = np.sum(um * (distances ** 2))
        return obj

    def fit(self, X: np.ndarray):
        """
        Fit FCM to data

        Args:
            X: Input data (n_samples, n_features)
        """
        n_samples, n_features = X.shape

        # Initialize membership matrix
        self.u = self._initialize_membership(n_samples)

        for iteration in range(self.max_iter):
            u_old = self.u.copy()

            # Update centers
            self.centers = self._update_centers(X, self.u)

            # Update membership
            self.u = self._update_membership(X, self.centers)

            # Check convergence
            if np.linalg.norm(self.u - u_old) < self.error:
                break

        # Calculate final objective value
        self.objective_value = self._calculate_objective(X, self.u, self.centers)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict cluster labels

        Args:
            X: Input data

        Returns:
            labels: Cluster labels
        """
        u = self._update_membership(X, self.centers)
        labels = np.argmax(u, axis=1)
        return labels