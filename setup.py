from distutils.core import setup
setup(
  name = 'SMSEdge-API-Python',
  packages = ['SMSEdge-API-Python'],
  version = '1.0.0',
  license='MIT',
  description = 'SMSEdge API package for Python development',
  author = 'Mimon Copitman',
  author_email = 'mimon@smsedge.io',
  url = 'https://github.com/SMSEdge/API-Python',
  download_url = 'https://github.com/SMSEdge/API-Python/releases/tag/1.0.0',
  keywords = [
    "SMSEdge",
    "SMSEdge-API",
    "SMSEdge-API-Python"
  ],
  install_requires=[
          'cerberus',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)