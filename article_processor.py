import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import urllib.request
import heapq
import re

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


class TextSummarizer:
    def __init__(self, input_data, num_sentences):
        self.input_data = input_data
        self.num_sentences = num_sentences
        self.is_url = self.check_if_url(input_data)

    def check_if_url(self, input_data):
        # Simple regex to check if the input is a URL
        url_pattern = re.compile(r'^(http|https)://')
        return re.match(url_pattern, input_data) is not None

    def fetch_article(self):
        wikipedia_article = urllib.request.urlopen(self.input_data)
        article = wikipedia_article.read()
        return article

    def parse_article(self, article):
        parsed_article = BeautifulSoup(article, 'lxml')
        paragraphs = parsed_article.find_all('p')
        article_text = ""
        for p in paragraphs:
            article_text += p.text
        return article_text

    def calculate_word_frequencies(self, article_text):
        stopwords_list = stopwords.words('english')
        word_frequencies = {}
        for word in word_tokenize(article_text):
            if word not in stopwords_list:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequency)
        return word_frequencies

    def calculate_sentence_scores(self, article_text, word_frequencies):
        sentence_list = sent_tokenize(article_text)
        sentence_scores = {}
        for sent in sentence_list:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 32:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        return sentence_scores

    def summarize(self):
        if self.is_url:
            article = self.fetch_article()
            article_text = self.parse_article(article)
        else:
            article_text = self.input_data

        word_frequencies = self.calculate_word_frequencies(article_text)
        sentence_scores = self.calculate_sentence_scores(article_text, word_frequencies)
        summary_sentences = heapq.nlargest(self.num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ''.join(summary_sentences)
        return summary