import jinja2


def generate(input, variables):
    src = input.read()
    template = jinja2.Template(src)
    return template.render(variables)
