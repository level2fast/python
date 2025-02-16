# In this exercise, you'll extend the distributions package with a new class called Binomial. 

# Inside the folder called `4a_binomial_package`, you'll find another folder and a number of files. Here is a description of each
# - distributions, which contains the code for the distributions package including Gaussiandistribution.py and Generaldistribution.py code.
# - setup.py a file needed for building python packages with pip
# - test.py unit tests to help you debug your code
# - numbers.txt and numbers_binomial.txt are data files used as part of the unit tests
# - Binomialdistribution.py and Binomialdistribution_challenge.py choose one of these files for completing the exercise. Binomialdistribution.py includes more of the code already set up for you. In Binomialdistribution_challenge.py, you'll have to write all of the code from scratch. Both files contain instructions with TODOS to fill out.

# Out of all these files, you'll only need to change the following:
# - __init__.py inside the distributions folder. You'll need to import the binomial package
# - either Binomialdistribution.py or Binomialdistribution_challenge.py You'll also need to put your Binomialdistribution.py file into the distributions folder.

# When you're ready to test out your code, you'll want to pip install your distributions package and then run the unit tests. In the terminal, assuming you are in the 4a_binomial_package directory (if not type `cd 4a_binomial_package`), type `pip install .` into the command line. Then run the unit tests by typing `python -m unittest test`. 

# Modify the Binomialdistribution.py code until all the unit tests are passing. 

# Note that if you change the code in the distributions folder after pip installing the package, Python will not know about the changes. You'll need to run `pip install --upgrade .` when you make changes to the package files.

# There is also a solution in the 4b_answer_binomial_package. Try not to look at the solution until your code is passing all of the unit tests.