from setuptools import setup

setup(
    name="brute_tool",
    version="1.0",
    py_modules=["module", "main"],
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'brute-start=main:menu',
        ],
    },
)
