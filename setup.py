try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "Audio Extract could not be installed, probably because "
        "setuptools is not installed on this computer.\n"
        "Install setuptools with $ pip install setuptools"
        "try again."
    )

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
    version='0.1.0',
    author='riad-azz',
    author_email='riadh.azzoun@hotmail.com',
    description='Extract and trim audio from videos or trim audios.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url='https://github.com/riad-azz/py-audio-extract',
    project_urls={
        "Source": "https://github.com/riad-azz/py-audio-extract",
    },
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=requires,
    license="MIT License",
    keywords=["convert video", "audio", "ffmpeg", "video to mp3"],
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
