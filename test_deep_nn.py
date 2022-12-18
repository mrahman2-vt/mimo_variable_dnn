import unittest
import deep_nn
import numpy as np

class TestDeepNN(unittest.TestCase):

    @unittest.skip("Need to change data format")
    def test_feed_forward(self):
        params = {}
        params["A"] = np.ones((10, 5), dtype=float)
        params["W"] = 0.2 * np.ones((8, 10), dtype=float)
        params["b"] = 0.2 * np.ones((8, 1), dtype=float)
        Z_exp = 2.2 * np.ones((8, 5), dtype=float)
        params["Z"] = deep_nn.feed_forward(params["W"], params["b"], params["A"])
        self.assertTrue(np.allclose(params["Z"], Z_exp))

    @unittest.skip("Need to change data format")
    def test_full_feed_forward(self):
        layers_dim = [2, 5, 3]
        params = {}
        params["W1"] = 0.1 * np.ones((5, 2))
        params["b1"] = 0.1 * np.ones((5, 1))
        params["W2"] = 0.1 * np.ones((3, 5))
        params["b2"] = 0.1 * np.ones((3, 1))
        X = np.array([[0.3, 0.4, 0.1, -0.9, -0.2],
                      [-0.5, 0.1, 0.2, -0.6, 0.1]])
        Y_exp = np.array( [[0.56463498, 0.56677739, 0.56616644, 0.56063789, 0.56494168],
                           [0.56463498, 0.56677739, 0.56616644, 0.56063789, 0.56494168],
                           [0.56463498, 0.56677739, 0.56616644, 0.56063789, 0.56494168]] )
        params = deep_nn.full_feed_forward(layers_dim, params, X)
        layers_dim = [2, 5, 4]
        params = {}
        params["W1"] = 0.1 * np.ones((5, 2))
        params["b1"] = 0.1 * np.ones((5, 1))
        params["W2"] = 0.1 * np.ones((4, 5))
        params["b2"] = 0.1 * np.ones((4, 1))
        params = deep_nn.full_feed_forward(layers_dim, params, X)
        self.assertEqual(params["A2"].shape[0], 4)
        self.assertEqual(params["A2"].shape[1], 5)

    @unittest.skip("Need to change data format")
    def test_cost_function(self):
        Y = 2 * np.ones((2, 3))
        Y_hat = np.zeros((2, 3))
        exp_cost = 4
        cost = deep_nn.cost_function(Y_hat, Y)
        self.assertEqual(cost, exp_cost)

    @unittest.skip("Need to change data format")
    def test_sigmoid_backward(self):
        params = {}
        params["Z"] = 0
        dAdZ = deep_nn.sigmoid_backward(params["Z"])

    @unittest.skip("Need to change data format")
    def test_full_feed_backward(self):
        A = np.ones((2, 2))
        Z = np.ones((2, 2))
        dA, db = deep_nn.full_feed_backward(A, Z)
        print(dA)
        print()
        print(db)

    def test_init_parameters(self):
        layers_dim = [3, 3, 2]
        params = deep_nn.init_parameters(layers_dim)
    
    def test_compute_loss(self):
        Y = np.ones((2, 2))
        Y_hat = 0.5 * np.ones((2, 2))
        cost = deep_nn.compute_cost(Y, Y_hat)

    def test_full_forward_prop(self):
        m = 10
        n = 3
        layers_dim = [n, 4, 2]
        X = np.ones((n, m))
        Y = np.ones((2, 2))
        params = deep_nn.init_parameters(layers_dim)
        Y_hat, caches = deep_nn.full_forward_prop(X, Y, params, layers_dim)

    def test_train_model(self):
        m = 10
        n = 3
        layers_dim = [n, 4, 2]
        X = np.ones((n, m))
        Y = np.ones((2, 2))
        params = deep_nn.init_parameters(layers_dim)
        deep_nn.train_model(X, Y, params, layers_dim)

if __name__ == '__main__':
    unittest.main()