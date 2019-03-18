# Pwned Checker v1.0

In a nutshell, this Python script has been made for all that people who wants to know if their mail or mails have ever been pwned using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v2), compatible with all versions of Python higher than Python 2.7 (that includes Python 3.X)

## Prerequisites

For using this script, you have to be sure to have the following things:
* Python 2.7+ 

## Usage

The script usage is pretty simple. It works both on Windows and Linux. For Windows, you can run:
```
python pwnedChecker.py <arguments>
```
For Linux, after giving him execution permissions (*chmod +x pwnedChecker.py*), you can also use:
```
./pwnedChecker.py <arguments>
```
You have several parameters to use:
```
-h, --help                  Displays the help menu
-e, --email EMAIL           Checks a single email
-f, --filename FILENAME     Checks a list of emails given in a file (one per line)
-o, --output OUTPUT         Changes the default output file name (it's only generated when working with a file)
-u, --unverified BOOLEAN    Include unverified breaches too
```

### Running examples
Checking a single email:
```
./pwnedChecker.py -e test@example.com
```
Checking emails from a file:
```
./pwnedChecker.py -f mycoolfile.txt
```
Checking emails from a file changing the output file name and including the unverified breaches:
```
./pwnedChecker.py -f mycoolfile.txt -o butnotascoolasthisone.txt -u true
```

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - The framework used
* [Python](https://www.python.org/) - Language used

## Authors

* **José Ángel Loarces** - [Linkedin](https://www.linkedin.com/in/jose-%C3%A1ngel-loarces-3bb722139/)

## License

This project is licensed under the MIT License.
