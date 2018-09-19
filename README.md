# Sallapam
### A retrieval based Malayalam chatbot based on an indexing strategy
Chatbots are virtual agents mimicking human conversational style using artificial intelligence either in spoken or textual form.  Chatbot has variety of applications like customer support.
Developing a regional languge bot is a challenging task. A chatbot that converses in Malayalam is the first attempt in Malayalam text processing area. Sallapam is a retrieval based chatbot enabling conversations based on a domain specific Malayalam corpus. Tourism domain is selected as the Malayalam corpus. </br>
Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly. Whoosh library is incorporated with the Malayalam chatbot engine for indexing purpose. The dataset created for the project is in tourism domain. The data is collected from various travel blogs and websites. The data is preprocessed and kept in text files for further processing.
The corpus is indexed and the indexes are used for generate the appropriate responses for the user queries. The user query is compared with the stored index terms generated using Whoosh. A candidate set of responses is retrieved. The ranking of the possible responses is done using Jaccard index. The most appropriate response is selected and given as the output.
### REQUIREMENTS
1. Malayalam Dataset
2. Whoosh Package
3. Flask Package
4. NLTK Package

- __Whoosh Installation:__

Whoosh is compatible with Python 2.5 and higher
If you have ```setuptools``` or ```pip``` installed, you can use ```easy_install``` or ```pip``` to download and install Whoosh automatically:
```
$ easy_install Whoosh
```
or
```
$ pip install Whoosh
```
Read the Whoosh documentation at https://whoosh.readthedocs.org/en/latest/ 
</br>
- A sample experiment dataset is given in the file named "data" in the root directory. 
- The searched index and corresponding response are stored in file named 'in' in index folder of the root directory.

