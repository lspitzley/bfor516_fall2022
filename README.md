# BFOR 516 - Advanced Data Analytics
Code and data for BFOR 516 Fall 2022




## Definitions

**Algorithm** - In mathematics and computer science, an algorithm is a 
finite sequence of rigorous instructions, typically used to solve a 
class of specific problems or to perform a computation. 
[(Wikipedia)](https://en.wikipedia.org/wiki/Algorithm). 

Examples:
Multi-layer Perceptron, Naive Bayes, Stochastic Gradient Descent

**Model** - "Machine learning models are output by algorithms and are 
comprised of model data and a prediction algorithm." 
[(Article)](https://machinelearningmastery.com/difference-between-algorithm-and-model-in-machine-learning/).
You can think of the model as a map between the predictors and an
outcome. 

*Other Names: estimator (sklearn terminology)*

**Predictor** - A predictor is data that may be related to an outcome. 

*Other names: attribute, column, feature, independent variable*. 

**Parameter (hyperparamter)** - Before you train a model, you must specify
parameters that affect how the model is fit. When creating a model with 
`sklearn`, the parameters are set before training and affect how the 
algorithm learns. Generally, these are known as *hyperparamters*. 

Examples: Maximum depth in a decision tree or hidden layers in a 
neural network.

**Parameter (model)** - These are the values that are set and updated
*inside* a model. Example: In a logistic regression, coefficients are 
paramters that are learned during the fitting process. 
[(Guide explaining the difference between hyperparameters and parameters)](https://machinelearningmastery.com/difference-between-algorithm-and-model-in-machine-learning/).

