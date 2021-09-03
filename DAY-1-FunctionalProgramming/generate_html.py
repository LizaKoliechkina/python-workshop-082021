def generate_html(color: str):
    def wrapper(fn):
        def inner(name: str):
            with open('template.html', 'r') as file:
                highlighted_name = f'<span style="color: {color};">{name.title()}</span>'
                temp = file.read().replace('{{ name }}', name.title()).replace('{{ welcome }}', fn(highlighted_name))

            with open(f'{name}-template.html', 'w') as file:
                file.write(temp)

            return fn(name)
        return inner
    return wrapper


@generate_html('blue')
def get_name(name):
    return f'Hello, {name}'


@generate_html('green')
def get_nick(nick):
    return f'Hello, {nick}'


get_nick('ala')
