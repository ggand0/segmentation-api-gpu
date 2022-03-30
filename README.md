# segmentation-api-gpu

1. Install [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

2. Cloen this repo including submodules
`git clone git@github.com:ggand0/segmentation-api-gpu.git --recursive`

3. Build docker image
`docker build -t ss-gpu:1.0 .`

4. Run docker image
`docker run --rm -it --ulimit memlock=-1 --ulimit stack=67108864 --gpus=all ss-gpu:1.0`

5. Run inference example
`python main.py`
