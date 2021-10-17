# Streamlit sample app - AIオオタニサン本塁打予測

[Streamlit](https://www.streamlit.io/)をサクッと使うためのサンプルアプリケーションです.

[PyCon JP 2021](https://2021.pycon.jp/)「[実践Streamlit & Flask - AIプロジェクトをいい感じにする技術](https://speakerdeck.com/shinyorke/service-development-with-streamlit-and-flask)」にて披露したアプリケーションでもあります.

![](document/img/sample.png)

## Licence

MIT

## 利用方法

このリポジトリをforkもしくはダウンロードして好きなアプリケーションに作り変えることを推奨します.

学習や仕事, 個人開発などお好きな目的・利用スタイルで使っていただいて構いません.

## install

### local

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ poetry install
```

## Usage

### local

```bash
(venv) $ stremlit run app.py
```

### Docker

```bash
docker-compose -f docker-compose-local.yml up
```

### Test

```bash
(venv) $ pytest .
```

### Cloud Run(for GCP)

`gcloud`コマンドを手元で使えるようにした上で

```bash
sh deploy.sh ${gcp project id} ${your service name}
```

`your service name` で指定した名前でCloud Runのサービスが作られます.

### CI(GitHub Actions)

`test->deploy`のJobを定義しています.

deployを動かすためには以下のsecretsを設定する必要があります.

- GCP_PROJECT_ID(GCPのProject ID)
- GCP_SA_KEY(必要な権限を持ったCredential JSON)

詳細は[deploy-cloudrun](https://github.com/google-github-actions/deploy-cloudrun)を御覧ください.

なお, Cloud Run環境は最初に作る必要があります（上記[deploy.sh](deploy.sh)を実行するのが手っ取り早いかも).

# Maintainer

[@shinyorke(Shinichi-Nakagawa)](https://github.com/Shinichi-Nakagawa)
