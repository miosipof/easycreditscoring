# A Simple Open-Source Credit Scoring System

_easycreditscoring_ provides a systematic - though simplified - approach to the credit scoring problem. We base on the publicly available [Kaggle dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/). 

To deal with the credit scoring problem we develop a simple Python package that combines data transformation process with the application of various machine learning models.
We will skip the exploratory data analysis (EDA) since the dataset-specific insights are publicly available.

## Contents

1. Workflow
2. Library structure
3. Examples

## 1. Workflow

We start with uploading the dataset in CSV format. Brief analysis shows a large number of missing values and outliers that are to be dealt with.

The library implements standard data cleaning and preprocessing techniques: non-numerical values cleanup, categorical one-hot encoding, outliers elimination based on z-score, missing values imputation with kNN (k-Nearest-Neighbours) algorithm.

After the dataset has been preprocessed, we apply a set of classic machine learning models to predict credit score and evaluate their efficiency: well-interpretable algorithms (logistic regression, decision tree, Bayes) and less interpretable (Random Forest, gradient boosting, neural network). All these models are implemented via abstract classes that allow their usage with a simple interface. 

In addition, the library contains an ensemble method to combine any of the implemented models.

To evaluate results, we use a standard confusion matrix to calculate accuracy and other metrics and check ROC-AUC metrics. For the neural network model we provide an advanced interface that implements a custom loss function based on unit economy.

Note: the library can be used to get first estimations and to set baselines. Further analysis, both during the dataset exploration and model fine-tuning, is not in the scope of our work, although our system shows good results on Kaggle dataset.


## 2. Library structure


```
├── setup.py
├── src
│   ├── data_cleaning.py	# Data cleaning tools
│   └── modelzoo.py.py   	# ML models implementation
│   └── ensembling.py		# Ensembling tools
│   └── economy.py		# Unit economy implementation
├── LICENSE.txt              	 
├── requirements.txt         	# List of dependencies
└── README.md                	# This README file
```

## 3. Examples

To install the library, use the following shell command: 

`% pip install easycreditscoring
`

Import works as follows:

`import easycreditscoring
`

`from easycreditscoring import DataCleaner, ModelPipeLine, Ensembling, UnitEconomy
`

To see an example of usage with Kaggle scoring dataset, see [this Colab notebook](https://colab.research.google.com/drive/1cM4GVzCSvxSBwFwlyY7UFk0gkyVJRksr?usp=sharing).