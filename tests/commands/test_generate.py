import io

from ecstask.commands import generate


def test_generate_with_vars():
    template = u'{ "name": "{{ name }}" }'
    buffer = io.StringIO(template)
    result = generate(buffer, {'name': 'Brad'})
    assert result == '{ "name": "Brad" }'
