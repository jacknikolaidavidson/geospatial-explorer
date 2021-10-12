# geospatial-explorer
Demo geospatial application in Python to provide interactivity throughout the prototype phase and explore data coming from the TERN WMS


# Running
- `python3 -m pip install virtualenv`
- `python3 -m virtualenv env`
- `. env/bin/activate`
- `pip install -r requirements.txt`
- `streamlit run application.py`
- (optional) streamlit run pydeckapp.py --server.port=8081
- (optional) streamlit run application.py --server.port=8082
- (optional) port forward appropriate port through local VSCode 
