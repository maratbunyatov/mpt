import numpy as np
from scipy import optimize
import pandas.stats.moments as moments


def cost_func(w, delivery, sigma):
    # print 'w', w
    projected_delivery = np.dot(w, delivery)
    res = projected_delivery + portfolio_stdev(w, sigma)
    # print 'cost + stdev', res
    return res

def portfolio_stdev(w, sigma):
    w = np.asmatrix(w)
    sigma = np.asmatrix(sigma)
    var = w * sigma * w.T
    res = np.sqrt(var[0, 0])
    return res

def MinVarianceAllocation(history):
    num_assets = len(history)

    # compute covariance matrix
    sigma = np.cov(history)

    projected_cost = [moments.ewma(h, halflife=10)[-1] for h in history]

    bounds = tuple((0.001,1) for _ in range(num_assets))

    opt_results = optimize.minimize(cost_func,
                                    x0=np.array([1.0] * num_assets),
                                    constraints=({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}),
                                    bounds=bounds,
                                    tol=np.mean(projected_cost)*0.01,
                                    args=(projected_cost, sigma),
                                    method='SLSQP')

    return opt_results['x'], opt_results['success']

















