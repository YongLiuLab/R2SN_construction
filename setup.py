from setuptools import setup,find_packages

# requirements = ['numpy']  # 自定义工具中需要的依赖包
with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

setup(
    name="R2SN",  # 自定义工具包的名字
    version="1.1.1",  # 版本号
    author="YangFan",  # 作者名字
    author_email="2669742207@qq.com",  # 作者邮箱
    description="description",  # 自定义工具包的简介
    license='MIT-0',  # 许可协议
    url="https://github.com/YongLiuLab/R2SN",  # 项目开源地址
    packages=['R2SN','examples'],  # 自动发现自定义工具包中的所有包和子包
    include_package_data=True,
    classifiers=[                                           # 关于包的其他元数据(metadata)
        "Programming Language :: Python :: 3",              # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",           # 根据MIT许可证开源
        "Operating System :: OS Independent",               # 与操作系统无关
    ],
    install_requires=[install_reqs],  # 指定了当前软件包所依赖的其他python类库。这些指定的python类库将会在本package被安装的时候一并被安装
    python_requires='>=3.6'
)