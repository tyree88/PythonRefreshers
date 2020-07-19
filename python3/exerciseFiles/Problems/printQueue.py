"""
Model how a print job takes paper out a print queue
Create three clases for this 
REQUIREMENTS
- First requirement is a job class that called print queue 
- Second is class called job each job can have 1 to 10 pages (should havea print pages method and check complete)
- Thrid is a printer class using the Queues deque method to take the first job off the queue item 
APPROACH
- The job class has information about how many pages are left in the job
- if we print a page from the job, we decrement the page count
- if the job hits 0 then it is complete 
- The printer class has information about the job its working on but needs the next job - cant get an empty queue
- have to make the jobs talk to each other with the printqueu and printcomplete
"""

import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == None


class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)
        super().__init__()

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:
    def __init__(self):
        super().__init__()
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:  # Queue is empty
            return "No more jobs to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()
        if job.check_complete():
            return "Printing complete"
        else:
            return " An error occurred"


def main():
    job = Job()
    printer_q = Queue()
    printer = Printer()
    printer_q.enqueue(job)
    print(printer_q.items)
    printer.get_job(printer_q)
    print(printer_q.items)


if __name__ == "__main__":
    main()
