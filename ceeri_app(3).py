from mainwindow import Ui_MainWindow
from PyQt4 import QtCore,QtGui
from configure_window import Ui_configure_window

import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
arr_node_dic=[]
currentIndex=0
s_nos=set()
node_name=set()
node_name_dic={}
total=0;

import time
class ConfigureWindow(QtGui.QMainWindow, Ui_configure_window):
    
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        flags= QtCore.Qt.Drawer| QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setupUi(self)
        
        try:
            temp_dic=arr_node_dic[currentIndex].copy()
            self.analog_count.setMaximum(int(arr_node_dic[currentIndex]["a_count"]))
            self.digital_count.setMaximum(int(arr_node_dic[currentIndex]["d_count"]))
            for i in range(0,int(arr_node_dic[currentIndex]["a_count"])):
                self.analog_sensors_list.addItem(str(i+1))
            for i in range(0,int(arr_node_dic[currentIndex]["d_count"])):
                self.digital_sensors_list.addItem(str(i+1))
        
            self.analog_sensor_input.valueChanged(self.analogValueChanged)
            self.digital_sensor_input.valueChanged(self.digitalValueChanged)
            
            
            self.pushButton.clicked.connect(self.OkButtonClicked)
        except:
            print "error"
    
    def OkButtonClicked(self):
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(533, 70, 20, 151))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        arr_node_dic[currentIndex]=self.temp_dic

    def analogValueChanged(self):
        print ""
        self.temp_dic["al"][int(self.analog_sensor_list.currentText())-1]=self.analog_sensor_input.text()
    
    def digitalValueChanged(self):
        print ""
        self.temp_dic["dl"][int(self.digital_sensor_list.currentText())-1]=self.digital_sensor_input.text()
    
        
class CentralWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        
        self.addNode.clicked.connect(self.addNodeClicked)
        
        self.removeNode.clicked.connect(self.removeNodeClicked)
        
        self.node_names.currentIndexChanged.connect(self.nameChanged)
        
        self.Nodes.currentIndexChanged.connect(self.currentIndexChanged)
        
        self.configureNode.clicked.connect(self.OpenConfigureWindow)
        
        
    def currentIndexChanged(self):
        currentIndex=self.Nodes.currentIndex()    
        
    def OpenConfigureWindow(self):
        self.popConfigureWindow=ConfigureWindow()
        self.popConfigureWindow.show()
        
    def nameChanged(self): 
        self.analog_sensor_value.setText(str(node_name_dic[str(self.node_names.currentText())]))
        
    def removeNodeClicked(self):
        index = self.Nodes.currentIndex()
        node_name=str(arr_node_dic[index]["name"])
        self.Nodes.removeItem(index)
        self.listWidget.takeItem(index)
        node_name_dic[node_name]=node_name_dic[node_name]-1
        if(node_name_dic[node_name]<0):
            node_name_dic[node_name]=0
        
        
          
    def addNodeClicked(self):
        temp_dic={}
        temp_dic["name"]=self.lineEdit.text()
        temp_dic["sno"]=self.Serial_No_lineEdit.text()
        temp_dic["bv"]=self.temp.text()
        temp_dic["bc"]=self.spinBox.text()
        temp_dic["a_count"]=self.total_analog.text()
        temp_dic["d_count"]=self.total_digital.text()
        temp_dic["type"]=self.comboBox.currentText()
        a_list=[]
        d_list=[]
        i=0
        for i in range(0,int(temp_dic["a_count"])):
            a_list.append(0)
        for i in range(0,int(temp_dic["d_count"])):
            d_list.append(0)
        temp_dic["al"]=a_list
        temp_dic["dl"]=d_list
        if(temp_dic["sno"] not in s_nos):
            s_nos.add(temp_dic["sno"])
            self.Nodes.addItem(temp_dic["name"]+" "+temp_dic["sno"])
            self.listWidget.addItem(temp_dic["name"]+" "+temp_dic["sno"])
            if(str(temp_dic["name"]) not in node_name):
                node_name_dic[str(temp_dic["name"])]=1
                node_name.add(str(temp_dic["name"]))
                self.node_names.addItem(temp_dic["name"])
            else:
                node_name_dic[str(temp_dic["name"])]=node_name_dic[str(temp_dic["name"])]+1
                
            if(temp_dic["type"]=="Coordinator"):
                self.comboBox.removeItem(0)
            arr_node_dic.append(temp_dic)
        else:
            print "sno already added"    
            

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    MainApp=CentralWindow()
    MainApp.show()
    sys.exit(app.exec_())
        