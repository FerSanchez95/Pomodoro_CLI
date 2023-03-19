#!/usr/bin/env python3
try:
    from plyer import notification
except:
    print("'plyer' must be installed. Please try 'pip install plyer' or 'python -m pip install plyer'")
import time
import os
import json

def main():

    def language_selection(select):
        if select == "eng":
            actual_lang = language["eng"]
            return actual_lang
        elif lang_selected == "esp":
            actual_lang = language["esp"]
            return actual_lang
        else:
            print("Defautl language english selected")
            actual_lang = language["eng"]
            return actual_lang
    
    def Notification(N_title, N_message): 
        path = os.getcwd()
        path_icon = path + "/icon.ico"
        notification.notify(
            title = N_title,
            message = N_message,
            app_name = "Pomodoro CLI",
            app_icon = path_icon,
            ticker= "algo hace esto...",
            timeout = 30,
            hints = {}
    )
    
    def progress_bar(part, total, lenght):
        frac = part/total
        completed = int(frac*lenght)
        missing = lenght-completed
        bar = f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
        return bar

    json_file = open('lang.json').read()
    language = json.loads(json_file)
    os.system('clear')
    lang_selected = str(input("\nLanguage (eng/esp): "))    
    lang_sel = language_selection(lang_selected) 
    os.system('clear')

    print(f"\n{lang_sel['welcome_msg']}\n")
    print(f">>> {lang_sel['message_url']}{lang_sel['pomodoro_url']}\n")
    intervals_reps = int(input(f"{lang_sel['interval_msg']}: "))
    minutes = int(input(f"{lang_sel['input_mins']}: "))
    rest = int(input(f"{lang_sel['input_rest']}: "))
    true_lenght = int(30)

    if 0 <=minutes <= 61 & 0<=rest<=61:
        print(f"{lang_sel['error1']}")
        return 0

    cycles = minutes*60
    rest_cycles = rest*60
    t_zero = time.perf_counter()
    
    for i in range(intervals_reps):
        #jt = job time; ttl = title; msg = message.
        initial_jt_ttl = f"{lang_sel['Initial_JT_Title']}"
        initial_jt_msg = f"{lang_sel['Initial_JT_Message']} {i+1}."
        Notification(initial_jt_ttl, initial_jt_msg)
        
        print("\n")
        for j in range(cycles):
            time.sleep(1.0)
            t_interval = time.perf_counter()
            t_elapsed_s = int(t_interval-t_zero)
            t_elapsed = f"{t_elapsed_s} seg" # time formated for seconds
            if t_elapsed_s >= 60:
                t_elapsed_m = int((t_elapsed_s+1)/60)
                t_elapsed = f"{t_elapsed_m} mins." 
            print(f"{progress_bar(j,cycles,true_lenght)}  T- {t_elapsed}", end='\r')

        print(f"\n{lang_sel['Final_JT_Pmessage_1']} {i+1} {lang_sel['Final_JT_Pmessage_2']}\n")
        final_jt_ttl = f"{lang_sel['Final_JT_title']}"
        final_jt_msg = f"{lang_sel['Final_JT_message_1']} {i+1}. {lang_sel['Final_JT_message_2']} {i+1}."
        Notification(final_jt_ttl, final_jt_msg)

        t_rest_zero = time.perf_counter()
        for k in range(rest_cycles):
            time.sleep(1.0)
            t_rest_interval = time.perf_counter()
            t_rest_elapsed_s = int(t_rest_interval-t_rest_zero)
            t_rest_elapsed = f"{t_rest_elapsed_s} segs."
            if t_rest_elapsed_s >= 60:
                t_rest_elapsed_m = int((t_rest_elapsed_s+1)/60)
                t_rest_elapsed = f"{t_rest_elapsed_m} mins. " 
            print(f"{progress_bar(k, rest_cycles, true_lenght)}  T- {t_rest_elapsed}", end='\r')
        
        print(f"\n{lang_sel['Final_RT_Pmessage_1']} {i+1} {lang_sel['Final_RT_Pmessage_2']}\n")
        final_rt_ttl = f"{lang_sel['Final_RT_title']}"
        final_rt_msg = f"{lang_sel['Final_RT_message']} {i+1}."
        if intervals_reps >> 1:
            fianl_rt_msg = final_rt_msg + lang_sel['Interval_reboot']
        Notification(final_rt_ttl, final_rt_msg)

    print(f"{lang_sel['Completed_msg']}\n")
    final_ttl = f"{lang_sel['Completed_msg']}"
    final_msg = f"{lang_sel['Final_msg']}"
    Notification(final_ttl, final_msg)
    return 0
        
if __name__=='__main__':
    main()
