project=$1
service=$2
# image build
gcloud builds submit --tag asia.gcr.io/${project}/${service}

# deploy
gcloud run deploy --image asia.gcr.io/${project}/${service} --platform managed --memory 512M --region asia-northeast1 --port 8501

