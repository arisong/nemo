def clean_text(text):
    
    text = text.strip()
    text = text.replace(u'\xa0', u' ')

    text = text.replace(r'’', '\'')
    text = text.replace(r'“', '\"')
    text = text.replace(r'”', '\"')
    text = text.replace(r'don\'t', 'do not')
    text = text.replace(r'didn\'t', 'did not')
    text = text.replace(r'won\'t', 'will not')
    text = text.replace(r'wouldn\'t', 'would not')
    text = text.replace(r'can\'t', 'can not')
    text = text.replace(r'couldn\'t', 'could not')
    text = text.replace(r'wasn\'t', 'was not')
    text = text.replace(r'weren\'t', 'were not')
    text = text.replace(r'\'re', ' are')
    text = text.replace(r'\'d', ' would')
    text = text.replace(r'\'ll', ' will')
    text = text.replace(r'\'ve', ' have')
    text = text.replace(r'\'m', ' am')

    return text
