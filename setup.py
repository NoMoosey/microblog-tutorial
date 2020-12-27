from setuptools import setup

setup(
    name='flask-tutorial',
    author='Joe Loesch',
    author_email='joey.loesch@gmail.com',
    packages='microblog',
    description='Following a flask tutorial...',
    install_requires=[
        "Flask == 1.1.2",
        "Flask-WTF == 0.14.3",
        "python-dotenv == 0.15.0",
    ],
    )