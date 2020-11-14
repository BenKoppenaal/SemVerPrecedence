# SymVer Precedence Checker

This Python package provides functionality to determine the precedence between two Semantic Versioning (SemVer) strings. For example, ```determinePrecedence("1.0.0", "0.9.9")``` will return true as the first SemVer string has a higher precedence than the second SemVer string. 

However, the functionality does NOT check the validity of the provided SemVer strings and assumes that no build metadata is included.

## Requirements

- Python 3.6+

## Installation

To use this package in all your python projects, please download this repository and use the following command in the package root directory to install the package.

```
~/SemVerPrecedence > pip3 install .
Processing /home/ben/SemVerPrecedence
Installing collected packages: SemVerPrecedence
  Running setup.py install for SemVerPrecedence ... done
Successfully installed SemVerPrecedence-0.0.1
```

## Uninstallation

To uninstall the package use the following command:

```
~/SemVerPrecedence > pip3 uninstall SemVerPrecedence
```

## Usage example

The package has two functions that can be imported and used to determine the SemVer precedence. One uses string manipulation, the other uses regular expressions. The following examples show the import string for each version.

Using string manipulation:
```
from SymVerPrecedence.precedenceByStringManipulation import determinePrecedence
``` 

Using regular expression:
```
from SymVerPrecedence.precedenceByRegex import determinePrecedence
``` 

An example using the Python interpreter in a terminal:
```
~ > python3.8
Python 3.8.0 (default, Oct 28 2019, 16:14:01) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from SymVerPrecedence.precedenceByRegex import determinePrecedence
>>> determinePrecedence("1.0.0", "0.9.9")
True
>>> determinePrecedence("1.0.0", "2.0.0")
False
```

## Unit tests

Unit tests have been created for both the string manipulation and regular expression version of the ```determinePrecedence``` function. 

Use the following command in the root directory of the package to run all tests.

```
python3 -m unittest -v
```

## References

The [official Python code style](https://www.python.org/dev/peps/pep-0008/) was not followed for naming conventions. The use of camelCase in the initial function name (```determinePrecedence```) was used to set the precedent for naming.

[SemVer BNF](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions)

## LICENSE
MIT