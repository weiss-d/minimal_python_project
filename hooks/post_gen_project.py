"""
Script for creating Dockerfile if 'use_docker' option is 'y'
"""
use_docker: str = '{{ cookiecutter.use_docker }}'
project_slug: str = '{{cookiecutter.project_slug}}'
python_version: str = '{{cookiecutter.python_version}}'

if use_docker == 'y':
    with open("Dockerfile", "w+") as file:
        file.write(
            f"""FROM python:{python_version}-alpine

WORKDIR /usr/src/{project_slug}

COPY src .
COPY requirements.txt .

RUN addgroup --system npuser \
    && adduser \
      --disabled-password \
      --home "$(pwd)" \
      --ingroup npuser \
      --no-create-home \
    npuser \
    && pip install --no-cache-dir -r requirements.txt

USER npuser

CMD ["python", "-m", "{project_slug}"]"""
        )
