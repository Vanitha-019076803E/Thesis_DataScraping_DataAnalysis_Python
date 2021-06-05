import patoolib
import glob
import gzip, io
import csv

def extract_func:
    contents = []

    #patoolib.extract_archive("/mnt/ssd1/pastebin/circl_data/codepad.org/2015/10.tar",outdir="/home/vanitha/codepad_org_2015")

    ZIPFILES='/home/vanitha/codepad_org_2015/home/rommelfs/pystemon/archive/codepad.org/2015/10/14/*'

    filelist = glob.glob(ZIPFILES)

    for gzfile in filelist:
        print("#Starting " + gzfile) 
        with gzip.open(gzfile, 'rb') as f:
            contents.append(f.read())

    #patoolib.extract_archive("/mnt/ssd1/pastebin/circl_data/codepad.org/2015/12.tar",outdir="/home/vanitha/codepad_org_2015")
    i = 16
    n = 32

    while i < n:
        ZIPFILES1='/home/vanitha/codepad_org_2015/home/rommelfs/pystemon/archive/codepad.org/2015/12/'+str(i)+'/*'
        filelist1 = glob.glob(ZIPFILES1)
        for gzfile in filelist1:
            print("#Starting " + gzfile) 
            with gzip.open(gzfile, 'rb') as f:
                contents.append(f.read())
        i = i+1

    file = open('/home/vanitha/codepad_org_2015/codepad_2015.csv', 'w+', newline ='')
    with file:    
        write = csv.writer(file)
        write.writerows(contents)



