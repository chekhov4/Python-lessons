def logger(path, days):
    def wrapper(func):
        def logging_function(*args, **kwargs):
            import time
            import os
            try:
                os.path.getctime(path)
            except WindowsError:
                with open(path, 'w') as log_file:
                    log_file.write("Function {} called at {}!!!\n".format(func.__name__, time.asctime()))
                log_file.close()
                func(*args, **kwargs)
                return logging_function


            if time.time() -  os.path.getctime(path) < days * 24 * 60 * 60:
                with open(path, 'a') as log_file:
                    log_file.write("Function {} called at {}!!!\n".format(func.__name__, time.asctime()))
            else:
                os.remove(path)
                with open(path, 'w') as log_file:
                    log_file.write("Function {} called at {}!!!\n".format(func.__name__, time.asctime()))
            log_file.close()
            func(*args, **kwargs)
        return logging_function

    return wrapper


@logger('C:\\temp\\log.txt', 1)
def my_function(repeat_time):
    for i in range(repeat_time):
        print('HEY! HEY!')
    return 'printed'


if __name__ == '__main__':
    my_function(3)