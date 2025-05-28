from configparser import ConfigParser #used to read .ini config files
import os

def config(filename="database.ini", section="postgresql"):
    #filename = the path to the ini file
    #section = the part of the .ini file that config will read 
    filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    filepath = os.path.abspath(filepath)
    parser = ConfigParser()

    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))  
    return db