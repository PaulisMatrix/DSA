import os,time,logging,enum,datetime

#enum for size units
class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4

def convert_unit(size_in_bytes,unit):
    #Convert the size from bytes to other units like KB, MB or GB
    if unit == SIZE_UNIT.KB:
       return size_in_bytes/1024
    elif unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
    elif unit == SIZE_UNIT.GB: 
       return size_in_bytes/(1024*1024*1024)
    else:
       return size_in_bytes

'''
To search in subdirectories, we are using the os.walk() function. 
It recursively yields a 3-tuple (dirpath, dirnames, filenames),
where dirpath is the path to the current directory, dirnames is a list of the names 
of the subdirectories in the current directory and filenames lists the regular files in the current directory.
'''
def getInfo(root_dir,logger):
    for curdir, _ , files in os.walk(root_dir):
        notFound = True
        deleted_size = 0
        #print("Searching in current directory:{}".format(curdir))
        for filenames in files:
            file_name = os.path.join(curdir, filenames)
            ext = os.path.splitext(file_name)[-1].lower()
            if os.path.isfile(file_name):
                if ext in {'.png','.jpg','.jpeg'}:
                    #if os.path.getmtime(file_name) < (now - 30 * 86400):
                        #print(fname)
                    notFound=False
                    size = convert_unit(os.path.getsize(file_name),SIZE_UNIT.MB)
                    #logger.info('File {} is of size:{0:.3f} MB to be deleted!'.format(file_name,size))
                    deleted_size+=size
                    #os.remove(file_name) #remove the file        
        if notFound:
                logger.info("No files to be deleted in the %s directory"%curdir)
        else:
            logger.info('%.3f MB data deleted from the %s directory'%(deleted_size,curdir))

if __name__=="__main__":
    root_dir='C://Users//1999y//Desktop//practice'
    now = time.time()
    t = datetime.datetime.now().strftime('%y%m%d')
    log_file = 'cleanup-'+t+'.log'
    log_format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename = log_file,
                    filemode = "a",
                    format = log_format, 
                    level = logging.INFO)
    logger = logging.getLogger()
    getInfo(root_dir,logger)
