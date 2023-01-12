import json
import torch
#torch.cuda.is_available() # nvidia-smi
from transformers import BartTokenizer, BartForConditionalGeneration
import random


file = open('config.json', 'r')
config = json.load(file)
file.close()


def bart(text, 
         num_words_min=config['summarisation']['number_of_words_minimum'],
         num_words_max=config['summarisation']['number_of_words_maximum'],
         pretrained_model='facebook/bart-large-cnn', 
         truncation=config['summarisation']['truncation'],
         num_beams=config['summarisation']['number_of_beams'],
         repetition_penalty=config['summarisation']['repetition_penalty'],
         length_penalty=config['summarisation']['length_penalty'],
         early_stopping=config['summarisation']['early_stopping']):
    
    random.seed(42)

    try: 
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        bart_model = BartForConditionalGeneration.from_pretrained(pretrained_model)
        bart_tokenizer = BartTokenizer.from_pretrained(pretrained_model)

        bart_tokens = bart_tokenizer.encode(text,
                                            return_tensors='pt',
                                            max_length=1024,
                                            truncation=truncation).to(device)

        bart_ids = bart_model.to(device).generate(bart_tokens,
                                                  min_length=int(num_words_min),
                                                  max_length=int(num_words_max),
                                                  num_beams=num_beams,
                                                  repetition_penalty=repetition_penalty, 
                                                  length_penalty=length_penalty, 
                                                  early_stopping=early_stopping)

        bart_output = [bart_tokenizer.decode(i,
                                             skip_special_tokens=True,
                                             clean_up_tokenization_spaces=False) for i in bart_ids]
    
    except Exception as ex:
        
        print(ex)
        
    return(bart_output[0])
