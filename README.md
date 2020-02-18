# SupremeUofT
MakeUofT 2020 Project

- [x] Solace connection
- [X] Use TextBlob
  


## Start up project
- Ensure you have the following downloaded:
  - Python 3.6+
  - Textblob
    - pip3 install -U textblob
    - python3 -m textblob.download_corpora
      - If there is a problem and you obtain Certificate error, do the following:
        - on mac: go to application/3.7 and run Install Certificates.command
        - Then rerun the command
  - Paho mqtt
    - pip3 install paho-mqtt


## Extra tips for expanding the project
- Voice recordings + typing as extra data we can use to help contextualize the information being provided in the current setting
- Geofencing -> local servers in a geographical area that can help us load balance and speed up service by using redudnacies from other users within the geofence 
- Augmented reality for people who are writing on trandiational pen and paper

## next steps 
- UI
- Conceptual sentance modal for ML
- get on to tablet
- Pitch to grammarly
