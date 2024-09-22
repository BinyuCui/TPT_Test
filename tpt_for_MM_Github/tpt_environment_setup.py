import subprocess

# This program is used to set up the package needed for the ATPT project
# please run this file individually without the main.py if this is your first time working on this project
# package name and version

packages = {
    'picosdk': '1.0',
    'PyQt5': '5.15.7',
    'Pillow':'9.2.0',
    'PyQt5-Qt5'	: '5.15.2',
    'Pygments':	'2.12.0',
    'asttokens':	'2.0.7',
    'backcall':	'0.2.0',
    'colorama':	'0.4.5',
    'cycler':	'0.11.0',
    'decorator':	'5.1.1',
    'executing': '0.10.0',
    'fonttools':	'4.36.0',
    'ipython':	'8.4.0',
    'jedi':	'0.18.1',
    'kiwisolver':	'1.4.4',
    'matplotlib':	'3.5.3',
    'matplotlib-inline':	'0.1.3',
    'numpy':	'1.23.2',
    'packaging':	'21.3',
    'pandas':	'1.5.2',
    'parso':	'0.8.3',
    'pickleshare':	'0.7.5',
    'picoscope':	'0.7.19',
    'pip':	'22.2.1',
    'prompt-toolkit':	'3.0.30',
    'pure-eval':	'0.2.2',
    'pyparsing':	'3.0.9',
    'pypiwin32':	'223',
    'pyserial':	'3.5',
    'python-dateutil':	'2.8.2',
    'pytz':	'2022.7.1',
    'pywin32':	'304',
    'pyserial':	'3.5',
    'python-dateutil':	'2.8.2',
    'pytz':	'2022.7.1',
    'pywin32':	'304',
    'scipy':	'1.9.0',
    'setuptools':	'63.2.0',
    'six':	'1.16.0',
    'stack-data':	'0.4.0',
    'tabulate':	'0.8.10',
    'traitlets': '5.3.0',
    'wcwidth':	'0.2.5'
}

# install package
for package, version in packages.items():
    subprocess.check_call(['python', '-m', 'pip', 'install', f'{package}=={version}'])
