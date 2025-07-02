# e-e Performance Indicator ML Project Tutorial

## Directory
### setup.py
setting up the machine learing model as a package helps build my entire machine learning applocation as a package and even deploy in Pi Pi

### requirements.txt


### .gitignore


### README.md


### src(folder)
once this is built, it becomes a resource and can be uploaded just like common packages ie. seaborn, pandas etc. The find_packages() function fetches and recognises the package through the __init__.py file. This is where the actual machine learning model is located

The <font color="blue"> Components Folder </font> contains all the modules created
we'll probably create a process called data ingestion(basically reading data from a database or data set)
they include;

* data ingestion as "ingestion.py"
* data transformation as "transformation.py"
* model trainer as "model_trainer.py"
* initialization or build file as "__init__.py"
* pipelines as "pipeline.py" (with training and prediction)

The <font color="blue"> Pipeline Folder </font> contains

The <font color="blue"> Exception File </font> contains my very own custom exception handling code. Exception handling allows a program to gracefully manage unexpected events or errors that occur during runtime. It provides a structured way to deal with the errors, preventing the program from crashing and potentially allowing it to recover or continue execution

The <font color="blue"> Log File </font> contains

The <font color="blue"> Utility file </font> contains


### venv(folder)