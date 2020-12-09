.PHONY: up build local

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