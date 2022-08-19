from sh import pg_dump, pg_restore
import os
import datetime


class BackupFile:
    timestr = datetime.datetime.now().strftime('%d%m%Y-%H%M')

    @classmethod
    def backup(self, comp_level=0):
        with open(f'backup-{BackupFile.timestr}.dump', 'w') as f:
            pg_dump('flask', '-Fc', '-c', '--if-exists', '-Z', comp_level, _out=f)
        return None

    @classmethod
    def restore(self, time):
        cwd = os.getcwd()
        archive = f"{cwd}/backup-{time}.dump"
        try:
            pg_restore('-c', '--if-exists', '-d', 'flask', archive)
        except Exception as e:
            print(e)
            return "Restoration failed. Ensure that DB exits"
        return None
