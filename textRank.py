import spacy
import pytextrank

import gensim
from gensim.summarization import summarize
#import summa
from summa import summarizer

text = """India recorded its lowest daily Covid-19 cases in over four months on Tuesday as it
registered 30,093 fresh cases of the coronavirus disease, the Union ministry of health and
family welfare data showed. The last time India's Covid-19 tally was below 30,000-mark was on 
March 16 when the country saw 28,903 fresh cases.

The country also saw 374 deaths due to Covid-19 in the last 24 hours, taking the death toll to 414,482. This is also the lowest death count India has seen after over three months. India witnessed deaths below 400 on March 30 when 354 fatalities were recorded.

Active cases of Covid-19 in the last 24 hours dipped sharply by 15,535, bringing the current infections in the country down to 406,130, the health ministry data showed. These account for 1.35% of the total infections reported in the country.

At least 45,254 people recovered from the infectious disease in the last 24 hours, taking India's recovery rate to 97.32%."""

en_nlp = spacy.load("en_core_web_sm")
en_nlp.add_pipe("textrank", config={ "stopwords": { "word": ["NOUN"] } })
doc = en_nlp(text)
tr = doc._.textrank
print("\n")
print("TEXTRANK Summarization")
for sent in tr.summary(limit_phrases=10, limit_sentences=2):
    print(sent)

print("\n")

print("SUMMA Summarization\n")
print(summarizer.summarize(text))
    
print("\n")
print("GENSIM Summarization\n")
print(summarize(text))
print("\n")
print("SUMMA Summarization with 0.3 ratio\n")
print(summarizer.summarize(text,ratio=0.3))
print("\n")

print("SUMMA Summarization with 0.5 ratio\n")
print(summarizer.summarize(text,ratio=0.5))
