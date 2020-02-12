import re

def clean_email(text):
    pattern = ''
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_http(text):
    #pattern = 'https?://([\w]|[$-_@.&+]|[!*\\(\\),])+'
    pattern = 'https?://(\w|[^\w\s])+'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_pic(text):
    pattern = 'pic.twitter.com/\S+'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_ATtag(text):
    pattern = '@\S+[ ]?'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_hashtag(text):
    pattern = '#\S'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_specialsymbol(text):
    pattern = '[^\w\s]'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_consonant_vowels(text):
    pattern = '[ㄱ-ㅎㅏ-ㅣ]+'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text

def clean_newline(text):
    pattern = '\n'
    repl = ''
    cleaned_text = re.sub(pattern,repl,text)
    return cleaned_text
