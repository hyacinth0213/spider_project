# -*- coding: utf-8 -*-

import hashlib
import os


class TextTools(object):
    def __init__(self):
        pass

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

    @staticmethod
    def strip_string(old_lines):
        new_lines = []
        for each_line in old_lines:
            new_line = each_line.replace("\r", "").replace("\n", "").replace("\t", "").strip()
            # print("new line:" + new_line)
            # if string is NULL, do not add
            new_lines.append(new_line)
        return new_lines


if __name__ == "__main__":
    text = ['\r\n    \t\t\t        \t\t\t\r\n            \t\t\t', 'Beschreibung:',
            ' Im Bereich des ehemaligen Gutshofes im Ortskern von Gielsdorf soll ein neues lebendiges und attraktives Dorfzentrum entstehen. Neben verschiedenen möglichen Wohnformen sind Gastronomie, Beherbergung, Handwerk und Vermarktung regionaler Produkte oder Handwerksbetrieb in den flexibel zu gestaltenden Gebäuden auf der ehemaligen Hofstruktur möglich.\r\nEin Bebauungsplan schafft die rechtliche Grundlage zur langfristigen Entwicklung. Weitere Einzelheiten entnehmen Sie bitte der beigefügten Expertise. Ineressenten wenden sich bitte an Frau Christiane Rohland unter der E-Mail: c.rohland@stadt-altlandsberg.de oder nutzen die angegebenen Telefonnummern. \r\n',
            '\r\n        \t\t\t    \t\t\t        \t\t\t\r\n            \t\t\t', 'Lage:',
            ' 15345 Altlandsberg, Ortsteil Gielsdorf',
            '\r\n        \t\t\t    \t\t\t        \t\t\t           \r\n\t\t   \t\t\t\t\t\t\t\t\t\t',
            '\r\n\t\t\t\t\t\t\tExpertise: ', '\r\n\t\t\t\t\t\t\t\tGutshof_ Gielsdorf.pdf\r\n\t\t\t\t\t\t\t',
            '\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\r\n        \t\t\t    \t\t\t        \t\t\t\r\n            \t\t\t',
            'Ansprechpartner:', ' Christiane Rohland',
            '\r\n        \t\t\t    \t\t\t        \t\t\t\r\n            \t\t\t', 'Email Kontakt:',
            ' c.rohland@stadt-altlandsberg.de', '\r\n        \t\t\t    \t\t\t        \t\t\t\r\n            \t\t\t',
            'Eingestellt am:', ' 24/10/2013', '\r\n        \t\t\t    \t\t\t    \t\t']
    # TODO...
    cleaned_text = TextTools.strip_string(text)
    for str_line in cleaned_text:
        print(str_line)
    print("finish output")
