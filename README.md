# Getting Started

A lot of learning and inspiration for this project was gotten from:

- https://github.com/ewulczyn/wiki-detox
- https://www.tensorflow.org/install


## Instructions for Mac
- Upgrade to Python 3 using pyenv using homebrew by running `brew install pyenv`.

- For tensorflow you'll need python 3.8. So after installing `pyenv` from the first step, 
  - run `pyenv install 3.8.0`
  - run `pyenv global 3.0.8`

  - running `python -V` should show a response of ```Python 3.8.0```. if not, you may have to add pyenv to your `bash_profile` or `zsh_profile`.
  Instructions for doing that can be found in step 2 of the Readme here https://github.com/pyenv/pyenv

- Run the following commands to complete your environment
    - `pip install --upgrade pip`
    - `pip install tensorflow`
    - `pip install -r requirements.txt`
- Jupyter notebook is the web app used to create and train models. 
    - Start Jupyter notebook by running `jupyter notebook`

## Learnings
### A few personal notes on how ML works, in this case for text classification

Overview steps
- Get training data
    - It can be sorted or unsorted. Either ways you decide what you're going to work with. Most people get sorted data which is easier to train. Others prefer to sort the data in the model definition code. It's really up to you as a dev.

- Divinde data into 3 - Trainiing, Validation and testing.

    - This can be 3 different files or 3 files in 3 different folders. There are Python ML packages that can read them in various file/folder structures.

    - Others too would like to do this in the actual code by dividing them into arbitrary percentages.
    It's really up to you as a dev.

- Create a new Jupyter notebook file and set the following in code:
    - where the data is coming from

    - Define your 'bag of words'
        - Words that the code will look out for in the text to help in training. Assuming that it is already provided. 

    - number of levels the data will go through in trainig. There's a tensorflow command to create a level.
        - The model actually does not take in raw strings so before the string starts entering the levels, it will have to be 'tokenized' - There's a command for that.

- Add training command to file to start training. Run the file in Jupyter notebook.

- If you're happy with the testing and validation accuracy results, `serialize` (or package in dev language) your model.

- A 'seriealized' model can be used in a REST endpoint function that takes the same kind of data it was trained with. Then the endpoint will spit out the result.
    - For mobile apps the serialized model can be added to the mobile app code and can be used with tensorflow there.

    - For web apps, there's tensorflow js that can employ the use of models in Javascript.
