"""
Author: 
"""
import multiprocessing
import time 
variables_in = []
for x in range(1,13):
    variables_in.append([x,0.25])
    variables_in.append([x,0.50])
    variables_in.append([x,0.75])
    variables_in.append([x,1])

def mes_a_mes(mes_f):
    mes = mes_f[0]
    f = mes_f[1]
    time.sleep(1)
    print(mes,f)


def multithread(threads):
    pool_tasks = multiprocessing.Pool(processes=threads)
    pool_tasks.map(mes_a_mes, variables_in)
    return pool_tasks


if __name__ == '__main__':

    p = multithread(4)
