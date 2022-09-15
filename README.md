# EasyLog
Simple Python module to log your stuff


## Install

The module uses colorama to display automatic logs, which are logs created automatically on exceptions and not manually by the user:

- Linux:
   
      sudo pip3 install colorama
    

- Windows:
   
      pip3 install colorama



## Usage

Download module from github:

        git clone https://github.com/ImAccia/easylog.git
     

Import the module in your script and use it

- Parameters:
   - .log()
      1. text     --> Your text to log (default "NO TEXT ENTERED")
      2. log_type --> The type of the log (some examples might be Error, Warning, Debug etc...) (default "UNCATEGORIZED")
      3. len      --> The lenght of the lines for the logs (default 88)
      4. path     --> The path of the log file (default logs/log.txt)


   - .printLog()
      1. number   --> The log to print (1 for the 1st log etc...) (default 0 --> prints all logs) (you can use negatives to start from the bottom, for example -1 is the last log)
      2. log_type --> The type of the log to print (some examples might be Error, Warning, Debug etc...)
      3. path     --> The path of the log file (default logs/log.txt)


   - .delLog()
      1. number   --> The log to delete (1 for the 1st log etc...) (default 0 --> deletes all logs) (you can use negatives to start from the bottom, for example -1 is the last log)
      2. path     --> The path of the log file (default logs/log.txt)


- Logging

        import easylog
        #Save a log
        easylog.log(text="Sample Log", log_type="DEBUG", len=40)


        #Save another log
        easylog.log(text="Another sample Log", log_type="DEBUG", len=40)


- Printing Logs

        #Print all logs
        easylog.printLog() #0 does the same
     ![Image](<https://i.imgur.com/XEXcRyO.png>)


        #Print the 2nd log
        easylog.printLog(2)
     ![Image](<https://i.imgur.com/D2458Uk.png>)

- Print Logs given Log Type

        #Print all logs with type DEBUG
        easylog.printLog(log_type="AUTO_LOG_ACCESS_ERROR") #0 does the same
     ![Image](<https://i.imgur.com/TVa3XOx.png>)


        #Print the specified log with type DEBUG
        easylog.printLog(1, log_type="AUTO_LOG_ACCESS_ERROR")
     ![Image](<https://i.imgur.com/vYXFkq1.png>)


- Delete Logs

        #Delete the 1st log
        easylog.delLog(1)
     ![Image](<https://i.imgur.com/vQLupuG.png>)


        #Delete all logs
        easylog.delLog() #0 does the same
     ![Image](<https://i.imgur.com/3llv62A.png>)
