import json
import spacy
nlp = spacy.load('en_core_web_trf') # python -m spacy download en_core_web_trf
import random
import statistics
from summarizer import Summarizer #pip install bert-extractive-summarizer
bert_kmeans_model = Summarizer()


file = open('config.json', 'r')
config = json.load(file)
file.close()

if config['compression']['summarisation_model'] == 'bart':
    TOKEN_LENGTH = 1024


def token_length(text):
    
    doc = nlp(text)
    tokenized_list = [str(token.text) for token in doc]
    token_length = len(tokenized_list)
    
    return token_length


def compression_bert_kmeans(text):

    random.seed(42)

    # compress only if text token length exceeds model token length
    if token_length(text) > TOKEN_LENGTH:

        doc = nlp(text)
        sent_length_list = []
        for sent in doc.sents:
            sent_length_list.append(len(sent.text))

        avg_sent_length = statistics.median(sent_length_list)

        est_num_sent = int(round(TOKEN_LENGTH/avg_sent_length, 0))

        text_compressed = bert_kmeans_model(text, num_sentences=est_num_sent)
        text_compressed_length = token_length(text_compressed)

        while text_compressed_length > TOKEN_LENGTH:
            est_num_sent -= 1
            text_compressed = bert_kmeans_model(text, num_sentences=est_num_sent)
            text_compressed_length = token_length(text_compressed)

    else:

        text_compressed = text

    return text_compressed
