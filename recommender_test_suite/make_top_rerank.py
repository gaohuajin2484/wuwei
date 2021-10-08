'''
@File  :make_top_rerank.py
@Author:gaohuajin
@Date  :9/27/2110:55 AM
@Desc  : 重排策略make_top_rerank，指定相应的排序模型的TOP1商品，做商品置顶。
'''
import os,json,jsonpath2
import copy

class make_top_rerank:
    def __init__(self,recall_config_path,original_data_path,rerank_data):
        self.recall_config = json.loads(self.r_json(recall_config_path))
        self.original_data = json.loads(self.r_json(original_data_path))
        self.matchType_and_triggerKey_config_value = self.get_engine_conifg_makeTop()
        self.rankScore_down = self.get_original_data_makeTop()
        self.rerank_data = rerank_data
        self.match_reuslt()

    def match_reuslt(self):
        if int(self.rankScore_down[0][0]) == int(self.rerank_data[0]):
            print("测试通过，重排策略make_top_rerank的结果数据没有问题")
        else:
            print("测试失败，重排策略make_top_rerank 预计结果是{},实际结果是{}".format(self.rankScore_down[0][0],self.rerank_data[0]))

    def r_json(self,path):
        with open(path,"r") as f:
            return f.read()

    def get_engine_conifg_makeTop(self):
        make_top_rerank_path = self.json_parse("$..makeTop",self.recall_config)
        matchType_and_triggerKey_path = [ [k[:-11]+'["matchType"]',k[:-11]+'["triggerKey]'] for k,v in make_top_rerank_path.items() if v == True]
        matchType_and_triggerKey_config_value = self.json_parse(matchType_and_triggerKey_path,self.recall_config)
        print(matchType_and_triggerKey_config_value)
        return matchType_and_triggerKey_config_value

    def get_original_data_makeTop(self):
        result = {}
        for id in self.original_data.keys():
            for k,v in self.original_data[id]["matchAlgoScore"].items():
                for i in self.matchType_and_triggerKey_config_value:
                    for k1,v1 in i.items():
                        if k1 == k and v1 == self.original_data[id]["triggerInfoLog"]["triggerKey"]:
                            result[id] = self.original_data[id]["rankScore"]
                        else:
                            pass

        return sorted(result.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    def json_parse(self,path,data):
        if isinstance(path,str):
            match_data = jsonpath2.Path.parse_str(path)
            match_result = {}
            for match in match_data.match(data):
                match_result[match.node.tojsonpath()] = match.current_value

            return match_result

        elif isinstance(path,list):
            macth_list = []
            match_dict = {}
            result = []
            for path_node_list in path:
                for path_node in path_node_list:
                    print(self.to_jsonPath(path_node))
                    match_data = jsonpath2.Path.parse_str(self.to_jsonPath(path_node))
                    for match in match_data.match(data):
                        macth_list.append(match.current_value)
                match_dict[macth_list[0]] = macth_list[1]
                copy_match_dict = copy.deepcopy(match_dict)
                result.append(copy_match_dict)
                macth_list.clear()
                match_dict.clear()

            return result

    def to_jsonPath(self,path):

        path = path.replace('"','').replace("[","").strip("$").rstrip("]")
        path = "$."+".".join(path.split("]"))
        path_1 = path[0:43]
        path_2 = path[44:]
        path_2 = "[{}].{}".format(path_2.strip(".").split(".")[0],path_2.strip(".").split(".")[1])
        path = path_1+path_2
        return path

if __name__ == '__main__':
    recall_config_path = os.path.join(os.path.dirname(os.getcwd()),"recommender_engine_conifg_json","HOME_FEED_RECOMMEND_RANK.json")
    original_data_path = os.path.join(os.path.dirname(os.getcwd()),"model_rank_json","test1.json")
    rerank_data = [18154049, 19733295, 21131450, 20716292, 19329551, 7421516, 21347604, 21020991, 4924563, 19731272, 7360144, 7069299, 1454556, 7091379, 22532329, 7030664, 288863, 7198062, 21627747, 21037907, 22777562, 1400411, 162723, 21666818, 20401505, 22394221, 7362639, 22528987, 4919709, 23732787, 2456581, 21751854, 19761479, 19431486, 1698825, 6527959, 19498633, 21105891, 16410164, 1639894, 21705354, 10495871, 20882310, 21160503, 7187653, 18253402, 21530747, 21584882, 1483513, 4792012, 20589497, 7461514, 8979967, 22358497, 4914961, 22543124, 19277730, 21926011, 5188008, 20668724, 30467, 1715984, 5077008, 4967050, 20432315, 7362642, 21925221, 2691221, 5916499, 21395150, 7394149, 1280137, 6354603, 23216492, 21023391, 23595265, 777939, 4302089, 7311410, 22789206, 20900228, 4508700, 20888112, 22959104, 293196, 7706147, 5457545, 22524713, 1264280, 7461568, 22345306, 23248951, 764888, 9118231, 18725039, 4923048, 21652202, 77563, 22127804, 23242311, 4925078, 20342998, 18927514, 22804757, 1456957, 21750048, 20993866, 5014750, 22270689, 20053360, 22397176, 2515360, 18239730, 6289761, 7379601, 20818187, 1455476, 20818432, 22319888, 19361049, 21764847, 5258710, 22118920, 160481, 5432216, 22833958, 22811359, 4927580, 7362643, 17766524, 1653302, 7362645, 7022271, 6131235, 23074392, 21522408, 6078023, 7199153, 5586166, 7330022, 7379926, 6976346, 21978912, 18725014, 437710, 21263738, 23572909, 18363797, 20819910, 2530836, 16401778, 21922212, 1669882, 18281319, 6813617, 23556869, 853920, 4925402, 18857634, 5923834, 7202893, 19411789, 21320780, 725248, 22081898, 22115726, 1708433, 2818344, 18617632, 7650863, 4307717, 21705330, 4913715, 4924604, 19897367, 6523901, 2765961, 18070234, 18070356, 5651531, 7030510, 7306803, 23972123, 7259794, 21165263, 21181579, 7057086, 22788493, 18157610, 23742457, 1707300, 20683479, 4926985, 4920620, 1261836, 1443579, 7288131, 4923463, 20822214, 20435582, 4922341, 9015555, 16416348, 18308928, 19423411, 21194483, 20804814, 693680, 6765208, 21119723, 22529082, 4742158, 7305841, 22075379, 20655307, 22102103, 21893132, 7100943, 7465755, 7379762, 2529966, 100021, 2594387, 4925283, 22506244, 22520844, 6398683, 8955718, 18173553, 19203519, 21103262, 21837503, 13412521, 1421353, 21239048, 1241064, 22903590, 18449740, 7628902, 23293484, 64453, 1280178, 6611215, 21695509, 6078425, 2563708, 12555180, 7421581, 5620412, 22806496, 22837933, 4500646, 2496014, 23627923, 22474041, 7673466, 20713447, 5153583, 4311122, 21258122, 19495974, 23293015, 5145300, 21741457, 19471309, 4311123, 4920872, 7036867, 21807212, 20721317, 7426607, 6533905, 21276964, 7310123, 18996801, 1704867, 22763950, 22372623, 22977344, 4924491, 18555277, 7208938, 4925968, 6776578, 5177744, 531513, 9705008, 4926012, 6015268, 18518399, 1481517, 621121, 6934768, 6286849, 21248043, 5437478, 10474504, 6911072, 6909597, 5203704, 22075399, 20638679, 22323808, 20868866, 6824598, 5207507, 23292756, 5595288, 910533, 7478937, 426877, 20024, 22636220, 5507946, 7682210, 320763, 23636187, 6691143, 15259436, 6472413, 6557759, 6459464, 6459534, 9123033, 21938996, 21510369, 7682429, 6909173, 23293474, 21075550, 6998119, 6981061, 18878550, 4236493, 21234422, 17655817, 860454, 6231623, 6207377, 18354072, 20937738, 4839903, 18624361, 21177388, 20739883, 20939832, 18354556, 6790131, 6009658, 8990394, 22840769, 465455, 20898337, 21082107, 22005209, 19489378, 2802585, 15184955, 4559299, 20923077, 874600, 6472459, 5275344, 6423704, 117836, 6937790, 22712353, 1280680, 19988484, 979712, 19860706, 23394044, 4537116, 7127429, 2542428, 23103936, 22968108, 22636961, 11743555, 18722055, 22106734, 19958380, 4924299, 19783870, 19529843, 6027033, 21369816]
    make_top_rerank = make_top_rerank(recall_config_path,original_data_path,rerank_data)