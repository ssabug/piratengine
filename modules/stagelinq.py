import threading
from PyStageLinQ import EngineServices, PyStageLinQ
from modules.utils import *
from pprint import pprint


class stagelinq():
    def __init__(self,piratengine):
        self.log('Init StagelinQ');
        self.log('Using https://github.com/Jaxc/PyStageLinQ');
        self.data={};
        self.piratengine=piratengine;

        self.receiveFilter=""

        self.session=PyStageLinQ.PyStageLinQ(self.new_device_found_callback, name="piratengine StagelinQ")
        self.thread = threading.Thread(target=self.session.start, args=());
        self.thread.start();

    def log(self,text,source='STLQ',severity='INFO',sameline=False):
        log(text,source=source,severity=severity,sameline=sameline);

    def new_device_found_callback(self,ip, discovery_frame, service_list):
        msg1="Found new Device on ip " +str(ip) + ": Device name: " + str(discovery_frame.device_name) + ", ConnectionType: " + str(discovery_frame.connection_type) + ", SwName: " +str(discovery_frame.sw_name); 
        msg2="SwVersion: "+ str(discovery_frame.sw_version) + ", port: "+ str(discovery_frame.Port);
        self.log(str(msg1));
        self.log(str(msg2));

        if len(service_list) > 0:
            self.log("Services found in device:")
        else:
            self.log("No services found")

        for service in service_list:
            self.log("\t"+ str(service.service) + " on port " + str(service.port))


        # Request StateMap service
        for service in service_list:
            if service.service == "StateMap":
                self.session.subscribe_to_statemap(service, EngineServices.prime_go, self.state_map_data_print)
            
    def state_map_data_print(self,data):
        for message in data:

            #searchedText='TrackName'
            #if searchedText in message.ParameterName:
            #    print(searchedText + " : " + message.ParameterValue['string'])
            if self.receiveFilter == '' or (self.receiveFilter != '' and self.receiveFilter in message.ParameterName):
                #device=data[0].ParameterValue
                
                #if '/media/' in str(device):
                #device=str(device['string'])
                #self.log(device)
                #prefix=device[:-1]+'/'
                #message.ParameterName=prefix+message.ParameterName;
                if message.ParameterName in self.data.keys():
                    self.data[message.ParameterName] = message.ParameterValue;
                    action = 'updated'
                else:
                    self.data |= {message.ParameterName : message.ParameterValue}
                    action='added'
                #for i,d in enumerate(data):
                #    self.log('  data : ' + str(data[0]));
                #self.piratengine.stagelinqNewData();
            #pprint(self.data)

            



    

