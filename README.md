# OphanimLog
Simple Python module to log your stuff


## Install

The module uses colorama to display automatic logs, which are logs created automatically on exceptions and not manually by the user.

- Linux:
   
      sudo pip3 install ophanimlog
    

- Windows:
   
      pip3 install ophanimlog



## Usage

Import the module in your script and use it

- Parameters:
   - .log()
      - text     --> Your text to log (default "NO TEXT ENTERED")
      - log_type --> The type of the log (some examples might be Error, Warning, Debug etc...) (default "UNCATEGORIZED")
      - len      --> The lenght of the lines for the logs (default 88)
      - path     --> The path of the log file (default logs/log.txt)


   - .printLog()
      - number   --> The log to print (1 for the 1st log etc...) (default 0 --> prints all logs) (you can use negatives to start from the bottom, for example -1 is the last log)
      - log_type --> The type of the log to print (some examples might be Error, Warning, Debug etc...)
      - path     --> The path of the log file (default logs/log.txt)


   - .delLog()
      - number   --> The log to delete (1 for the 1st log etc...) (default 0 --> deletes all logs) (you can use negatives to start from the bottom, for example -1 is the last log)
      - path     --> The path of the log file (default logs/log.txt)


- Logging

        import ophanimlog
        #Save a log
        ophanimlog.log(text="Sample Log", log_type="DEBUG", len=40)


        #Save another log
        ophanimlog.log(text="Another sample Log", log_type="DEBUG", len=40)


- Printing Logs

        #Print all logs
        ophanimlog.printLog() #0 does the same
     ![Image](<https://i.imgur.com/XEXcRyO.png>)




        #Print the 2nd log
        ophanimlog.printLog(2)
     ![Image](<https://i.imgur.com/D2458Uk.png>)




- Print Logs given Log Type

        #Print all logs with type DEBUG
        ophanimlog.printLog(log_type="AUTO_LOG_ACCESS_ERROR") #0 does the same
     ![Image](<https://i.imgur.com/TVa3XOx.png>)




        #Print the specified log with type DEBUG
        ophanimlog.printLog(1, log_type="AUTO_LOG_ACCESS_ERROR")
     ![Image](<https://i.imgur.com/vYXFkq1.png>)





- Delete Logs

        #Delete the 1st log
        ophanimlog.delLog(1)
     ![Image](<https://i.imgur.com/vQLupuG.png>)




        #Delete all logs
        ophanimlog.delLog() #0 does the same
     ![Image](<https://i.imgur.com/3llv62A.png>)






## TIP

To make it so that logs get saved to a different file dynamically on each new day you could use this snippet

      import ophanimlog as log
      import time
      from datetime import datetime

      stamp = time.time()
      dt_obj = datetime.fromtimestamp(stamp).strftime('%d-%m-%y')
      log.log(path=f"log{str(dt_obj)}.txt")
