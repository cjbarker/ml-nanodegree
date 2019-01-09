# Predicting Boston Housing Prices

## The Problem
The Boston housing market is highly competitive, and you want to be the best real estate agent in the area. To compete with your peers, you decide to leverage a few basic machine learning concepts to assist you and a client with finding the best selling price for their home. Luckily, you’ve come across the Boston Housing dataset which contains aggregated data on various features for houses in Greater Boston communities, including the median value of homes for each of those areas. Your task is to build an optimal model based on a statistical analysis with the tools available. This model will then be used to estimate the best selling price for your clients' homes.

Project details are hosted on Udacity's Machine-Learning Projects:
[https://github.com/udacity/machine-learning/tree/master/projects/boston_housing](https://github.com/udacity/machine-learning/tree/master/projects/boston_housing)

Project Specifications including the reviewer's rubric can be found on Udacity's [Predicting Boston housing
Prices](https://review.udacity.com/#!/rubrics/103/view).

## Setup
Install necessary library dependencies first.

```bash
pip3 install -r requirements.txt
```

## Run via Jupyter Notebook
```bash
jupyter notebook boston_housing.ipynb
```
## Data

The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing).

**Features**
1.  `RM`: average number of rooms per dwelling
2. `LSTAT`: percentage of population considered lower status
3. `PTRATIO`: pupil-teacher ratio by town

**Target Variable**
4. `MEDV`: median value of owner-occupied homes

