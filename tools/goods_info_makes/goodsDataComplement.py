'''
@File  :goodsDataComplement.py
@Author:gaohuajin
@Date  :9/27/2111:03 AM
@Desc  :
'''
import requests,jsonpath2,json

class SearchGoodsAttr:

    def __init__(self,goods_id=None,style_id=None,request_id=None):
        self.GOODS_ATTR_SEARCH_API = "http://sh-gateway.shihuo.cn/v4/services/sh-goodsinnerapi/goods/get?id={}&access_token=WphjwI564K8kzs5JQZ&client_name=ghj"
        self.STYLE_ATTR_SEARCH_API  ="http://sh-gateway.shihuo.cn/v4/services/sh-goodsinnerapi/style/get?id={}&access_token=WphjwI564K8kzs5JQZ&client_name=ghj"
        self.goods_id = goods_id
        self.style_id = style_id
        if request_id[:2] == "TT" or request_id[:2] == "DG":
            if len(style_id) != 0:
                self.goods_id=  self.goods_id + self.getGoodsId()
            else:
                pass
        else:
            pass

    def getGoodsId(self):
        '''

        :return: 返回商品id
        '''
        goods_id_path = "$.data.data[0].goodsId"
        if isinstance(self.style_id[0],list):
            list1 = []
            for i in self.style_id:
                list2 = self.__toResult(self.STYLE_ATTR_SEARCH_API, i, goods_id_path)
                list3 = list(set(list2))
                if len(list3) == 1:
                    list1.append(list3[0])
                else:
                    list1.append(list3)
        else:
            return self.__toResult(self.STYLE_ATTR_SEARCH_API,self.style_id,goods_id_path)

        return list1

    def getRootCategoryId(self):
        '''

        :return: 返回一级类目id
        '''
        root_category_id_path = "$.data.list[0].rootCategoryId"
       # return self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,root_category_id_path)
        root_category_id_list = self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,root_category_id_path)
        style_id_attr = []
        for i in range(len(root_category_id_list)):
            style_id_attr.append(str(self.style_id[i])+":"+str(root_category_id_list[i]))
        print(style_id_attr)

    def getChildCategoryId(self):
        '''

        :return: 返回二级类目id
        '''
        child_category_id_path = "$.data.list[0].childCategoryId"
        return self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,child_category_id_path)
        # child_category_id_list = self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,child_category_id_path)
        # style_id_attr = []
        # for i in range(len(child_category_id_list)):
        #     style_id_attr.append(str(self.style_id[i])+":"+str(child_category_id_list[i]))
        # return style_id_attr



    def getGoodsRootCategoryAndChildCategory(self):
        '''

        :return: 返回一级类目id+二级类目id
        '''

        child_category_id_path = "$.data.list[0].childCategoryId"
        root_category_id_path = "$.data.list[0].rootCategoryId"
        path= []
        path.append(root_category_id_path)
        path.append(child_category_id_path)
        result = self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,path)
        for i in range(len(self.style_id)):
            result[i]["style_id"] = int(self.style_id[i])
        return result

    def getGoodsRootBrandAndChildBrand(self):
        '''

        :return: 返回一级品牌id+二级品牌id
        '''

        child_brand_path = "$.data.list[0].rootBrandId"
        root_brand_id_path = "$.data.list[0].childBrandId"
        path= []
        path.append(child_brand_path)
        path.append(root_brand_id_path)
        return self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,path)

    def getRootBrandId(self):
        '''

        :return: 返回一级品牌id
        '''
        root_brand_id_path = "$.data.list[0].rootBrandId"
        return self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,root_brand_id_path)

    def getChildBrandId(self):
        '''

        :return: 返回二级品牌id
        '''
        child_brand_id_path = "$.data.list[0].childBrandId"
        return self.__toResult(self.GOODS_ATTR_SEARCH_API,self.goods_id,child_brand_id_path)

    def __toResult(self,api,keys,data_path):
        '''

        :return:
        '''

        if isinstance(keys, list):
            __to_result_list = []
            goods_dict = {}
            for id in keys:
                __STYLE_ATTR_SEARCH_API = api.format(
                    id)
                res = requests.get(__STYLE_ATTR_SEARCH_API)
                if isinstance(data_path,list):
                    goods_dict["goods"] = id
                    goods_dict["{}".format(data_path[0].split(".")[-1])] = list(self.parse(data_path[0],res.json()).values())[0]
                    goods_dict["{}".format(data_path[1].split(".")[-1])] = list(self.parse(data_path[1],res.json()).values())[0]
                    __to_result_list.append(goods_dict.copy())
                else:
                    try:
                        __to_result_list.append(list(self.parse(data_path,res.json()).values())[0])
                    except:
                        print(res.json())
                        print(self.parse(data_path,res.json()))
            return __to_result_list
        else:
            __STYLE_ATTR_SEARCH_API = api.format(
                keys)
            res = requests.get(__STYLE_ATTR_SEARCH_API)

            __to_result = list(self.parse(data_path,res.json()).values())[0]
            return __to_result

    def parse(self,jsonpath, data):
        """
        data：{"data": {"list": [{"goods_id": "13"},{"goods_id": "16"}]}}
        jsonpath：$.data.lists[*].goods_id
        result:{"$[data][lists][0][goods_id]":"13","$[data][lists][1][goods_id]":"16"}
        """
        __result = {}

        try:
            path = jsonpath2.Path.parse_str(jsonpath)
            for match_data in path.match(data):
                __result[match_data.node.tojsonpath()] = match_data.current_value

            return __result
        except:
            return "数据有误，请检查你输入的参数属否正确"

if __name__ == '__main__':
    style_id = [4922319,9705837, 5411097, 16401778, 4922341, 21653837, 7029013, 4924924, 4926599, 6714389, 4922284, 4927053, 21347604, 4922687, 4925403, 18154049, 21473001, 21406797, 4924932, 4922089, 4926302, 6309911, 4925078, 4925503, 20434592, 21509959, 4923004, 4923685, 20900228, 4924973, 7218880, 6379275, 21363340, 19479945, 23613082, 6018595, 6062205, 4922411, 4923072, 7006965, 6440370, 4924660, 4928150, 15223986, 19077755, 6437527, 5276699, 4925917, 21274783, 4922430, 6729406, 6021949, 7095544, 4922993, 6254446, 4925318, 22917597, 4925424, 18900816, 4925013, 4925848, 19005808, 6934768, 4923694, 4925258, 4925645, 4924294, 4924479, 6022090, 6013699, 4926018, 7012397, 21824669, 4925283, 4925747, 4926932, 4923650, 20460297, 4924410, 20952890, 12565426, 7018884, 21626136, 6828323, 4924523, 21272678, 5554011, 6051248, 4925847, 1699852, 4920439, 6430419, 6338555, 20850324, 6548318, 5074521, 6430171, 20716292, 4922244, 22788661, 6550019, 169181, 6753444, 22543124, 4925846, 4925408, 22808041, 18253402, 7310680, 18239730, 6857111, 22127804, 7030917, 21926011, 6506169, 4917278, 6844029, 5226324, 7461567, 4913634, 19658932, 4925009, 19335319, 6696553, 5989153, 4923611, 22367588, 19782976, 4913728, 20053360, 1543477, 20046761, 6429726, 20461357, 9154721, 4926432, 22296362, 17941605, 6888094, 21626291, 23272033, 880005, 7030664, 151128, 7108255, 17932459, 19508128, 6813617, 2544981, 21134164, 19429652, 6765208, 21320843, 23972123, 23290964, 4923463, 21751854, 4195777, 7118928, 115883, 20050118, 6211627, 21705330, 7442788, 919348, 22524713, 6606815, 6909042, 5198643, 7030510, 22081898, 22806496, 19393852, 19733295, 19452612, 4913847, 7259794, 6753441, 20675177, 23169971, 5370875, 4913702, 20192488, 4926366, 19334925, 4920627, 7044390, 20888112, 9705903, 6820594, 17977067, 1588639, 7330022, 4924571, 919350, 22102103, 1693877, 21083552, 125191, 857911, 175362, 21893132, 6806262, 2594387, 4914961, 20646001, 20724808, 5370844, 22777538, 22397176, 20882310, 22325747, 21160503, 9100574, 4913661, 17701, 19424752, 20589497, 6753434, 21705354, 1550022, 18725039, 30467, 2743894, 1703119, 18725014, 7187074, 19331524, 1535576, 20955391, 4913715, 6950434, 22782537, 5569928, 622177, 423, 6753449, 20739314, 7108256, 6721242, 5080156, 21181583, 7024265, 4925965, 19270716, 4920853, 764888, 5403650, 23934152, 4913650, 7360144, 4913799, 19498633, 4913783, 4922192, 9087983, 19666257, 6858899, 24150051, 4926154, 1280137, 7009909, 23216492, 9099428, 4913826, 23248951, 4924460, 18899170, 4924604, 19761479, 21651859, 6753430, 9701469, 7394149, 19897367, 1456957, 4921465, 7187077, 4913675, 6357172, 19652341, 856679, 4908810, 6885314, 6495792, 20822214, 6131235, 9015555, 8903252, 1241064, 21837503, 2530836, 6958664, 18173553, 7461568, 70334, 5731414, 23687516, 2691259, 4902486, 1698825, 20563502, 7623721, 4946135, 7311410, 6495848, 19342016, 7362639, 5586137, 20821241, 100021, 21807212, 8997486, 22788470, 693680, 6945871, 6404407, 5611765, 7411601, 22160589, 9099647, 4911496, 6909173, 621121, 21507313, 21995897, 23627923, 21995798, 21134181, 7362644, 897898, 23245072, 6785852, 7379762, 2515360, 7208938, 23687474, 22520844, 5207507, 6472459, 22488621, 17891691, 7461514, 249621, 7362645, 8997463, 125658, 22061874, 4908289, 23272036, 4311122, 6783269, 20280817, 6998119, 21199931, 4244972, 7211887, 8997484, 5411047, 21082466, 5866572, 7288131, 278859, 23601686, 22368611, 5437478, 5839237, 10443298, 21075550, 19431899, 23208284, 22930607, 5203704, 7140627, 801724, 426878, 1649012, 19912844, 4236493, 8997487, 23888587, 6664112, 19488117, 2542428, 19354755, 21369816]
    aa = SearchGoodsAttr(goods_id=[],style_id=style_id,request_id="TTe8m40h8td800")
    print(json.dumps(aa.getGoodsRootCategoryAndChildCategory()))