"""
封装断言
"""


class Assert:
    def __init__(self, assert_type, real, expect, detail=None):
        if assert_type == 'equal':
            self.equal(real, expect, detail)
        elif assert_type == 'notEqual':
            self.not_equal(real, expect, detail)
        elif assert_type == 'notIN':
            self.not_in(real, expect, detail)
        elif assert_type == 'cover':
            self.cover(real, expect, detail)
        elif assert_type == 'notCover':
            self.not_cover(real, expect, detail)
        else:
            self.error(assert_type)

    @staticmethod
    def equal(real, expect, detail):

        assert expect == real, detail

    @staticmethod
    def not_equal(real, expect, detail):

        assert expect != real, detail

    @staticmethod
    def not_in(real, expect, detail):

        assert real not in expect, detail

    @staticmethod
    def cover(real, expect, detail):

        assert expect in real, detail

    @staticmethod
    def not_cover(real, expect, detail):

        assert expect not in real, detail

    @staticmethod
    def error(assert_type):

        assert 1 == 0, "没有匹配到断言类型【{}】，请联系管理员添加，或更换断言类型！".format(assert_type)
