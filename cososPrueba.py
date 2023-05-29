#words = nltk.word_tokenize(sample)
#print('tokenizado: \n',words)

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def normalize(words):
    words = remove_non_ascii(words)
    words = replace_numbers(words)
    return words

#words = normalize(words)
#print('Normalizado \n',words)

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = SnowballStemmer('spanish')
    stems = [stemmer.stem(i) for i in words]
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""

    #nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(i) for i in words]
    return lemmas

def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return stems, lemmas

#stems, lemmas = stem_and_lemmatize(words)
#print('Stemmed:\n', stems)
#print('\nLemmatized:\n', lemmas)