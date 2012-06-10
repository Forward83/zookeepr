try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='zookeepr',
    version='1.0.0',
    description='A conference management system',
    author='Zookeep Core Team',
    author_email='zookeepr-core@zookeepr.org',
    url='http://zookeepr.org',
    install_requires=[
        "WebOb",
        "Pylons",
        "SQLAlchemy",
        "AuthKit",
        # FormEncode used to do form input validation
        "FormEncode",
        "WebTest",
        "pastescript",
        # DNS for email address validation
        "dnspython",
        "pylibravatar",
        "vobject",
        "pytz",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite = 'nose.collector',
    package_data={'zookeepr': ['i18n/*/LC_MESSAGES/*.mo',
        'templates/autohandler',
        'templates/*.myt',
        'templates/*/*.myt',
        'public/*.css',
        'public/*.png',
        'public/*.gif',
        'public/*.pdf',
        'public/sponsors/*.gif',
        ]},
    #message_extractors={'zookeepr': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = zookeepr.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
