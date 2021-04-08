def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')

    atts = ' '.join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = ''.join(args)

    return f'<{tag} {atts}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de python 3, por'),
            tag('strong', 'Juracy filho', id='jf'),
            tag('span', 'e'),
            tag('strong', 'Leonardo leitao', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
