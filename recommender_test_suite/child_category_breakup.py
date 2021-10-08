'''
@File  :child_category_breakup.py
@Author:gaohuajin
@Date  :9/27/2110:51 AM
@Desc  :重排策略child_category_breakup，根据配色的二级类目实现打散功能，相邻2个配色的二级类目不能相同。
'''

from  tools.goods_info_makes import goodsDataComplement

class Child_category_breakup:
    def __init__(self,data_list):
        self.data_list =data_list
        self.goodsDataComplement = goodsDataComplement.SearchGoodsAttr(goods_id=[],style_id=self.data_list,request_id="TTe8m40h8td800")

    def test_check(self):
        '''
        :return:style_id:style_id:index:index:child_category_id
        eg. ['9705837:9705837:1:2:12', '21653837:21653837:5:6:604']
        '''
        child_category = self.goodsDataComplement.getChildCategoryId()
        tag = True
        i = 1
        error_list= []
        for i in range(len(child_category)):
            if child_category[i-1] == child_category[i]:
                tag = False
                error_list.append(str(self.data_list[i-1])+":"+str(self.data_list[i])+":"+str(i-1)+":"+str(i)+":"+str(child_category[i]))
            else:
                pass
        if tag == True:
            return "测试通过，重排策略child_category_breakup的结果数据没有问题"
        else:
            return "测试通过，重排策略child_category_breakup存在问题的数据有 {}".format(error_list)

if __name__ == '__main__':
    test_data =[4922319,9705837, 9705837, 16401778, 4922341, 21653837, 21653837, 4924924, 4926599, 6714389, 4922284, 4927053, 21347604, 4922687, 4925403, 18154049, 21473001, 21406797, 4924932, 4922089, 4926302, 6309911, 4925078, 4925503, 20434592, 21509959, 4923004]
    test = Child_category_breakup(test_data)
    print(test.test_check())