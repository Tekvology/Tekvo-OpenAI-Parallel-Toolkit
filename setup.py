from setuptools import find_packages, setup

setup(
        name='tekvo-openai_parallel_toolkit',
        version='1.0.0',
        author='Elvin',
        author_email='inquiry@tekvo.io',
        description='Tekvo OpenAI-Parallel-Toolkit is a Python library for handling multiple OpenAI API keys and parallel '
                    'tasks.'
                    ' It provides API key rotation, multithreading for faster task execution, '
                    'and utility functions to boost your OpenAI integration. '
                    'Ideal for efficient large-scale OpenAI usage.',
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url='https://github.com/Tekvology/Tekvo-OpenAI-Parallel-Toolkit',
        packages=find_packages(),  # Automatically find all packages
        classifiers=[  # Optional
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
        install_requires=[
            'openai',
            'colorlog',
            'tqdm',
            'cachetools'
        ],
        python_requires='>=3.8',
)
