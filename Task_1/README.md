# Task 1. Natural Language Processing. Named entity recognition

In this task, we need to train a named entity recognition (NER) model for the identification of mountain names inside the texts. For this purpose you need:  

* Find / create a dataset with labeled mountains.  
* Select the relevant architecture of the model for NER solving.  
* Train / finetune the model.  
* Prepare demo code / notebook of the inference results.  
  
The output for this task should contain:  
  
* Jupyter notebook that explains the process of the dataset creation.  
* Dataset including all artifacts it consists of.  
* Link to model weights.  
* Python script (.py) for model training.  
* Python script (.py) for model inference.  
* Jupyter notebook with demo.  
  
Recommendation:  
  
* Look into possibilities of ChatGPT for dataset generation;  
* Check BERT-based pre-trained models for NER problem;  


## Progress of the work

In our Natural Language Processing project, we have successfully started solving the Named Entity Recognition (NER) task for identifying mountain names in texts. Below is an overview of our current progress and future plans:

### Current Status
Training data preparation: 
Dataset_creation.ipynb
We have completed the preparation of a training dataset where text data is annotated with named entities (mountain names).

* Model Architecture Selection:
Selected the spaCy model architecture to solve the NER problem.

* Model Training: 
model_training.py
Successfully trained the model on the prepared training data and achieved satisfactory performance.

* Demonstration Code:
Demo.ipynb
Developed the main code for model inference and output.

### Future plans
Testing and Validation:
We plan to test the model on new texts to assess its accuracy and readiness for use in real-world conditions.

Optimization and Fine-tuning:
We are considering model optimization and fine-tuning to improve the results.