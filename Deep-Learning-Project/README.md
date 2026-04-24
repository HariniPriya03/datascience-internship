# DEEP-LEARNING-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: G. HARINI PRIYA

*INTERN ID*: CT04DN652

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## CIFAR-10 Image Classification with PyTorch 

## Project Overview
In this project, I created a simple Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset using PyTorch. CIFAR-10 is a well-known dataset in computer vision, containing 60,000 small color images divided into 10 classes. The goal was to train a model that can correctly identify the category of new images.

`The project shows the full process—from loading data, training the CNN, checking how well it works, to visualizing the results. I built and ran everything using Visual Studio Code (VSCode).`

## About the Dataset
*CIFAR-10 has 10 classes*:

- Airplane

- Automobile

- Bird

- Cat

- Deer

- Dog

- Frog

- Horse

- Ship

- Truck

It has 50,000 training images and 10,000 test images. Each image is a small 32x32 pixel color picture. Since the dataset isn’t too big or complicated, it’s great for learning and testing deep learning models.

## How the Project Works

### Loading and Preparing Data
I used PyTorch’s torchvision to download the dataset automatically. The images are converted to tensors and normalized, which helps the model learn better. The data is divided into batches and shuffled during training.

### The CNN Model
The model has two convolutional layers with ReLU activations and max pooling, followed by three fully connected layers. It’s a simple structure but can still learn useful features from the images.

### Training the Model
Training runs for 5 epochs using cross-entropy loss (good for multi-class classification) and SGD optimizer with a small learning rate and momentum. I track the loss to see how the model improves.

### Saving the Model
After training, the model’s weights are saved to a file so it can be loaded later without retraining.

### Evaluating Performance
I test the model on 10,000 test images and calculate accuracy to see how often the model predicts correctly.

### Visualizations
I include two visualizations:

- A plot of training loss over the epochs to show learning progress.

- A display of some test images with their true labels and the model’s predictions to see how well it works on real examples.

## Using VSCode for Development
I wrote and ran the code in Visual Studio Code (VSCode). The built-in terminal made it easy to run training and testing scripts. VSCode’s Python tools helped with code checking and debugging. Also, Matplotlib charts showed up right inside VSCode, so I didn’t have to leave the editor to see the results.

## Results
- Training loss drops steadily, which means the model is learning.

- Test accuracy reaches about 50%, which is good for a simple CNN trained only for 5 epochs without extra tricks.

- The model predicts many images correctly but sometimes makes mistakes — showing how image classification can be challenging.

## How to Run This Project
- Clone the repo.

- Install PyTorch, torchvision, matplotlib, and numpy.

- Run the Python script from VSCode’s terminal to train the model, evaluate it, and see the visualizations.

- Training time depends on your computer — usually a few minutes on CPU, faster with a GPU.

## Ideas to Improve
To make the model better, you can:

- Train for more epochs.

- Use stronger models like ResNet.

- Add data augmentation to improve learning.

- Try the Adam optimizer for faster training.

- Add dropout and batch normalization for better regularization.

## Conclusion
This project is a simple example of how to build and train a CNN for image classification using PyTorch in VSCode. It covers all the main steps — loading data, training, evaluating, and visualizing — and is a good starting point for learning more about computer vision with deep learning.

## Output 
### Test Images
![Image](https://github.com/user-attachments/assets/eb4ada75-e560-48b9-ad2f-b2016ed7d689)

### Training over loss matplotlib graph
![Image](https://github.com/user-attachments/assets/a39ea550-37b2-474d-a013-86a911c1a6eb)
