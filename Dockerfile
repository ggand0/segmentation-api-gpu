
FROM nvcr.io/nvidia/pytorch:20.06-py3

WORKDIR /build
COPY . /build

RUN apt-get update && apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-tk git tmux htop tree
    
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
ENV FORCE_CUDA="1"
RUN cd PyTorch-Encoding && \
    python3 setup.py develop

# Avoid ModuleNotFoundError: No module named 'encoding.version'
WORKDIR /app
COPY . /app