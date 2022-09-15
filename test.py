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