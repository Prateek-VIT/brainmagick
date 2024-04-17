# Use the official PyTorch image as the base image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git gcc wget

# Add the VOLUME mount to the docker file
RUN git clone https://github.com/Prateek-VIT/brainmagick.git

# Set the working directory to the cloned repository
WORKDIR /app/brainmagick
RUN git checkout recurrence

# Install Miniconda
RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
ENV PATH="/root/miniconda3/bin:$PATH"
RUN rm -rf ~/miniconda3/miniconda.sh

# Create a new conda environment and install required dependencies
RUN conda create -n bm ipython python=3.8 -y
RUN echo "source activate bm" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# Install requirements
RUN /bin/bash -c "source activate bm && pip install -U -r requirements.txt"
RUN /bin/bash -c "source activate bm && pip install -e ."

# Create 'data' directory and 'gwilliams2022' subdirectory
RUN mkdir -p /app/brainmagick/data/gwilliams2022

# Set the default command to run when the container starts
CMD [ "/bin/bash"]

# After building this file, make a folder called brainmagick