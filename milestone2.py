import logging  
import yaml
import time
import datetime
import csv
logging.basicConfig(filename = "milestone2.txt",
                    filemode = "w",
                    format='%(asctime)s.%(process)d;%(message)s',
                    datefmt=('%Y-%m-%d %H:%M:%S'),
                    level=logging.INFO)  

#time Function  
def TimeFunction(Task,Func_Input,Exe_Time):
    logging.info('M1A_Workflow.Task'+Task+' Executing TimeFunction ('+Func_Input+','+Exe_Time+')' )
    exe=int(Exe_Time)
    time.sleep(exe)
def dataLoad(filename):
    with open('Milestone2A_DataInput1.csv','r')as filedescriptor:
        data.load(filedescriptor)
def TimeFunction1(Task,Func_Input,Exe_Time):
    logging.info('M1A_Workflow.FlowA.Task'+Task+' Executing TimeFunction ('+Func_Input+','+Exe_Time+')' )
    exe=int(Exe_Time)
    time.sleep(exe)
#opening File
with open('Milestone1A.yaml','r') as file:
    data=yaml.full_load(file)
    d=data.get('M1A_Workflow')
    T=d.get('Type')
    E=d.get('Execution')
    if(T=="Flow" and E=="Sequential"):
        logging.info('M1A_Workflow Entry')  
    A=d.get('Activities')
    Task_A=A.get('TaskA')
    T1=Task_A.get('Type')
    if(T1=='Task'):
        logging.info('M1A_Workflow.TaskA Entry')  
    F_IO=Task_A.get('Inputs')
    FInput=F_IO.get('FunctionInput')
    ExeTime=F_IO.get('ExecutionTime')
    TimeFunction('A',FInput,ExeTime)
    logging.info('M1A_Workflow.TaskA Exit') 
    Task_B=A.get('TaskB')
    T2=Task_B.get('Type')
    if(T2=='Task'):
        logging.info('M1A_Workflow.TaskB Entry')  
    F_IO=Task_B.get('Inputs')
    FInputB=F_IO.get('FunctionInput')
    ExeTimeB=F_IO.get('ExecutionTime')
    TimeFunction('B',FInputB,ExeTimeB)
    logging.info('M1A_Workflow.TaskB Exit') 

    #flowA
    Flow_A=A.get('FlowA')
    T_flow=Flow_A.get('Type')
    E_flow=Flow_A.get('Execution')
    if(T_flow=="Flow" and E_flow=="Sequential"):
        logging.info('M1A_Workflow.FlowA Entry')  
    Act_flow=Flow_A.get('Activities')

    Task_C=Act_flow.get('TaskC')
    T3=Task_C.get('Type')
    if(T3=='Task'):
        logging.info('M1A_Workflow.FlowA.TaskC Entry')  
    F_IO_flow=Task_C.get('Inputs')
    FInputC=F_IO_flow.get('FunctionInput')
    ExeTimeC=F_IO_flow.get('ExecutionTime')
    TimeFunction1('C',FInputC,ExeTimeC)
   
    Task_D=Act_flow.get('TaskD')
    T4=Task_D.get('Type')
    if(T4=='Task'):
        logging.info('M1A_Workflow.FlowA.TaskD Entry')  
    F_IO_flow2=Task_D.get('Inputs')
    FInputD=F_IO_flow2.get('FunctionInput')
    ExeTimeD=F_IO_flow2.get('ExecutionTime')
    TimeFunction1('D',FInputD,ExeTimeD)
    logging.info('M1A_Workflow.FlowA.TaskD Exit') 
    logging.info('M1A_Workflow.FlowA.TaskC Exit') 
    logging.info('M1A_Workflow.FlowA Exit') 
    logging.info('M1A_Workflow Exit') 