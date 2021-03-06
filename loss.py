import numpy as np


def binary_cross_entropy(self, predicted, y, lambda_=0.0):

    m = y.shape[0]
    #print(predicted.shape)
    #print(y.shape)
    weights_mats = [layer.weights for layer in self.layers if layer.trainable]
    reg = 0
    for weight_mat in weights_mats:
        reg += np.sum(np.square(weight_mat[:, 1:]))
    reg *= lambda_ / (2 * m)

    loss = (-1 / m) * np.sum((np.log(predicted + 10**-15) * y) +
                             np.log(1 - predicted + 10**-15) * (1 - y))
    return loss + reg


def getLoss(loss):
    if(loss == 'binary_cross_entropy'):
        return binary_cross_entropy
