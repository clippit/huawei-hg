华为家用路由器配置文件加解密工具
=====

适用于大多数电信赠送的华为家用路由器（HG232等）。

用法
-----

    translate.py < input_file > output_file

本工具会自动根据输入文件决定加密或解密。

示例：

    # 解密
    translate.py < ctce8_HG232.cfg > ctce8_HG232.cfg.xml
    # 加密
    translate.py < ctce8_HG232.cfg.xml > ctce8_HG232.cfg
