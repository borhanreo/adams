#!/usr/bin/env bash
python3.6 main.py --prototxt $PWD/model/dnn_deploy.prototxt --model $PWD/model/dnn_iter_7.caffemodel --labels $PWD/model/custom_words.txt --source webcam