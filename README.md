# Linkedin Jobscraper

## This is Work in Progress

### How to use:

Edit the base.py file. The file is devided into two modules: the first downloads a list of jobs into a json document and the second part reads that document and follows all the links stored there and gets the job details for every job.

Edit the search_term variable to fit your needs (e.g. 'devops', or 'support'). Then edit the filename in which you want to save the jobs list (a parameter of the to_file function)

Edit the details to `with file.open` function to load the file you saved eralier and then provide a details file name to the to_file function at the end.

