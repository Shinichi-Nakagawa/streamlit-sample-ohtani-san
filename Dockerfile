FROM python:3.9

LABEL  maintainer "Shinichi Nakagawa <spirits.is.my.rader@gmail.com>"

# install
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install

# app
COPY app.py app.py ./
ADD assets assets
ADD dataset dataset
ADD entities entities
ADD interfaces interfaces
ADD model model
ADD usecase usecase
CMD streamlit run app.py
EXPOSE 8080:8501
