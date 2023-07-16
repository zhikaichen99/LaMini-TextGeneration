# LaMini-TextGeneration
Deploying a HuggingFace LLM on Amazon SageMaker. Building a Streamlit application for it and deploying it on an Amazon EC2 Instance

This repo contains the source code for my article published on Medium. You can follow the article for a step-by-step procedure on how to deploy an LLM, use it in a Streamlit application, and deploy that application on an EC2 Instance.

https://medium.com/@zhikaichen1999/deploying-a-hugging-face-language-model-on-amazon-sagemaker-8e28020a7ced

## Project Motivation
The motivation for this project was to gain experience deploying LLMs in SageMaker and learning how to build working applications that can be deployed for anyone to use.

## Repository Structure and File Description

```markdown
├── LaMini-Streamlit.ipynb                        # Notebook that needs to be run in SageMaker
├── README.md                                     # Readme file
├── app.py                                        # Streamlit application file
├── requirements.txt                              # requirements file           

```

## Requirements
You will need an AWS account if you want to follow along with the article.

## Installations
The packages and libraries required for this project are in the `requirements.txt` file.

## How To Interact With The Project
1. Close the repository to your local machine using the following command:
```
git clone https://github.com/zhikaichen99/LaMini-TextGeneration.git
```
3. Upload the Juyter notebook onto your SageMaker Notebook instance.
4. Alternatively, you can do every step yourself by following the Medium article


