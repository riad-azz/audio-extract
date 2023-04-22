try:
    from setuptools import find_packages, setup, Command
except ImportError:
    raise ImportError(
        "Audio Extract could not be installed, probably because "
        "setuptools is not installed on this computer.\n"
        "Install setuptools with $ pip install setuptools"
        "try again."
    )


class AddToPathCommand(Command):
    """
    Custom command to add package to system's PATH during installation.
    """
    description = 'Add package to system PATH'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Add package directory to PATH
        import sys
        from pathlib import Path

        package_dir = Path(__file__).resolve().parent
        if str(package_dir) not in sys.path:
            sys.path.insert(0, str(package_dir))


requires = [
    "ffmpeg>=1.4",
    "imageio-ffmpeg>=0.4.8",
    "mutagen>=1.46.0",
    "py-file-type>=0.1.0",
]

long_description = open('README.md').read()
long_description_content_type = 'text/markdown'

setup(
    name='audio_extract',
    version='0.3.0',
    author='riad-azz',
    author_email='riadh.azzoun@hotmail.com',
    description='Extract and trim audio from videos or trim audios.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url='https://github.com/riad-azz/audio-extract',
    project_urls={
        "Source": "https://github.com/riad-azz/audio-extract",
    },
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=requires,
    license="MIT License",
    keywords=["convert video", "audio", "ffmpeg", "video to mp3"],
    entry_points={
        'console_scripts': [
            'audio-extract=audio_extract.execute:main',
        ],
    },
    cmdclass={
        'add_to_path': AddToPathCommand,
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Conversion",
    ],
)
