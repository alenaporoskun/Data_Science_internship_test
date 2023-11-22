## Task 2. Computer vision. Sentinel-2 image matching  
  
In this task, you will work on the algorithm (or model) for matching satellite images. For the
dataset creation, you can download Sentinel-2 images from the official source [here](https://dataspace.copernicus.eu/browser/) or use our
dataset from [Kaggle](https://www.kaggle.com/datasets/isaienkov/deforestation-in-ukraine). Your algorithm should work with images from different seasons. For this
purpose you need:  
  
* Prepare a dataset for keypoints detection and image matching (in case of using the ML approach).  
* Build / train the algorithm.  
* Prepare demo code / notebook of the inference results  
  
The output for this task should contain:  
  
* Jupyter notebook that explains the process of the dataset creation.  
* Link to the dataset (Google Drive, etc.).  
* Link to model weights.  
* Python script (.py) for model training or algorithm creation.  
* Python script (.py) for model inference.  
* Jupyter notebook with demo.  


## Progress of the work  

###  Demonstration Code (Demo.ipynb)

1. Processing Each Image in a Folder  
  
* Reading images from the folder 'C:/Users/Admin/Test_task/Task_2/data/new'.  
* Initialization of the SIFT detector.  
* Viewing and processing each image separately.  
* Finding key points and their descriptors using SIFT.  
* Visualization of key points on the image.  
  
2. Comparison of each Image Pair  
  
* Creates all possible image pairs in a folder.  
* Initializing the SIFT detector.  
* Comparing each pair of images to find close matches.  
* Selecting "good" matches using distance relationships.  
* Visualize image pairs with "good" matches and output the results to Jupyter Notebook.  