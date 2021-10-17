# Streamlit sample app - AIオオタニサン本塁打予測

[Streamlit](https://www.streamlit.io/)をサクッと使うためのサンプルアプリケーションです.

![](document/img/sample.png)

## Licence

MIT

## 利用方法

forkして好きなアプリケーションに作り変えることを推奨します.

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

# Maintainer

[@shinyorke(Shinichi-Nakagawa)](https://github.com/Shinichi-Nakagawa)
