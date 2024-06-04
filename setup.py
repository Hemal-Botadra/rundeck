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
    "idna==1.10",
    "apache-airflow[kubernetes]==2.9.0",
]

setup(
    name='my-package',
    version=f'1.2.3',
    description='This is an awesome Python package',
    author='Hemal',
    install_requires=install_requires,
    license='MIT',
)