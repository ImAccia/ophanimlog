# EasyLog
Simple Python module to log your stuff


## Install

The module uses colorama to display automatic logs, which are logs created automatically on exceptions and not manually by the user:

- Linux:
   
      sudo pip3 install colorama
    

- Windows:
   
      pip3 install colorama



## Usage

Download file from github:

        git clone https://github.com/ImAccia/easylog.git
     

Import the module in your script and use it

        import easylog
        #Save a log
        easylog.log(text="Sample Log", log_type="DEBUG", len=40)


        #Save another log
        easylog.log(text="Another sample Log", log_type="DEBUG", len=40)


        #Print all logs
        easylog.printLog() #0 does the same


        #Print the 2nd log
        easylog.printLog(2)


        #Print all logs with type DEBUG
        easylog.printLog(log_type="AUTO_LOG_ACCESS_ERROR") #0 does the same


        #Print the specified log with type DEBUG
        easylog.printLog(1, log_type="AUTO_LOG_ACCESS_ERROR")


        '''
        #Delete the 1st log
        easylog.delLog(1)


        #Delete all logs
        easylog.delLog() #0 does the same
        '''
