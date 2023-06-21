![python](https://img.shields.io/badge/python-3.10-blue)
# Sentiment Analysis API

This is a API for predicting sentiment analysis of texts.
It was build with [Django-Rest-Framework](https://www.django-rest-framework.org/) and is based on Natural Language Processing. It uses pre-trained [SetFit model](https://huggingface.co/StatsGary/setfit-ft-sentinent-eval) for sentiment analysis.

<img src="https://raw.githubusercontent.com/huggingface/setfit/main/assets/setfit.png">
<p align="center">
    source: https://huggingface.co/setfitt
</p>


# StatsGary/setfit-ft-sentinent-eval

This is a [SetFit model](https://github.com/huggingface/setfit) that can be used for text classification. The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.


## Get Started With Sentiment Analysis API
> Use a virtual env
* Clone repo : ```$ git clone https://github.com/remon-rakibul/sentiment-analysis-api```
* ```$ cd sentiment-analysis-api```
* Create a virtualenv: ```$ mkvirtualenv env``` or ```$ python -m venv env```
* Activate env : ```$ workon env``` or ```$ source env/bin/activate```

**Install dependencies** 
```
$ pip install -r requirements.txt
```

**Run project locally**
```
$ python manage.py runserver
```

## API Endpoints

> **health**

  ![alt postman screenshot](https://github.com/remon-rakibul/sentiment-analysis-api/blob/main/example/health.png?raw=true)

  A GET request to make sure everything is working properly. 

> **analyze**

  ![alt postman screenshot](https://github.com/remon-rakibul/sentiment-analysis-api/blob/main/example/analyze.png?raw=true)

  Takes a sentence through POST request and runs sentiment analysis model to predict sentiment. 

  The input text should be inside a "text" key in JSON format.

## Postman API Collection

  Get postman collection for this project.

  [Sentiment Model API](https://github.com/remon-rakibul/sentiment-analysis-api/blob/main/Sentiment-Model-API.postman_collection.json)

  ![alt postman screenshot](https://github.com/remon-rakibul/sentiment-analysis-api/blob/main/example/collection.png?raw=true)