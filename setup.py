# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""setup config
"""
from setuptools import setup, find_packages


setup(
    name = "sample",        # 项目名
    version = '1.0.0',      # 当前包版本
    description = "short des",  # 项目短描述
    log_description = "log des",    # 项目长描述
    url = "https://github.com/sue-chain/setupproject",      # project homepage url
    author = "sue.chain",      # 作者
    author_email = "sue.chain@gmail.com",      # 作者邮箱
    license = "BSD",            # 常用BSD, MIT
    keywords = "sample keyword",        # 关键字
    # 当前项目要包含的包，用find_packages检索当前项目，exclude排除不需要检索的目录
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']), 
    # 当前项目依赖软件
    install_requires=['arrow==0.7.0'],
    # 内嵌数据包，data_files可以指向项目外部路径
    package_data={
        'sample': ['package_data.dat'],
    },
    # data_files=[('my_data', ['data/data_file'])],
    classifiers = [     # 详细当前项目成熟度，如开发状态，版权，支持python版本
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ],
)
