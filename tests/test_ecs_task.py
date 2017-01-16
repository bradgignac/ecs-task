import io

import ecs_task


def test_generate_with_vars():
    template = u'{ "name": "{{ name }}" }'
    buffer = io.StringIO(template)
    result = ecs_task.generate(buffer, {'name': 'Brad'})
    assert result == '{ "name": "Brad" }'
