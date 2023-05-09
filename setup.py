# pylint: disable=C0114
from typing import Dict, List, Optional
from setuptools import setup

AUTHOR: str = "lindsaygelle"
AUTHOR_EMAIL: Optional[str] = None
CLASSIFIERS: List[str] = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
DESCRIPTION: str = "liquibase"
GITHUB_AUTHOR: str = AUTHOR
GITHUB_REPOSITORY: str = "liquibase"
INCLUDE_PACKAGE_DATA = True
INSTALL_REQUIRES: List[str] = ["semver==3.0.0"]
KEYWORDS: List[str] = [GITHUB_REPOSITORY]
with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
MAINTAINER: str = AUTHOR
MAINTAINER_EMAIL: Optional[str] = AUTHOR_EMAIL
NAME: str = "liquibase"
PACKAGE_DIR: Dict[str, str] = {NAME: NAME}
PACKAGES: List[str] = [NAME]
# noqa: E501
PROJECT_URLS: Dict[str, str] = {
    "Bug Reports": f"https://github.com/{GITHUB_AUTHOR}/{GITHUB_REPOSITORY}/issues",
    "Documentation": f"https://github.com/{GITHUB_AUTHOR}/{GITHUB_REPOSITORY}",
    "Source Code": f"https://github.com/{GITHUB_AUTHOR}/{GITHUB_REPOSITORY}",
}
PYTHON_REQUIRES: str = ">=3.8"
URL: str = f"https://www.github.com/{GITHUB_AUTHOR}/{GITHUB_REPOSITORY}"
VERSION = "1.0.0"

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS,
    description=DESCRIPTION,
    include_package_data=INCLUDE_PACKAGE_DATA,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    name=NAME,
    package_dir=PACKAGE_DIR,
    packages=PACKAGES,
    project_urls=PROJECT_URLS,
    python_requires=PYTHON_REQUIRES,
    url=URL,
    version=f"{VERSION}",
)
