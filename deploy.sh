project=$1

# image build
gcloud builds submit --tag asia.gcr.io/${project}/streamlit-sample-ohtani-san

# deploy
gcloud run deploy --image asia.gcr.io/${project}/streamlit-sample-ohtani-san --platform managed --memory 512M --region asia-northeast1 --port 8501

