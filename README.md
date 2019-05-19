# yieldmo_wordExists
Python Code to Check if a word exists in an grid? Like the find words we used to solve as kids. For this question, you can go left or right, up or down. To keep it simple, no diagonals

Example :

    acdef
    ghije
    mopqu
    swtuv

return true for word `how` and `vue` but false for `mope`


# Pre Requisites
You will need python 3.7 . You can download python from here
https://www.python.org/downloads/

You will also need Git Client. You can download it from here
https://git-scm.com/downloads

You will also need numpy library and can be installed by running `pip install numpy`
However if your python does not come with PIP, you can install PIP from here
https://pip.pypa.io/en/stable/installing/

# Understand the code
To know more about how this code works, please refer to the jupyter notebook [here](
https://github.com/harithatavarthy/yieldmo_wordExists/blob/master/wordExists.ipynb)


# How to run this code

a. Run the command `git clone https://github.com/harithatavarthy/yieldmo_wordExists.git`

b. Run the command `cd yieldmo_wordExists`

c. Now you can search for the word by running the command `python wordExists.py <searchword>`
    
    ex:  python wordExists.py how

You will see the boolean output `true` if the words `how` and `vue` . You can then replace the search word with `mope` and execute the code to see the boolean output `false`
