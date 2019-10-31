import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())


    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        return sorted([x for x in self.config['tox']['envlist'].replace('\n', ',').split(',') if x !=''])

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        pythons = []
        for sect in self.config.sections():
            try:
                pythons.append(self.config[sect]['basepython'])
            except:
                continue
        return list(set(pythons))
file_class = ToxIniParser('config.txt')
print(file_class.number_of_sections)
print(file_class.environments)
print(file_class.base_python_versions)