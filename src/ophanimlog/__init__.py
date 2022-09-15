import datetime
from colorama import init, Fore, Back

init(autoreset=True)

'''
def addEnd(text, start, previusManual):
    missing=100-start-1-4
    if previusManual:
        missing-=1
    for i in range(1,missing):
        text+=' '
    text+=f'║'

    return text
'''


def parseText(text, len):
    text=text.replace("╔","").replace("╝","")
    start=0
    final=""
    first = True
    for c in text:

        if first:
            if start % (len-5) == 0 and start != 0:
                final+="\n║\t"
                start=0
                first = False

            if c == "\n":
                start=0
                final+="\n║\t"
                c=''
                first = False
                continue

            final+=c
            start+=1


        else:
            if start % len == 0 and start != 0:
                final+="\n║\t"
                start=0

            if c == "\n":
                start=0
                final+="\n║\t"
                c=''
                continue

            final+=c
            start+=1

    return final



def log(text="NO TEXT ENTERED", log_type="UNCATEGORIZED", len=88, path="logs/log.txt"):
    try:
        with open (path, "a+", encoding="utf-8") as f:  
            try: #tries to convert text if it's not a string
                text = text.text
            except:
                try:
                    text = text
                except Exception as e:
                    text=f"Couldn't log, invalid error message format:\n\nError message:\n{e}"
                    print(text)
                    log(text=text, log_type="AUTO_TEXT_TYPE_ERROR", len=88, path=path)
                    return -1


            finalText = parseText(text, len) #parse text to the selected len

            time = datetime.datetime.now()
            finalime = parseText(f"[{str(time)}]", len) #parse text to the selected len
            finalLog_type = parseText(log_type, len)

            topBanner='╔'
            for i in range(1,len+10):
                topBanner+='═'
            topBanner+='╗'

            botBanner='╚'
            for i in range(1,len+10):
                botBanner+='═'
            botBanner+='╝'

            midBanner='╠'
            for i in range(1,len+10):
                midBanner+='═'
            midBanner+='╣'

            f.write(f'''
{topBanner}
║ Time:\t {finalime}
║ Type:\t {finalLog_type}
{midBanner}
║ Error: {finalText}
{botBanner}''')

            f.close()


        return 0


    except Exception as e:
        print(f"Couldn't find log file, make sure the directory specified is the correct one, currently selected directory: {path}.\n\nError message:\n{e}")
        return -1





def printLog(number=0, log_type="", path="logs/log.txt"):
    with open (path, "r+", encoding="utf-8") as f:
        logs=f.read()
        if number == 0 and log_type == "": #prints all the logs
            print(f'''░▒▓ SAVED LOGS ▓▒░\n''') 
            for item in logs.split("╔")[1:]:
                    if f"Type:\t AUTO_" in item:
                        print(Fore.YELLOW+"╔"+item) #makes auto logs be printed in yellow
                    else:
                        print("╔"+item)
            return 0

        elif number == 0: #prints all the logs give the log_type
            try:
                similarLogs=''
                similarCount=0
                print(f'''░▒▓ LOGS {log_type} ▓▒░\n''') 
                for item in logs.split("╔")[1:]:
                    if f"Type:\t {log_type}\n" in item:
                        if "Type:\t AUTO_" in item:
                            print(Fore.YELLOW+"╔"+item) #makes auto logs be printed in yellow
                        else:
                            print("╔"+item)
                    elif log_type in item:
                        if "Type:\t AUTO_" in item:
                            similarLogs+=Fore.YELLOW+"╔"+item+Fore.WHITE
                        else:
                            similarLogs+="╔"+item
                        similarCount+=1
                
                if similarCount!=0:
                    print(f'''\n\n░▒▓ {similarCount} SIMILAR LOGS FOUND CONTAINING THE WORD {log_type} ▓▒░\n{similarLogs}''')
                        

                return 0
            except Exception as e:
                num = len(logs.split("╔"))
                text=f"Couldn't find the log you selected ({number} {log_type}).\nThere are only {num-1} logs available, so make sure that you've entered a coherent number.\n\nError message:\n{e}"
                print(text)
                log(text=text, log_type="AUTO_LOG_ACCESS_ERROR", len=88, path=path)
                return -1

        else:

            if log_type=="":
                try:
                    print(f'''░▒▓ LOG NUMBER {number} ▓▒░\n''') 
                    if "Type:\t AUTO_" in logs.split("╔")[number]:
                        print(Fore.YELLOW+"╔"+logs.split("╔")[number])
                    else:
                        print("╔"+logs.split("╔")[number])
                    return 0
                except Exception as e:
                    num = len(logs.split("╔"))
                    text=f"Couldn't find the log you selected ({number}).\nThere are only {num-1} logs available, so make sure that you've entered a coherent number.\n\nError message:\n{e}"
                    print(text)
                    log(text=text, log_type="AUTO_LOG_ACCESS_ERROR", len=88, path=path)
                    return -1

            else:
                try:
                    print(f'''░▒▓ LOG TYPE {log_type} NUMBER {number} ▓▒░\n''') 
                    counter=0
                    for item in logs.split("╔")[1:]:
                        if f"Type:\t {log_type}\n" in item:
                            counter+=1 
                        if counter == number:
                            if f"Type:\t AUTO_" in item:
                                print(Fore.YELLOW+"╔"+item)
                            else:
                                print("╔"+item)
                            break

                    return 0
                except Exception as e:
                    num = len(logs.split("╔"))
                    text=f"Couldn't find the log you selected ({number}).\nThere are only {num-1} logs available, so make sure that you've entered a coherent number.\n\nError message:\n{e}"
                    print(text)
                    log(text=text, log_type="AUTO_LOG_ACCESS_ERROR", len=88, path=path)
                    return -1



def delLog(number=0, path="logs/log.txt"):
    with open (path, "r+", encoding="utf-8") as f:
        logs=f.read()

    if number == 0: #deletes all the logs
        with open (path, "w+", encoding="utf-8") as f:
            print(f'''░▒▓ ALL LOGS HAVE BEEN DELETED ▓▒░
{logs}''') 
            return 0

    else:
        try:
            i = 1
            logs.split("╔")[number]
            with open (path, "w+", encoding="utf-8") as f:
                for item in logs.split("╔")[1:]:
                    if i != number:
                        f.write("╔"+item)
                    else:
                        print(f"░▒▓ DELETED LOG NUMBER {i} ▓▒░\n\n╔{item}")
                    i+=1

            return 0

        except Exception as e:
            num = len(logs.split("╔"))
            text=f"Couldn't find the log you selected ({number}).\nThere are only {num-1} logs available, so make sure that you've entered a coherent number.\n\nError message:\n{e}"
            print(text)
            log(text=text, log_type="AUTO_LOG_DEL_ERROR", len=88, path=path)
            return -1