Flask==2.3.3
gunicorn==20.1.0
spacy>=3.0.0,<4.0.0
es_dep_news_trf @ https://github.com/explosion/spacy-models/releases/download/es_dep_news_trf-3.6.1/es_dep_news_trf-3.6.1-py3-none-any.whl

gcloud builds submit --tag gcr.io/unchainednews/receive_text
gcloud run deploy --image gcr.io/unchainednews/receive_text

para correrlo en un una instancie de amazon

todo esto ejecutarlo en la carpeta en donde tengo corriendo el .pem

gianfrancocaneva@Gianfranco-Caneva Codigo % ssh -i "pfi1.pem" ec2-user@ec2-3-90-183-128.compute-1.amazonaws.com en conectar
chmod 400 pfi1.pem y dps vuelvo a correr el comando de arriba
sudo yum install git
sudo yum install pip
pip3 install -r requirements.txt
bajarse el codigo y correr

