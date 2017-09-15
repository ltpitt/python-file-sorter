# File Sorter

File Sorter will divide your files (ROMs, Movies, other) in folders, using the first letter of the file\'s name
The user can change the directory structure according to his/her preferences.


## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder

Now you have two choices: pip or pipsi.  

Pip is the classic choice.  
Here are [installation instructions](https://pip.pypa.io/en/stable/installing/).  

Once pip is installed, from the script folder:

    $ pip install .

The other option is pipsi.  
If you don't use `pipsi`, you're missing out.  
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Once pipsi is installed, from the script folder: 

    $ git clone https://github.com/ltpitt/python-file-sorter.git
    $ cd python-github-backup
    $ pipsi install .

# Usage

To use it:

    $ file-sorter --help
```
Usage: file-sorter [OPTIONS]

Options:
  --path TEXT                  Path where the sorting will be applied
  --folder_group_size INTEGER  Number of letters that will be grouped into a
                               single folder e.g. 3 will create folders: 0 ABC
                               DEF GHI ...
  --help                       Show this message and exit.
```

### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
