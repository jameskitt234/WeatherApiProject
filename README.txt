Zynstra Technical task Submission by James Kitt

A simple command line program written in python to retrieve data from a provided
weather API, process the data and write the answers to the provided questions
into a text file as JSON formatted list in a location chosen by the user.
Submission directory contains:
  - README.txt
  - requirements.txt
  - technicalTask.py
  - test_technicalTask.py
  - answers.txt (file containing answers using candidate number 7)

---Prerequisites---
To ensure that the application is able to run correctly please ensure that your
device has the python libraries listed in the requirement.txt file.

---Installation---
Please save the contents of the reposistory to the desired location on your
device. It is important that 'test_technicalTask.py' is located in the same
directory as 'technicalTask.py'.

---How to use---
To use 'technicalTask.py':
  1. Open the command line on your device.
  2. Navigate to the 'technicalTaskSubmission' directory.
  3. On the command line run the file using:
      py technicalTask.py candidateNumber fileSavePath
     	- 'candidateNumber' is the required candidate number which will be used
      	  by the API.
      	- 'fileSavePath' is the path to the location on your device where the
          answers.txt file will be saved. (this should end with a "\")
    Note: On your device "py" may be different for example "python" or "python3"
  4. If the script has run correctly the answers.txt file will be save at your
    specified location.

To use 'test_technicalTask.py':
  1. Open the command line on your device.
  2. Navigate to the 'technicalTaskSubmission' directoy.
  3. On the command line run the file using:
      py test_technicalTask.py
  4. In command line it should show that all test have passed.
