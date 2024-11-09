!pip install nltk

import nltk
# download punkt required for word_tokenize
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# create a variable text
text = " Advancements in space and sky technologies are transforming our understanding of the universe and improving life on Earth. Satellites enable real-time monitoring of climate, natural disasters, and environmental changes, helping us respond more effectively to global challenges. Meanwhile, developments in space exploration, like advanced telescopes and planetary rovers, reveal new insights about distant galaxies and planets. Together, these technologies drive innovation, deepen scientific knowledge, and inspire future generations to explore beyond our world. "

# tokenize the text into words
tokens = word_tokenize(text)

# print the list of tokens
print(tokens)

# count the number of tokens
num_tokens = len(tokens)

# print the number of tokens
print("Number of tokens:", num_tokens)

# create a frequency distribution of the tokens
freq_dist = FreqDist(tokens)
print(freq_dist)

# print the frequency of each token
for token, frequency in freq_dist.items():
    print(f"{token}: {frequency}")
