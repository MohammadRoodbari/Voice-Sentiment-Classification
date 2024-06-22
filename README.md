# Voice-Sentiment-Classification

## Overview

Voice-Sentiment-Classification is a project that converts Persian voice inputs to text using the Whisper speech recognition model and classifies the sentiment of the text using a fine-tuned ParsBERT model. The ParsBERT model has been pruned and converted to ONNX format for optimized performance. The entire system is deployed using FastAPI and Docker for efficient and scalable deployment.

## Table of Contents

- [Features](#features)
- [Data](#data)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)


## Features

- Converts persian voice input to text using Whisper speech recognition model.
- Classifies sentiment of text using a fine-tuned ParsBERT model.
- Optimized ParsBERT model in ONNX format for efficient inference.
- RESTful API using FastAPI.
- Dockerized for easy deployment.

## Data

[snappfood-sentiment-analysis](https://www.kaggle.com/datasets/soheiltehranipour/snappfood-persian-sentiment-analysis): a Persian sentiment analysis dataset

## Architecture

1. **[ParsBert](https://github.com/hooshvare/parsbert)** : Transformer-based Model for Persian Language Understanding.
2. **[Whisper](https://github.com/hezarai/hezar)**: Whisper model converts voice input to text for persian language .


## Setup and Installation

### Clone the Repository

```bash
git https://github.com/MohammadRoodbari/Voice-Sentiment-Classification.git
```
```bash
cd Voice-Sentiment-Classification
```

## Usage
To start the FastAPI server
```bash
cd app
```
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```
### Docker Deployment
To build and run the Docker container, follow these steps:

```bash
docker build -t Voice-Sentiment-Classification
```
```bash
docker run -d -p 8000:8000 Voice-Sentiment-Classification
```
