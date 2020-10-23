import setuptools

setuptools.setup(
  name="monnify-python",
  version="0.1.1",
  description="python app to make integration with monnify easier",
  packages=setuptools.find_packages("src"),
  package_dir={"":"src"})
