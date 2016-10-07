import core_av
import os

## import signature database
sig_db = core_av.get_signature_db()
#############

def import_file(file_path):
    file = file_path.split('/')[1]
    print file
    signature = core_av.hash_block(file_path)
    if signature in sig_db:
        print '\tdb have had this virus'
        return
    else:
        db = open('signature_db.txt','a')
        db.write(signature + " " + file + "\n")
        db.close()
        print '\timport successfull'

def import_folder(path = 'virus_samples_import'):
    if not os.path.isdir(path):
        print 'not a path'
        return
    else:
        viruses = os.listdir(path)
        for virus in viruses:
            if virus[-3:] == '.py':
                import_file(path+'/'+virus)

def main():   
    import_folder()

if __name__ == '__main__':
    main()

