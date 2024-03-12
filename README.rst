===========
scikit-talk
===========


.. image:: https://img.shields.io/pypi/v/scikit_talk.svg
        :target: https://pypi.python.org/pypi/scikit_talk

.. image:: https://img.shields.io/travis/partigabor/scikit_talk.svg
        :target: https://travis-ci.com/partigabor/scikit_talk

.. image:: https://readthedocs.org/projects/scikit-talk/badge/?version=latest
        :target: https://scikit-talk.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status



## [UPDATE]:  scikit-talk is maintained and continues to be developed here: https://github.com/elpaco-escience/scikit-talk

===========

Scikit-talk helps to process real-world conversational speech data.

Scikit-talk is a free and open source Python library to help working with transcriptions of conversational speech data, tailored for the research community.
The ultimate aim is to make the processing, analyzing, and merging of such corpora speedier, and less cumbersome.
Scikit-talk is still in development, with various modules underway. The current version features a working Preprocessor module.

Preprocessor module - build dataframes from files (e.g. .eaf, .cha, .txt).
This module currently contains 3 functions. They essentially execute similar tasks for different transcription formats.
The functions read in differently formatted conversational speech data, returning them in a unified format, which is then comparable, concatenatable,
and easier to work on.

The functions of the Preprocessor module take two arguments, an input path, and an output path, where the latter is optional.
If an output path is given, a .csv file is written there, which contains the a dataframe of all the transcription files that were read in.
If only an input file is given, the functions return a dataframe compiled from the files.

The data is organized into the following columns: begin, end, speaker, utterance, source.
If the corpus provides timestamps, begin and end will contain these in a pandas.datetime format, otherwise NaN.

We assume that the corpora and files are formatted perfectly, adhering to the requirements of various standards and conventions (e.g. Linguistic Data Consortium).

* Free software: MIT license
* GitHub: https://github.com/partigabor/scikit_talk

Features
--------

* Preprocessor

Usage:

``cha_to_dataframe(path_in, *path_out)``
    This function reads .cha files, transcriptions of speech that were produced in the CHAT format. 
    
``eaf_to_dataframe(path_in, *path_out)``
    This function reads .eaf files, transcriptions of speech that were produced in the ELAN format. 
    
``def ldc_to_dataframe(path_in, *path_out)``
    This function reads .txt files, transcriptions of speech that were produced in the LDC format. 
    
All three function shall have the same output:
The function takes the files, reads and appends them one by one, line by line, and returns one dataframe.
The function takes two arguments: an input path (e.g. path_in) and an output path (e.g. path_out), where the latter is optional.

If you only give the input path (path_in), the function returns a pandas dataframe object.
If you give the optional output path (path_out) as well, the function writes the dataframe into that path, as a .csv file.
path_in should be a string, pointing to a folder where .cha files are located. Example: path_in = '/folder/'
path_out should be a string, pointing to a folder where you want your dataset written. Example: path_out = '/folder/output/'
You have to make this output directory yourself before calling the function.

Overall, calling a function should look like the following:
    preprocessor.ldc_to_dataframe(path_in)
    OR
    preprocessor.ldc_to_dataframe(path_in, path_out)

Credits
-------
This package uses tools from the speach_ library made by Le Tuan Anh, and the pylangacq_ library by Jackson L. Lee.
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _speach: https://github.com/neocl/speach
.. _pylangacq: https://github.com/jacksonllee/pylangacq
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
