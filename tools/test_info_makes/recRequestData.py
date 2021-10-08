'''
@File  :recRequestData.py
@Author:gaohuajin
@Date  :9/27/2111:10 AM
@Desc  :
'''
from configobj import ConfigObj
import os,json,copy,re,time

class GetRequestData():
    def __init__(self):
        self.liuliang = self.getConfigValues("switch",section="liuliang")

    def getLiuliangAbtest(self,abtestList):
        new_data_list = []
        if self.liuliang == "all":
            return abtestList
        elif self.liuliang == "tt":
            new_data_list = list(filter(lambda x: re.search('=3', x) != None or re.search('=99', x) != None , abtestList))  # 生成新列表
        elif self.liuliang == "dg":
            new_data_list = list(filter(lambda x: re.search('=2', x)  != None, abtestList))
        elif self.liuliang == "sh":
            new_data_list = list(filter(lambda x: re.search('=11', x) != None or re.search('=12', x) != None or re.search('=13', x) != None, abtestList))
        return new_data_list

    def getRequestPara(self,cangjingName):
        request_json_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),"recommender_requestData_josn","{}.json".format(cangjingName))
        request_json_data = self.toJson(request_json_path)
        result_dict ={}
        result_list = []
        abtest = self.getConfigValues(cangjingName)
        liuliang_abtest = self.getLiuliangAbtest(abtest)

        with open(os.path.join(os.path.dirname(__file__),"deviceCode.txt"),"r") as f:
            for i in range(1, 5):
                self.readlines = f.readlines(i)
                v = self.readlines
                device_code = json.dumps(v[0].split("\n")[0])
                device_code = json.loads(device_code)
                self.eval = eval(device_code)
                device_code = self.eval
                request_json_data["userParam"] = device_code
                for i in liuliang_abtest:
                    result_dict["data"] = request_json_data
                    result_dict["header"] = {'content-type': 'application/json', 'abtest-control': i}
                    result_list.append(copy.deepcopy(result_dict))
        return result_list

    def toJson(self,path):
        with open(path,"r") as f:
            return json.load(f)

    def writeMockPath(self,data):
        conf = ConfigObj(os.path.dirname(__file__)+'/abtestConfig.ini')
        for key,value in data.items():
            conf["MOCKPATH"][key] = value
        conf.write()

    def rmMockPath(self,defutalPath):
        conf = ConfigObj('config.ini')
        del conf["MOCKPATH"][defutalPath]
        conf.write()

    def getConfigValues(self,key,section=None):

        if section == None:
            section = "abtest"
        else:
            pass
        conf = ConfigObj(os.path.dirname(__file__)+'/envConfig.ini')
        try:
            return conf[section][key]
        except:
            return "没有找到该记录"