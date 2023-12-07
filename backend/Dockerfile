FROM python:3.9-buster

WORKDIR /src

# 必要なシステムパッケージをインストール
RUN apt-get update

RUN pip install --upgrade pip

RUN pip install poetry
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY . .
RUN poetry install --no-root


# CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
