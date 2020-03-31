Training folder contain everything for training model.  

Please take a look at: for more detail:https://cs230.stanford.edu/blog/tips/?fbclid=IwAR1TP-vkdVDTTFg5F6ne1Dofyyz_2L-xQ9fTmctKCw8xUosdHkeTnIJKwEM

Here is each file or directory’s purpose:

- data/: will contain all the data of the project (generally not stored on github), with an explicit train/dev/test split
experiments: contains the different experiments (will be explained in the following section)
- model/: module defining the model and functions used in train or eval. Different for our PyTorch and TensorFlow examples
- build_dataset.py: creates or transforms the dataset, build the split into train/dev/test
- train.py: train the model on the input data, and evaluate each epoch on the dev set
- search_hyperparams.py: run train.py multiple times with different hyperparameters
- synthesize_results.py: explore different experiments in a directory and display a nice table of the results
evaluate.py: evaluate the model on the test set (should be run once at the end of your project)




