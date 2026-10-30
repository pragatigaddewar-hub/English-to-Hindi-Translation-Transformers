# import the tokenizer class
from transformers import AutoTokenizer

# import the model class for translation
from transformers import AutoModelForSeq2SeqLM

# load the tokenizer of the English to Hindi model
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

# load the English to Hindi translation model
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

# the English sentence we want to translate
sentence = "I am going to school."

# convert the sentence into token IDs
inputs = tokenizer(sentence, return_tensors="pt")

# let the model generate the Hindi token IDs
output_ids = model.generate(**inputs)

# convert the Hindi token IDs back into Hindi text
translated = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# print the translated sentence
print(translated)