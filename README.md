# English to Hindi Translation using Transformers

This project translates an English sentence into Hindi using a pre-trained Transformer model from Hugging Face.

## About the Project

The model is an Encoder-Decoder Transformer. The Encoder reads and understands the English sentence, and the Decoder generates the Hindi sentence one token at a time.

## Model Used

- Helsinki-NLP/opus-mt-en-hi (pre-trained, about 300 MB)

## How It Works

1. The English sentence is converted into token IDs by the tokenizer
2. The Encoder reads the token IDs
3. The Decoder generates the Hindi token IDs
4. The Hindi token IDs are converted back into Hindi text

## Project Structure

```
translation_app.py    # main script
requirements.txt      # required libraries
README.md             # project description
```

## Installation

```
pip install -r requirements.txt
```

## Usage

Open `translation_app.py`, change the sentence, and run:

```
python translation_app.py
```

Example:

```python
sentence = "I am going to school."
```

Output:

```
मैं स्कूल जा रहा हूँ.
```

## Limitations

- The model is small, so long sentences, slang and technical terms may be translated incorrectly
- Names and unknown words may be written wrongly in Hindi
- The model always uses the masculine form in Hindi (for example "रहा हूँ")
- Works best with short, simple sentences with proper punctuation

## Tools Used

- Python
- Hugging Face Transformers
- PyTorch
- SentencePiece

## Author

Pragati Gaddewar
