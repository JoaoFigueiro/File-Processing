import configparser


config = configparser.ConfigParser()
print(config.read('mess.ini'))

dev_dict = {}
prod_dict = {}

for section in config.sections():
    section_attribute = config[section]

    match section_attribute.get('env'): 
        case 'dev': 
            section_attribute.pop('env')
            dev_dict[section] = dict(section_attribute.items())
            
        case 'prod': 
            section_attribute.pop('env')
            prod_dict[section] = dict(section_attribute.items())
    
dev_section = configparser.ConfigParser()
prod_section = configparser.ConfigParser()

with open('dev_config.ini', 'w') as dev_cfg:
    dev_section.read_dict(dev_dict)
    dev_section.write(dev_cfg) 

with open('prod_config.ini', 'w') as prod_cfg:
    prod_section.read_dict(prod_dict)
    prod_section.write(prod_cfg)

