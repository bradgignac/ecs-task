from click.testing import CliRunner

from ecstask import cli


template = '{ "name": "{{ name }}" }'


def test_generate_from_stdin():
    runner = CliRunner()
    args = ['--var', 'name', 'brad']
    result = runner.invoke(cli.generate, args, input=template)
    assert result.output == '{ "name": "brad" }\n'
    assert result.exit_code == 0


def test_generate_from_file():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('template.json', 'w') as f:
            f.write(template)

        args = ['template.json', '--var', 'name', 'brad']
        result = runner.invoke(cli.generate, args)
        assert result.output == '{ "name": "brad" }\n'
        assert result.exit_code == 0
