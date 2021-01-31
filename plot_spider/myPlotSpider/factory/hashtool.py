import hashlib


class Factories(object):  # 在这里加入一些静态类方法
    @staticmethod
    def string_to_sha1_hash(s):  # 使用sha1将字符串转换成唯一的数值
        m = hashlib.sha1(s.encode("utf-8")).hexdigest()
        return m
