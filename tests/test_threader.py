from __future__ import print_function
from past.builtins import cmp
from builtins import range
from builtins import object
import sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # add working directory
sys.path.append(os.path.abspath("../util")) # add relative path

from sutils.threader import api, Designator, IterDecouple

if __name__ == "__main__":

    def worker(q):
        while not q.empty():
            next_job = q.get()
            print('Processing job:', next_job.description)

    class Job(object):
        def __init__(self, priority, description):
            self.priority = priority
            self.description = description
            print('New job:', description)
        def __cmp__(self, other):
            return cmp(self.priority, other.priority)

    #api.spawn = True
    #q = PriorityQueue()
    q = Designator()
    # https://pymotw.com/2/Queue/
    q.put( Job(10, 'Low-level job 1') )
    q.put( Job(1, 'Important job 1') )
    q.put( Job(10, 'Low-level job 2') )
    q.put( None)
    q.put( Job(3, 'Mid-level job') )
    q.put( Job(1, 'Important job 2') )
    q.put( Job(10, 'Low-level job 3') )
    """
    print len(q)
    for i in q:
        print i.description
    print len(q)
    """
    import multiprocessing as m
    import threading as th

    #processes = [m.Process(target=worker,args=(q,)) for i in xrange(3)]
    processes = [th.Thread(target=worker,args=(q,)) for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    #print len(q)

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()

    def handler_timeout(signum, frame):
        raise Exception("Function taking too long")

    #import signal
    #signal.signal(signal.SIGALRM, handler_timeout)

    def demo_decouple_iter():
        """

        :return:
        """
        import time, random

        class SimulateProcess(object):
            def __init__(self, value, time_processing):
                self.value = value
                self.time_processing = time_processing
                self._creation_time = time.time()

            def process(self):
                time.sleep(self.time_processing)
                return self

            __call__ = process

            def __str__(self):
                return str(self.value)

        def simulate_iterable(max_time=1, no_itmes = 10):
            """
            Simulates iterable that gives data un-evenly in time,
            fast or really slow in some cases.

            :param max_time: maximum random time to simulate process
            :param no_itmes: number of processes to create
            :return: iterator
            """
            for order in range(no_itmes):
                tp = random.random() * max_time
                yield SimulateProcess(order, tp), tp

        def simulate_consumer(myiter, call = False, stop_in= None, test_name = None):
            """
            Simulates iterator consumption. The idea is to simulate a process
            that wants to get data as fast as possible, faster is better.

            :param myiter: iterator of SimulateProcess instances
            :param buffsize: buffer size
            :return (No_items, time_ideal, time_normal_for, time_test_for,
                    time_spared_normal, time_loosed_ideal)
            """
            if test_name is None:
                test_name = type(myiter)
            name = " ({})".format(test_name)
            print("Testing for loop {}".format(name))

            worker_times = [0] # time of each worker, 0 is added to simulate empty
            times = [] # time for each epoch
            time_test_for = time.time()  # real process time
            time_epoch_start = time.time() # epoch start time
            for i, (task, time_processing) in enumerate(myiter):
                if stop_in is not None and i == stop_in:
                    myiter.close()
                if call:
                    task()
                time_epoch_end = time.time() # epoch finish time
                time_epoch = time_epoch_end - time_epoch_start # epoch time
                worker_times.append(time_processing) # append real worker time
                times.append(time_epoch) # append for loop epoch time
                print("value: {}, epoch time: {}, worker time: {}"
                      "".format(task,time_epoch,time_processing))
                time_epoch_start = time_epoch_end # update epoch start time

            No_items = len(times) # Number of items
            time_test_for = time.time() - time_test_for
            time_ideal = max(worker_times) # ideal process time
            time_normal_for = sum(worker_times) # not decoupled time
            time_spared_normal = time_normal_for - time_test_for # spared time from normal for loop
            time_loosed_ideal = time_test_for - time_ideal # loosed time from ideal
            print("processed items: ", No_items)
            print("ideal process time: ", time_ideal)
            print("normal for loop time: ", time_normal_for)
            print("tested for loop time{}: ".format(name), time_test_for)
            print("time spared (from normal for): ", time_spared_normal)
            print("loosed time (from ideal):", time_loosed_ideal)
            return (No_items, time_ideal, time_normal_for, time_test_for,
                    time_spared_normal, time_loosed_ideal)

        api.spawn = False
        myiter = list(simulate_iterable())
        stop_in = 3
        decoupled = IterDecouple(myiter, buffsize=0)
        decoupled.call_func = lambda x: (x[0](), x[1])
        decoupled.buffsize = 0 # unlimited

        start_before = 2
        print("\ntest: detached for loop is started {} seconds before\n"
              "".format(start_before))
        decoupled.start()
        time.sleep(start_before)
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(decoupled, stop_in = stop_in)
        if stop_in is None:
            assert No_items == len(myiter)
            assert time_ideal < time_test_for < time_normal_for

        processes = 5
        print("\ntest: detached for loop is started in normal for loop with "
              "{} processes\n".format(processes))
        decoupled.processes = processes
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(decoupled, stop_in = stop_in)
        if stop_in is None:
            assert No_items == len(myiter)
            assert time_ideal < time_test_for < time_normal_for

        print("\ntest: detached for loop is started {} seconds before in "
              "normal for loop with {} processes\n".format(start_before, processes))
        decoupled.processes = processes
        decoupled.start()
        time.sleep(start_before)
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(decoupled, stop_in = stop_in)
        if stop_in is None:
            assert No_items == len(myiter)
            assert time_test_for < time_normal_for # the ideal should be 0

        # disable processes
        decoupled.processes = None

        print("\ntest: detached for loop is started in normal for loop\n")
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(decoupled, stop_in = stop_in)
        if stop_in is None:
            assert No_items == len(myiter)

        print("\ntest: simple list\n")
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(myiter, call=True) # tests: simple list
        if stop_in is None:
            assert No_items == len(myiter)

        print("\ntest: empty iteration\n")
        (No_items, time_ideal, time_normal_for, time_test_for,
        time_spared_normal, time_loosed_ideal) = simulate_consumer(IterDecouple([]))

        """
        # tests repeatability and that processes do not block
        i = 0
        while True:
            signal.alarm(5)  # timeout of 5 seconds
            i+=1
            print("Try",i)
            try:
                simulate_consumer([]) # tests: empty iteration
            except Exception as e:
                signal.alarm(0)
                raise e
        """

    demo_decouple_iter()

