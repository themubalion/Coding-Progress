class entries:
    def __init__(self,topic,inittime,fintime,date,language):
        self.topic = topic
        self.inittime = inittime
        self.fintime = fintime
        self.date = date
        self.lang = language

fnamelist = {'python':'Python-Progress.txt','css':'CSS-Progress.txt','js':'JavaScript-Progress.txt','web':'WebDev-Progress.txt'}

def func_entry():
    topic = input('Enter the topic you learned today. \n')
    time_init = input('Enter the start of the time. \n')
    time_final = input('Enter the time you finished your Topic. \n')
    date = input('Enter present date.\n')
    lang = input('The language where the topic belongs.\n')
    if ':' not in topic and time_init and time_final and date and lang:
        if 'python' in lang.lower():
            thand = open(fnamelist['python'],'a')
        elif 'css' in lang.lower():
            thand = open(fnamelist['css'],'a')
        elif 'javascript' or 'js' in lang:
            thand = open(fnamelist['js'],'a')
        else:
            thand = open('other-progresses.txt','a')
    else:
        print('Please do not insert colon ":" in the input box')


    entry = entries(topic,time_init,time_final,date,lang)

    initial_entry = f"Topic: {entry.topic}\nFrom: {entry.inittime}\nTo:{entry.fintime}\nDate:{entry.date}\nLanguage:{entry.lang}\n\n"

    final_entry = thand.write(initial_entry)
    thand.close()
func_entry()