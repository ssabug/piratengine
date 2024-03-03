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

        self.receiveFilter="/Engine/Deck1"

        self.session=PyStageLinQ.PyStageLinQ(self.new_device_found_callback, name="piratengine StagelinQ")
        self.thread = threading.Thread(target=self.session.start, args=());
        self.thread.start();

    def log(self,text,source='STLQ',severity='INFO',sameline=False):
        log(text,source=source,severity=severity,sameline=sameline);

    def new_device_found_callback(self,ip, discovery_frame, service_list):
        # Print device info and supplied services
        print(
            f"Found new Device on ip {ip}: Device name: {discovery_frame.device_name}, ConnectionType: {discovery_frame.connection_type}, SwName: {discovery_frame.sw_name}, "
            f"SwVersion: {discovery_frame.sw_version}, port: {discovery_frame.Port}")

        if len(service_list) > 0:
            print("Services found in device:")
        else:
            print("No services found")

        for service in service_list:
            print(f"\t{service.service} on port {service.port}")


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

                if message.ParameterName in self.data.keys():
                    self.data[message.ParameterName] = message.ParameterValue;
                    action = 'updated'
                else:
                    self.data |= {message.ParameterName : message.ParameterValue}
                    action='added'

                self.log(action + ' ' + message.ParameterName  + ' to ' + str(self.data[message.ParameterName]));
                #self.piratengine.stagelinqNewData();
            pprint(self.data)

            



    

