![python](https://img.shields.io/badge/python-3.10-blue)
# Sentiment Analysis API

This is a API for predicting sentiment analysis of texts.
It was build with [Django-Rest-Framework](https://www.django-rest-framework.org/) and is based on Natural Language Processing. It uses pre-trained NLP model from [here](https://huggingface.co/StatsGary/setfit-ft-sentinent-eval) for text analysis.

## Get Started
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

> http://127.0.0.1:8000/api/v1/health

  ![alt postman screenshot](https://github.com/remon-rakibul/sentiment-analysis-api/blob/main/example/health.png?raw=true)

  A GET request to make sure everything is working properly. 

> http://127.0.0.1:8000/api/v1/analyze

  ![alt postman screenshot](https://github.com/remon-rakibul/sentiment-analysis-api]/blob/main/example/analyze.png?raw=true)

  Takes a sentence through POST request and runs sentiment analysis model to predict sentiment. 

  The input text should be inside a "text" key in JSON format.