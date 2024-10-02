from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd

# Azure Text Analytics credentials
endpoint = "https://cognitive05.cognitiveservices.azure.com/"
key = "2c212b98108e483da10026f4cb0cca72"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return client

client = authenticate_client()

# Load files (example: loading from local directory)
documents = []
filenames = ["file1.txt", "file2.txt"]
for filename in filenames:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        documents.append({"id": filename, "text": text})

# Prepare the input for sentiment analysis
documents_list = [{"id": doc["id"], "text": doc["text"]} for doc in documents]

response = client.analyze_sentiment(documents=documents_list, show_opinion_mining=True)

results = [doc for doc in response if not doc.is_error]
for result in results:
    print("Document Id:", result.id)
    print("Overall Sentiment:", result.sentiment)
    print("Positive phrases:")
    for sentence in result.sentences:
        for mined_opinion in sentence.mined_opinions:
            print(" - Aspect:", mined_opinion.aspect)
            print(" - Opinion:", mined_opinion.opinion)
