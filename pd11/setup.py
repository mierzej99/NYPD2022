from setuptools import setup, find_packages

setup(name='homework_exercise',
      version='0.1',
      description='Homework for NYPD class',
      author='Michal Mierzejewski',
      license='MIT',
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      package_data={'homework_exercise': ['data_file.json','data_file_2.toml']},
      zip_safe=False)
