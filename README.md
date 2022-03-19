# segmentation-api-gpu

1. Install [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

2. Build docker image
`docker build -t ss-gpu:1.0 .`

3. Run docker image
`docker run --rm -it --ulimit memlock=-1 --ulimit stack=67108864 --gpus=all ss-gpu:1.0`

4. Run inference example
`python main.py`
