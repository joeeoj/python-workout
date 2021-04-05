def myxml(tag: str, text: str = '', **kwargs: str) -> str:
    """the first argument is the name of the tag. The second argument is the content (text).
    The name-value pairs are attributes"""
    if kwargs:
        template = f'<{tag} {{}}>{{}}</{tag}>'
        attrs = ' '.join([f'{k}="{v}"' for k,v in kwargs.items()])
        return template.format(attrs, text)
    else:
        template = f'<{tag}>{{}}</{tag}>'
        return template.format(text)
