import gzip
import os
import subprocess
import datetime

timestr = datetime.datetime.now().strftime('%d%m%Y-%H%M')
# timestr = datetime.datetime.now().strftime('%d%m%Y')
filename = f'backup-{timestr}.dmp'
path = 'D:\\Projets\\Sandbox\\backup\\tmp\\'
local_file_path = path + f'{filename}'


def backup(host, dbname, user, password, file=local_file_path):
    command = f'pg_dump -h {host} -p 5432 -d {dbname} -U {user} -Fc -f {file}'
    print(command)
    popen = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,env={
        'PGPASSWORD': password,
        'PATH': 'C:\Program Files\PostgreSQL\\12\\bin',
        'PGHOST': '127.0.0.1',
        'PGPORT': '5432',
        'SYSTEMROOT': 'C:\\WINDOWS'})

    # for stdout_line in iter(popen.stdout.readline, ''):
    #     f.write(str(stdout_line).encode('utf-8'))

    popen.stdout.close()
    popen.wait()


def compress_file(file):
    src_file = path + f'{file}'
    compressed_file = f"{str(src_file)}.gz"
    with open(src_file, 'rb') as f_in:
        with gzip.open(compressed_file, 'wb') as f_out:
            for line in f_in:
                f_out.write(line)
    return compressed_file


def extract_file(file):
    src_file = path + f'{file}'
    extracted_file, extension = os.path.splitext(src_file)
    print(extracted_file)
    with gzip.open(src_file, 'rb') as f_in:
        with open(extracted_file, 'wb') as f_out:
            for line in f_in:
                f_out.write(line)
    print("decompress ok")
    return extracted_file