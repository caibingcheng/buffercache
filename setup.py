from setuptools import setup
import datacache

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(name="datacache",
      version=datacache.__version__,
      author="bbing",
      author_email="jack_cbc@163.com",
      url="https://github.com/caibingcheng/datacache",
      description="a tool for data caching",
      tests_require=["pytest", "pytest-cov"],
      long_description=long_description,
      license="MIT",
      python_requires=">=3.0",
      )
