import numpy as np
from data import X, y, X_, y_

class NaiveBayes:
    def __init__(self, X, y):
        self.y = y
        self.X = X
        
    def predict(self, x):
        labels np.unique(self.y)
        probs = [self.pr_y_given_x(y,x) for y in labels]
        return np.argmax(probs)
              
                
    
    
    def pr_y_given_x(self, y, x):
        loggies = np.zeros(x.shape)
        for i, xi in enumerate(x):
            loggies[i] +=np.log(self.pr_xi_given_y(xi, i, y))
        return np.sum(loggies) + np.log(self.pr_y(y))
            
    
    def pr_xi_given_y(self, xi, i, y):
        filtered = self.x[self.y == y]
        count = np.sum(filtered[:, i] == xi)
        pr = count /filtered.shape[0]
        return pr if pr > 0 else 2**(-32)
        
    def pr_y(self, y):
        return np.sum(self.y == y) / self.y.shape[0]

model = NaiveBayes(X, y)
if __name__ == '__main__':
    preds = [model.predict(x) for x in X_]
    accuracy = np.sum(preds == y_) / y_.shape[0]
    print(f'Accuracy: {accuracy}')
