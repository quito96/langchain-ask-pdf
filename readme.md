# Langchain Ask PDF (Tutorial)

 - !GM Version!

>You may find the step-by-step video tutorial to build this application [on Youtube](https://youtu.be/wUAUdEw5oxM).

This is a Python application that allows you to load a PDF and ask questions about it using natural language. The application uses a LLM to generate a response about your PDF. The LLM will not answer questions unrelated to the document.

## How it works

The application reads the PDF and splits the text into smaller chunks that can be then fed into a LLM. It uses OpenAI embeddings to create vector representations of the chunks. The application then finds the chunks that are semantically similar to the question that the user asked and feeds those chunks to the LLM to generate a response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.


## Installation

To install the repository, please clone this repository and install the requirements:

```bash
pip install -r requirements.txt
```

You will also need to add your OpenAI API key to the `.env` file.

## Usage

To use the application, run the `main.py` file with the streamlit CLI (after having installed streamlit): 

```bash
streamlit run app.py --server.port 8089
```


## Contributing

This repository is for educational purposes only and is not intended to receive further contributions. It is supposed to be used as support material for the YouTube tutorial that shows how to build the project.

----
## Systemd Service Installation for Automatic Run as askpdf.service


## Step 1: Check and create the group
First, make sure the group exists:

```bash
getent group streamlitapp
```

If the group streamlitapp doesn't exist, create it with the following command:
```bash
sudo groupadd streamlitapp
```

## Step 2: Generate the content for askpdf.service
The generated service file content is:
```ini
[Unit]
Description=askpdf  Service
After=network.target
[Service]
Type=simple
ExecStart=/home/marantec/anaconda3/envs/untitled/bin/python -m streamlit run /home/marantec/PycharmProjects/langchain-ask-pdf/app.py
WorkingDirectory=/home/marantec/PycharmProjects/langchain-ask-pdf/
Restart=always
RestartSec=3
User=root
Group=streamlitapp
[Install]
WantedBy=multi-user.target
```

## Step 3: Instructions and Commands
Save the content above in a file named 'askpdf.service' and place it in '/etc/systemd/system/'.
```bash
sudo nano /etc/systemd/system/askpdf.service 
```

### Then, activate the systemd service for askpdf:
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable askpdf
```
```bash
sudo systemctl start askpdf
```
```bash
sudo systemctl status askpdf
```




### Check Journal 
```bash
journalctl -u askpdf.service -f
```