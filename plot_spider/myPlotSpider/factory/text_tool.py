# -*- coding: utf-8 -*-

import hashlib
import os


class Factories(object):
    @staticmethod
    def string_to_sha1_hash(s):  # 使用sha1将字符串转换成唯一的数值
        m = hashlib.sha1(s.encode("utf-8")).hexdigest()
        return m

    @staticmethod
    def string_to_uuid(s):  # 将字符串转换成唯一的uuid
        pass

    @staticmethod
    def get_suffix_type(file):  # 判断一个文件的后缀名是什么类型
        file_suffix = os.path.splitext(file)[-1][1:]  # get suffix (file type)
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
