#!/usr/bin/env python
from setuptools import setup

setup(
    name='lib-agent',
    version='1.0.4',
    description='Using OnlyKey as hardware SSH and GPG agent',
    author='CryptoTrust',
    author_email='admin@crp.to',
    url='http://github.com/onlykey/onlykey-agent',
    packages=[
        'libagent',
        'libagent.age',
        'libagent.device',
        'libagent.gpg',
        'libagent.signify',
        'libagent.ssh',
    ],
    install_requires=[
        'bech32>=1.2.0',
        'cryptography>=3.4.6',
        'pycryptodome>=3.9.8',
        'docutils>=0.16',
        'python-daemon>=2.3.0',
        'wheel>=0.32.3',
        'backports.shutil_which>=3.5.1',
        'ConfigArgParse>=0.12.1',
        'python-daemon>=2.1.2',
        'ecdsa>=0.13',
        'pynacl>=1.4.0',
        'mnemonic>=0.18',
        'pymsgbox>=1.0.6',
        'semver>=2.2',
        'unidecode>=0.4.20',
    ],
    platforms=['POSIX'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Communications',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
)
