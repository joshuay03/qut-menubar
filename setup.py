from setuptools import setup

APP = ['app_generator.py']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['_csv', 'PyQt5', 'rumps']
}

setup(
    app=APP,
    name='MyQUT',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['_csv', 'PyQt5', 'rumps']
)
