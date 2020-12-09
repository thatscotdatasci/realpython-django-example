.PHONY: up build local update-reqs

up:
	@docker-compose up --build

build:
	@docker-compose build

local:
	@. .env; \
	. .env.django.secret; \
	SOCIAL_AUTH_GITHUB_KEY=$$SOCIAL_AUTH_GITHUB_KEY \
	SOCIAL_AUTH_GITHUB_SECRET=$$SOCIAL_AUTH_GITHUB_SECRET \
	python manage.py runserver

update-reqs:
	@pip freeze > requirements.txt
