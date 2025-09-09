import importlib.resources as imprsrc
import pickle

import numpy as np


class cosmopower_NN():
    def __init__(self):
        with imprsrc.files("cosmopower_slim").joinpath(
            "trained_models", "CP_paper", "PK", "PKLIN_NN.pkl"
        ).open('rb') as f:
            (self.W, self.b, self.alphas, self.betas,
             self.parameters_mean, self.parameters_std,
             self.features_mean, self.features_std,
             self.n_parameters, self.parameters,
             self.n_modes, self.modes,
             self.n_hidden, self.n_layers, self.architecture) = pickle.load(f)

        with imprsrc.files("cosmopower_slim").joinpath(
            "trained_models", "CP_paper", "PK", "k_modes.txt"
        ).open() as f:
            self._log10k = np.log10(np.loadtxt(f))

    def dict_to_ordered_arr_np(self, input_dict):
        """Sort input parameters

        Parameters:
            input_dict (dict [numpy.ndarray]):
                input dict of (arrays of) parameters to be sorted

        Returns:
            numpy.ndarray:
                parameters sorted according to desired order
        """
        if self.parameters is not None:
            return np.stack([input_dict[k] for k in self.parameters], axis=1)
        else:
            return np.stack([input_dict[k] for k in input_dict], axis=1)

    def forward_pass_np(self, x):
        r"""Forward pass through the network to predict the output,
        fully implemented in Numpy

        Parameters:
            x (numpy.ndarray): array of input parameters

        Returns:
          numpy.ndarray: output predictions
        """
        last_layer = (x - self.parameters_mean) / self.parameters_std
        for i in range(self.n_layers - 1):
            # linear network operation
            act = np.dot(last_layer, self.W[i]) + self.b[i]

            g = (1.0 + np.exp(-self.alphas[i] * act))

            # pass through activation function
            last_layer = act * (self.betas[i] + (1.0 - self.betas[i]) / g)

        # final (linear) layer -> (standardised) predictions
        last_layer = np.dot(last_layer, self.W[-1]) + self.b[-1]

        return last_layer * self.features_std + self.features_mean

    def predictions_np(self, parameters_dict):
        r"""
        Predictions given input parameters collected in a dict.
        Fully implemented in Numpy. Calls ``forward_pass_np``
        after ordering the input parameter dict

        Parameters:
            parameters_dict (dict [numpy.ndarray]):
                dictionary of (arrays of) parameters

        Returns:
            numpy.ndarray:
                output predictions
        """
        parameters_arr = self.dict_to_ordered_arr_np(parameters_dict)
        return self.forward_pass_np(parameters_arr)

    def ten_to_predictions_np(self, parameters_dict):
        """10^predictions given input parameters collected in a dict.
        Fully implemented in Numpy. It raises 10 to the output
        from ``forward_pass_np``

        Parameters:
            parameters_dict (dict [numpy.ndarray]):
                dictionary of (arrays of) parameters

        Returns:
            numpy.ndarray:
                10^output predictions
        """
        return 10.**self.predictions_np(parameters_dict)
