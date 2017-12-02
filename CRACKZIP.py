#-*-coding:utf-8-*-
import zipfile
import optparse

def usage():
    print ("CRACK ZIPFILE ver1.0, by johntheripper225\n")
    print("python crack_zipfile.py [-f] zip_filename [-d] dictionnary_filename\n")
    print("[Options]")
    print("-f <zip filename>")
    print ("-d <dictionnary filename>\n")

def lecture(FichierZip, password):
    try:
        FichierZip.extractall(pwd=password)
        return password
    except:
        pass

def main():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest="filename", help="Specify the ZIP FILE")
    parser.add_option("-d", dest="dict_file", help="Specify the dictionnary file")
    (options, args) = parser.parse_args()

    if ((options.filename == None) or (options.dict_file == None)):
        usage()

    else:
        filename = options.filename
        dict_file = options.dict_file

        FichierZip = zipfile.ZipFile(filename)

        PassFile = open(dict_file)
        for word in PassFile.readlines():
            password = word.strip('\n')

            test = lecture(FichierZip, password)

            if test:
                print("[+] Password Found:" + ' ['+ password+']\n')
                break
            else:
                print("[-] Password" ' ['+ password+']' + " is incorrect\n")

if __name__ == "__main__":
    main()
