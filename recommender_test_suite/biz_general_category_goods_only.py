'''
@File  :biz_general_category_goods_only.py
@Author:gaohuajin
@Date  :9/27/2110:50 AM
@Desc  :重排策略biz_general_category_goods_only，根据入参的type字段，对召回的style_id进行商品去重。
'''
from  tools.goods_info_makes import goodsDataComplement

class Biz_general_category_goods_only():
    def __init__(self):
        #8
        # print("------重排之前的数据")
        # self.get_chongpai_qian()
        # print("------重排之后的数据")
        # self.get_chongpai_hou()
        pass

    def get_chongpai_qian(self):
        data = [18164758, 18876021, 5265503, 15272357, 23537565, 9118070, 6545674, 9119413, 7306882, 6701650, 22559512, 7381755, 5471995, 23003597, 22193974, 10482517, 9118158, 5263164, 6820594, 19386313, 23624634, 20342998, 7277795, 9114135, 7442788, 9119512, 23236418, 6230810, 21319138, 19005808, 20065366, 14390, 7160537, 5891147, 20693435, 1699612, 5554011, 7263136, 19331524, 23906330, 22835751, 23810369, 4781713, 1455501, 12532840, 22270689, 853248, 1588639, 5765532, 2543559, 19429652, 9119661, 23450204, 7331396, 6831828, 23536883, 23351924, 23775133, 19450806, 23810270, 1629496, 23916077, 23822954, 19920447, 21093705, 23774750, 23237025, 13413732, 4219232, 23022603, 7331658, 9700072, 564889, 23452825, 23799681, 23302907, 23450249, 6544975, 23799713, 23556752, 19399524, 7310123, 5569928, 6995781, 18725105, 23007858, 6388215, 23449681, 23472730, 23238734, 23055365, 1707300, 23460279, 23221893, 7270337, 17937596, 9082084, 23304140, 23810049, 20710487, 5434929, 7306803, 17701, 5047401, 23717965, 7454346, 4400507, 19263935, 5552814, 5648787, 4244972, 1456957, 23800018, 23793941, 20882375, 23616177, 23018538, 7488703, 5507946, 18253694, 5681869, 22821086, 23357278, 20804814, 23158291, 23556786, 5274708, 5048396, 21093641, 30467, 19402229, 18157610, 23524131, 21672921, 22618215, 19774368, 1703119, 18308928, 6639736, 856679, 118501, 6119399, 6959789]
        goods_attr = goodsDataComplement.SearchGoodsAttr(goods_id=[], style_id=data, request_id="TTe8m40h8td800")
        aa = goods_attr.getGoodsRootCategoryAndChildCategory()
        type_4 = []
        type_6 = []
        type_4_attr = []
        for i in aa:
            if i["childCategoryId"] == 111111:
                type_6.append(i["goods"])
            else:
                type_4.append(i["goods"])
                type_4_attr.append(i)

        print("type_6未去重的goodsid")
        print(type_6)
        print("type_6未去重的goodsid的长度")
        print(len(type_6))
        print("type_4未去重的goodsid")
        print(type_4)
        print("type_4去重的goodsid")
        print(set(type_4))
        print("type_4去重的goodsid的长度")
        print(len(set(type_4)))

        # print("这是去重前的style_ids{}".format(type_4_dict))


    def get_chongpai_hou(self):
        data = [18164758, 5265503, 23537565, 6545674, 22559512, 23003597, 22193974, 5263164, 23624634, 7277795, 9114135, 23236418, 14390, 20693435, 23906330, 23810369, 4781713, 1455501, 22270689, 853248, 1588639, 23450204, 23536883, 23351924, 23775133, 1629496, 23916077, 23822954, 23774750, 23237025, 4219232, 23022603, 9700072, 564889, 23799681, 23302907, 6544975, 19399524, 23007858, 23472730, 23238734, 23055365, 23460279, 23221893, 7270337, 23304140, 17701, 5047401, 23717965, 5648787, 23800018, 23793941, 23018538, 5507946, 5681869, 22821086, 23357278, 23158291, 5274708, 5048396, 30467, 23524131, 21672921, 19774368, 18308928, 856679, 6959789]
        goods_attr = goodsDataComplement.SearchGoodsAttr(goods_id=[], style_id=data, request_id="TTe8m40h8td800")
        aa = goods_attr.getGoodsRootCategoryAndChildCategory()
        type_4 = []
        type_6 = []
        type_4_attr = []
        for i in aa:
            if i["childCategoryId"] == 11111111:
                type_6.append(i["goods"])
            else:
                type_4.append(i["goods"])
                type_4_attr.append(i)

        print("type_6未去重的goodsid")
        print(type_6)
        print("type_6未去重的goodsid的长度")
        print(len(type_6))
        print("type_4未去重的goodsid")
        print(type_4)
        print("type_4去重的goodsid")
        print(set(type_4))
        print("type_4去重的goodsid的长度")
        print(len(set(type_4)))

        # print("这是去重前的style_ids{}".format(type_4_dict))


if __name__ == '__main__':
    run = Biz_general_category_goods_only()
    request_data = {"categories": [
        {
            "type": "6",
            "rootId": 8
        }]}

