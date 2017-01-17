import io

import ecstask


def test_generate_with_vars():
    template = u'{ "name": "{{ name }}" }'
    buffer = io.StringIO(template)
    result = ecstask.generate(buffer, {'name': 'Brad'})
    assert result == '{ "name": "Brad" }'
