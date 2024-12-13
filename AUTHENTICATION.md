# API Authentication Guide

## Overview
This API uses token-based authentication to secure endpoints. Each user is issued a unique token upon login, which must be included in the `Authorization` header of API requests.

## Setup

### Generate Tokens for Existing Users
Run the following command:
```bash
python manage.py drf_create_token <username>
