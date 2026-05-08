#!/bin/sh

# start the enroot container on the cluster
IMAGE=/netscratch/enroot/nvcr.io_nvidia_tensorflow_22.12-tf2-py3.sqsh

srun -K \
  --job-name="md_bleurt" \
  --container-mounts=/netscratch:/netscratch,/ds:/ds,$HOME:$HOME \
  --container-workdir="$(pwd)" \
  --container-image=$IMAGE \
  --ntasks=1 \
  --nodes=1 \
  --gpus=1 \
  --partition=L40S \
  --immediate=60 \
  --time=04:00:00 \
  --mem=128GB \
  --pty /bin/bash
