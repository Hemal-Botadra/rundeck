from setuptools import setup

install_requires = [
    "ddtrace",
    "grpcio",
    "protobuf",
    "pxproto",
    "python-json-logger",
    "redis[hiredis]<4.4",
    "uvloop",
    "Pillow",
    "apache-airflow[kubernetes]==2.9.1",
]

setup(
    name='my-package',
    version=f'1.2.3',
    description='This is an awesome Python package',
    author='Hemal',
    install_requires=install_requires,
    license='MIT',
)