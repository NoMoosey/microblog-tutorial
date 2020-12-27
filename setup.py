from setuptools import setup

setup(
    name='flask-tutorial',
    author='Joe Loesch',
    author_email='joey.loesch@gmail.com',
    description='Following a flask tutorial...',
    install_requires=[
        "Flask >= 1.1.2",
        "Flask-WTF >= 0.14.3",
        "python-dotenv >= 0.15.0",
        "Flask-SQLAlchemy >= 2.4.4",
    ]
    )