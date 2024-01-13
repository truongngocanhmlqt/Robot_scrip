import os
root_path = os.getenv('root_path')
path = f'{root_path}settings/config.robot'
class getconfig():
    def __init__(self):
        self.ip_source = '100.64.10.7'
        self.ip_destination = '100.64.10.6'
        self.vlan_id = 10
        self.iface = 'Ethernet'
        self.timeout = '5s'
        self.GetConfig(path)

    def GetConfig(self, path):
        print("Reading: ", path)
        # check file exist
        if not os.path.exists(path):
            print(path, " does not exist")
            return -1
        # Get information
        try:
            with open(path, 'r') as file:
                for line in file:
                    if line.find('$') >= 0 and line.find('ip_source') >= 0:
                        self.ip_source = line.split()[-1]
                    if line.find('$') >= 0 and line.find('ip_destination') >= 0:
                        self.ip_destination = line.split()[-1]
                    if line.find('$') >= 0 and line.find('vlan_id') >= 0:
                        self.vlan_id = line.split()[-1]
                    if line.find('$') >= 0 and line.find('IFACE') >= 0:
                        self.iface = line.split()[-1]
                    if line.find('$') >= 0 and line.find('default_time_out_cmd') >= 0:
                        self.timeout = line.split()[-1]

        except FileNotFoundError:
            print(path, " does not exist")
        except IOError:
            print("Error read file")

# settingObj = getconfig()
# print(settingObj.ip_source)
# print(settingObj.ip_destination)
# print(settingObj.vlan_id)
# print(settingObj.iface)
# print(settingObj.timeout)
