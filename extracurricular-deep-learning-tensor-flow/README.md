# TensorFlow

## Installation
There are two options for running TensFlow: Locally via Python or Docker container.

The following steps are required for [getting TensorFlow installed](https://www.tensorflow.org/install).

### Install Python Packages

```bash
# Install virtual environment for Python Package Manager
pip3 install virtualenv

# setup virtual env 
virtualenv udacity-tf

# activate virtual environment for use
source udacity-tf/bin/activate

# Install TensorFlow 
pip3 install tensorflow

# deactivate virtualenv when finish
deactivate
```

### Run TensorFlow Container

Assumption: [Docker](https://docs.docker.com/install/) is already installed.

```bash
# Download latest image
docker pull tensorflow/tensorflow

# Start a Jupyter notebook server 
docker run -it -p 8888:8888 tensorflow/tensorflow
```

## References
* [Tutorials](https://www.tensorflow.org/tutorials)
* [How-To Guides](https://www.tensorflow.org/guide) 
* [Models & Datasets](https://www.tensorflow.org/resources/models-datasets)
