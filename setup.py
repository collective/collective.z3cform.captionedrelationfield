"""Installer for the collective.z3cform.captionedrelationfield package."""

from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="collective.z3cform.captionedrelationfield",
    version="1.0a1",
    description="An add-on for Plone that adds a relationfield that can optionally store a caption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Plone Community",
    author_email="collective@plone.org",
    url="https://github.com/collective/collective.z3cform.captionedrelationfield",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.z3cform.captionedrelationfield/",
        "Source": "https://github.com/collective/collective.z3cform.captionedrelationfield",
        "Tracker": "https://github.com/collective/collective.z3cform.captionedrelationfield/issues",
        # 'Documentation': 'https://collective.z3cform.captionedrelationfield.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.9",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "plone.app.vocabularies",
        "plone.app.z3cform",
        "plone.autoform",
        "z3c.form",
        "z3c.relationfield",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.testing",
            "plone.supermodel",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.z3cform.captionedrelationfield.locales.update:update_locale
    """,
)
