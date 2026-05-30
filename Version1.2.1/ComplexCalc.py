import tkinter as tk
import math
from math import sqrt, cbrt
import cmath
import sys
import os
import time
import inspect
import platform

OS = platform.system()

inf = math.inf
pi = math.pi
e = math.e
tau = math.tau

answer_number = 0

def get_image_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            icon_path = os.path.join(os.path.dirname(sys.executable), relative_path)
        else:
            # Running as Python script
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
        return icon_path
    except Exception as e:
        #print(f"Icon load error: {e}")
        pass
# Usage
#config_path = get_resource_path('config/settings.json')
if OS == 'Windows':
    try:
        image_path = get_image_path('CompCalcIcon.ico')
        #print('Image path is', image_path)
    except Exception as e:
        #print('Error trying to get the icon:', e)
        pass

elif OS == 'Darwin':
    try:
        image_path = get_image_path('CompCalcIcon.icns')
        #print('Image path is', image_path)
    except Exception as e:
        #print('Error trying to get the icon:', e)
        pass

elif OS == 'Linux':
    def get_resource_path(relative_path):
        """Get absolute path to resource, works for dev and for bundled."""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = os.path.dirname(os.path.abspath(__file__))
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


    image_path = get_resource_path('CompCalcIcon.png')

def hasvars(string):
    boolean = False
    for i in range(len(string)):
        if not string[i].isnumeric():
            boolean = True
            break
    return boolean

def haseq(string):
    boolean = False
    
    symbols = ['+', '-', '/', '*', '^', '&', '%', '~', '|', '=', '[', ']', '{', '}', '<', '>', '!', ',']
    for i in range(len(symbols)):
        string = string.replace(symbols[i], ' '+symbols[i]+' ')
    string = string.replace('(', '( ')
    string = string.replace(')', ' )')
    string = string.replace('*  *', '**')
    string = string.replace('/  /', '//')
    string = string.replace('=  =', '==')
    string = string.replace('>  =', '>=')
    string = string.replace('<  =', '<=')
    string = string.replace('!  =', '!=')
    words = string.split(' ')
    
    for i in range(len(words)):
        if words[i] == '=':
            boolean = True
            break
    return boolean

def isvar(string):
    string = string.replace('_', '')
    return string.isalpha()

def variable_handling(string, execute=True):
    global all_vars
    words = string.split(' ')
    keys = all_vars.keys()
    for i in range(len(words)):
        if isvar(words[i]):
            words[i] = 'all_vars["'+words[i]+'"]'
    command = ''
    for i in range(len(words)):
        command += words[i]
    ##print(command)
    if execute:
        exec(command)
    
    variables.delete('1.0', tk.END)
    keys = list(all_vars.keys())
    for i in range(len(keys)):
        variables.insert(tk.END, f'{keys[i]} = {all_vars[keys[i]]}\n')
    variables.see(tk.END)
    answer.config(text=str(entry.get()))
    
def roots(number, root):
    c = number
    b = root
    try:
        begin = time.time()
        a = 0
        if b < 0:
            posroot = -b
        else:
            posroot = b
        d = [100000, 10000, 1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001, 0.0000000000001, 0.00000000000001]
        for i in range(len(d)):
            if time.time()-begin > 0.02:
                break
            w = d[i]
            while math.pow(a, posroot) <= c:
                if time.time()-begin > 0.05:
                    break
                a = a+w
            a = a-w
            continue
        a = round(a, 14)
        if b < 0:
            a = 1/a
        return(str(a))
    except OverflowError:
        ##print('Number or root too large!')
        return 'Number or root too large!'
        

def on_key_press(event):
    global entry, answer, history, variables, all_vars, answer_number
    try:
        text = variables.get('1.0', 'end')
        lines = text.splitlines()
        all_vars = {}
        for i in range(len(lines)):
            try:
                lines[i] = lines[i].replace(' ', '')
                parts = lines[i].split('=')
                #if parts[0] != 'pi' and parts[0] != 'e' and parts[0] != 'tau' and parts[0] != 'inf':
                all_vars[parts[0]] = eval(parts[1])
            except Exception as e:
                ##print('Variable Error:', e)
                pass
            
        all_vars['pi'] = math.pi
        all_vars['e'] = math.e
        all_vars['tau'] = math.tau
        all_vars['inf'] = math.inf
        
        if event.keysym.lower() == 'return':
            
            if haseq(str(entry.get())):
                num = str(entry.get())
                history.config(state='normal')
                history.insert(tk.END, num+'\n')
                history.see(tk.END)
                answer.config(text=num)
                history.config(state='disabled')
                
                string = ' '+str(entry.get())+' '
                keys = list(all_vars.keys())
                symbols = ['+', '-', '/', '*', '^', '&', '%', '~', '|', '=', ',']
                for i in range(len(symbols)):
                    string = string.replace(symbols[i], ' '+symbols[i]+' ')
                string = string.replace('(', '( ')
                string = string.replace(')', ' )')
                string = string.replace('^', '**')
                ##print(string)
                variable_handling(string)
                
            else:
                num = answer_number
                if '<compiled_function' in num or '<function' in num: # <function roots at 0x70256e56b7e0> or <compiled_function roots at 0x77d976d4c740>
                    parts = num.split(' ')
                    func = parts[1]
                    num = 'Args: '+str(inspect.signature(eval(func)))
                    num = num.replace(', /', '')
                
                elif '<built-in function' in num:
                    parts = num.split(' ')
                    func = parts[2]
                    func = func[:-1]
                    num = 'Args: '+str(inspect.signature(eval(func)))
                    num = num.replace(', /', '')
                
                elif '<module' in num:
                    parts = num.split(' ')
                    func = str(parts[1])
                    if func == "'time'" or func == "'tkinter'" or func == "'inspect'" or func == "'sys'" or func == "'os'":
                        num = 'Invalid'
                    else:
                        num = 'Python module '+func
                history.config(state='normal')
                history.insert(tk.END, str(num)+'\n')
                history.see(tk.END)
                answer.config(text=num)
                history.config(state='disabled')
            
            
            
        elif event.keysym.lower() == 'delete':
            answer.config(text='0')
            entry.delete(0, tk.END)
        else:
            string = ' '+str(entry.get())+' '
            keys = list(all_vars.keys())
            symbols = ['+', '-', '/', '*', '^', '&', '%', '~', '|', '=', '[', ']', '{', '}', '<', '>', '!', ',']
            for i in range(len(symbols)):
                string = string.replace(symbols[i], ' '+symbols[i]+' ')
            string = string.replace('(', '( ')
            string = string.replace(')', ' )')
            string = string.replace('*  *', '**')
            string = string.replace('/  /', '//')
            string = string.replace('=  =', '==')
            string = string.replace('>  =', '>=')
            string = string.replace('<  =', '<=')
            string = string.replace('!  =', '!=')
            
            ##print(string)
            if haseq(string):
                variable_handling(string, False)
                
            else:
                for i in range(len(keys)):
                    string = string.replace(' '+keys[i]+' ', ' '+str(all_vars[keys[i]])+' ')
                ##print(string)
                t = eval(string)
                ##print(num)
                num = str(t)
                answer_number = num
                if '<compiled_function' in num or '<function' in num: # <function roots at 0x70256e56b7e0> or <compiled_function roots at 0x77d976d4c740>
                    parts = num.split(' ')
                    func = parts[1]
                    num = 'Args: '+str(inspect.signature(eval(func)))
                    num = num.replace(', /', '')
                
                elif '<built-in function' in num:
                    parts = num.split(' ')
                    func = parts[2]
                    func = func[:-1]
                    num = 'Args: '+str(inspect.signature(eval(func)))
                    num = num.replace(', /', '')
                
                elif '<module' in num:
                    parts = num.split(' ')
                    func = str(parts[1])
                    if func == "'time'" or func == "'tkinter'" or func == "'inspect'" or func == "'sys'" or func == "'os'":
                        num = 'Invalid'
                    else:
                        num = 'Python module '+func
                
                answer.config(text=num)
            
            
                
                    
                
            #print(all_vars)
            
    except Exception as e:
        #print('Invalid syntax!')
        #print('Error:', e)
        if str(entry.get()) == '':
            answer.config(text='0')
        elif '=' in str(entry.get()):
            answer.config(text=str(entry.get()))
        else:
            answer.config(text='Invalid')

all_vars = {'pi': pi, 'e': e, 'tau': tau, 'inf': inf}


Root = tk.Tk()
Root.title("ComplexCalc V1.2.1")
Root.geometry("300x310")
if OS == 'Windows':
    try:
        Root.iconbitmap(image_path)
    except Exception as e:
        #print('Error:', e)
        pass
elif OS == 'Darwin' or OS == 'Linux':
    try:
        icon_image = tk.PhotoImage(file=image_path)
        Root.iconphoto(True, icon_image)
    except Exception as e:
        #print('Error:', e)
        pass
    

entry = tk.Entry(Root, width=300)
entry.pack(padx=2, pady=10)
answer = tk.Label(Root, text='0')
answer.pack(pady=2)
history_label = tk.Label(Root, text='History')
history_label.pack(pady=2)
history = tk.Text(Root, height=5, width=300)
history.pack(padx=2, pady=2)
history.config(state='disabled')
variables_label = tk.Label(Root, text='Variables')
variables_label.pack(pady=2)
variables = tk.Text(Root, height=6, width=300)
variables.pack(padx=2, pady=2)
#button = tk.Button(root, text="Create Variable", command=var)
#button.pack(pady=2)

keys = list(all_vars.keys())
for i in range(len(keys)):
    variables.insert(tk.END, f'{keys[i]} = {all_vars[keys[i]]}\n')

# Bind key press and release events to the root window
Root.bind("<KeyPress>", on_key_press)

Root.mainloop()