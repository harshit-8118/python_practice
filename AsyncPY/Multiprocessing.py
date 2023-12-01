from multiprocessing import Process
from time import sleep

def fun(num = 2):
    sleep(.1)
    print(num ** 2)

'''
# race condition arises
def fn1(fs, fst):
    for i in fst:
        sleep(.001)
        fs.write(i)


def fn2(fs, fst):
    for i in fst:
        sleep(.001)
        fs.write(i)
'''

if __name__ == "__main__":
    procs = []
    for i in range(5):
        procs.append(Process(target=fun, args=(i + 1, )))

    # print(procs)
    for proc in procs:
        proc.start()

    sleep(.11)
    print('hi')
    for proc in procs:
        proc.join()

    # below code will generate race-condition
    fst = '''
    Artificial Intelligence and Ethics:
    Artificial Intelligence (AI) has become an integral part of various industries, revolutionizing the way we live and work. As AI     systems advance, concerns about ethical considerations and responsible use have gained prominence. Issues such as bias in algorithms, privacy concerns, and the potential impact on employment have sparked debates worldwide.
    Renewable Energy Transition:
    The global push toward renewable energy sources represents a critical response to climate change and the need for sustainable energy solutions. Countries worldwide are investing heavily in wind, solar, and other renewable technologies to reduce dependence on fossil fuels. 
    Mental Health in the Digital Age:
    The digital age has brought unprecedented connectivity and convenience, but it has also given rise to unique challenges, particularly in the realm of mental health. Increased screen time, social media pressures, and the constant flow of information can contribute to stress and anxiety. 
    '''
    
    # with open('this.txt', 'w') as fs:
    #     procs.append(Process(target=fn1, args=(fs, fst,)))
    #     procs.append(Process(target=fn2, args=(fs, fst,)))
    #     for proc in procs:
    #         proc.start()
    #     for proc in procs:
    #         proc.join()