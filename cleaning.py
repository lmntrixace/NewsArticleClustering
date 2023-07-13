import re

def preprocess_text(text, max_length=None):
    cleaned_text = re.sub('<[^<]+?>', '', text)

    cleaned_text = re.sub(r'\[embed.+?\].+?\[/embed\]', '', cleaned_text)

    cleaned_text = re.sub(r'\[google.+?\].+?\[/google\]', '', cleaned_text)

    main_body = re.search(r'<body>(.*?)</body>', cleaned_text, re.IGNORECASE | re.DOTALL)
    if main_body:
        cleaned_text = main_body.group(1)

    cleaned_text = cleaned_text.strip()

    if max_length is not None and len(cleaned_text) > max_length:
        cleaned_text = cleaned_text[:max_length]

    return cleaned_text