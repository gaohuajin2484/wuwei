'''
@File  :size_boost_weight_rerank.py
@Author:gaohuajin
@Date  :9/27/2110:58 AM
@Desc  :重排策略size_boost_weight_reank，根据用户的下单和APP设置的偏好尺码做排序加权。
'''

import copy

class Size_boost_weight_rerank:
    def __init__(self,user_size,style_size,original_score,weight_num,log_size,log_score):
        self.user_size = user_size
        self.style_size = style_size
        self.original_score = original_score
        self.weight_num = weight_num
        self.log_score = log_score
        self.log_size = log_size
        self.weight_list = self.get_weight_list()
        self.weight_score = self.get_weight_score()

    def get_weight_list(self):
        result = []
        tag = False
        for i in self.style_size.keys():
            for u_size in self.user_size:
                if u_size in self.style_size[i]:
                    tag = True
                else:
                    pass
            if tag == False:
                result.append(i)
            else:
                pass
            tag = False

        return result

    def get_weight_score(self):
        weight_score = copy.deepcopy(self.original_score)
        for i in self.weight_list:
            weight_score[i]["tmpScore"] = self.original_score[i]["tmpScore"] * self.weight_num

        return weight_score

    def diff_size(self):
        if self.weight_list == self.log_size:
            print("验证通过")
        else:
            print("验证失败")

    def diff_score(self):

        if self.log_score == self.weight_score:
            print("验证通过")
        else:
            print("验证失败")


if __name__ == '__main__':
    user_size = ["42","42.5"]
    style_size = ""
    original_score = ""
    log_size = ""
    log_score = ""
    weight_num = 0.8
    size_boost_weight_rerank  = Size_boost_weight_rerank(user_size,style_size,original_score,weight_num,log_size,log_score)
    size_boost_weight_rerank.diff_size()
    size_boost_weight_rerank.diff_score()