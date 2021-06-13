import glob, os, zipfile

def main(sid,dir, exclude_folder=None, exclude_file_pattern=None):
    from _cmd_.send_error import send_err
    file_creation_path = '/mnt/d/'
    path = os.path.dirname(dir)
    file_name = os.path.relpath(dir, path)
    try:
        zp = zipfile.ZipFile(os.path.join(file_creation_path,(file_name+'.zip')),'w')
        txt_file = open(os.path.join(file_creation_path,(file_name+'.txt')),'w')
    except:
        err = 'file creation failed'
        send_err(err, sid)
        return
    ex_folder = tuple(exclude_folder)
    if exclude_file_pattern != []:
        file_pattern = exclude_file_pattern[0]
    else: file_pattern = '*'
    files = [x for x in glob.glob(os.path.join(dir,file_pattern)) if os.path.isfile(x) and not (x.startswith(ex_folder))]
    for file in files:
        # print('1',os.path.relpath(file,path))
        zp.write(file,os.path.relpath(file,path))
        txt_file.write('1'+ os.path.relpath(file,path)+'\n')
    def get_files(dir):
        dirs = [x for x in os.scandir(dir) if x.is_dir() and not (x.name).startswith(ex_folder)]
        for dir_ in dirs:
            # print(dir_.path)
            files = glob.glob(os.path.join(dir_,file_pattern))
            for file in files:
                if not os.path.relpath(file,dir_).startswith(ex_folder):
                    # print('2',os.path.relpath(file,path))
                    zp.write(file,os.path.relpath(file,path))
                    txt_file.write('2'+os.path.relpath(file,path)+'\n')
            get_files(dir_)
    get_files(dir)
    zp.close()
    txt_file.close()
    err = 'job done' # success msg
    send_err(err, sid)