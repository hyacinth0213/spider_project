# -*- coding: utf-8 -*-

import hashlib
import os


class Factories(object):  # 在这里加入一些静态类方法
    @staticmethod
    def string_to_sha1_hash(s):  # 使用sha1将字符串转换成唯一的数值
        m = hashlib.sha1(s.encode("utf-8")).hexdigest()
        return m

    @staticmethod
    def get_suffix_type(file):  # 判断一个文件的后缀名是什么类型
        # python中，使用==来比较两个**对象的值**是否相等，而java 则使用== 比较两个**对象**是否是同一对象
        # 譬如，java中比较字符串，一般使用equal 方法，来比较两个对象的值是否相等，而不使用==
        # 相比较的，python 使用**is** 来比较两个对象是否是同一对象。
        # 典型的图片类型后缀名: BMP, GIF, PNG, JPG, JPEG, TIFF
        # 获取file后缀名
        # 使用 os.path.splitext(file)[0] 可获得文件名。
        # 使用 os.path.splitext(file)[-1] 可获得以.开头的文件后缀名。
        # file_prefix = os.path.splitext(s)[0] 获取前缀(文件名)
        file_suffix = os.path.splitext(file)[-1][1:]  # get suffix (file type)
        # print(str.upper())  # 把所有字符中的小写字母转换成大写字母
        # print(str.lower())  # 把所有字符中的大写字母转换成小写字母
        # print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
        # print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写
        suffix_str = file_suffix.upper()
        if suffix_str == 'PDF' \
                or suffix_str == 'DOC':
            return 'DOCUMENT'
        elif suffix_str == 'JPG' \
                or suffix_str == 'JPEG' \
                or suffix_str == 'BMP' \
                or suffix_str == 'PNG' \
                or suffix_str == 'GIF' \
                or suffix_str == 'TIFF':
            return 'PICTURE'
        else:
            return 'UNKNOWN'
        pass

    @staticmethod
    def fix_field(field):
        return field.strip() if field else ''


print(Factories.get_suffix_type('https://www.altlandsberg.de/uploads/images/grundstuecke/id19/Gutshof_ Gielsdorf.pdf'))
print(Factories.get_suffix_type('https://www.altlandsberg.de/uploads/images/grundstuecke/id35/Kastanienallee 53 FK.jpg'))

