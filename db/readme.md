last updated 2022 - 6 - 29

#schema

数据表图式。

## 销量预测

### 三月销量预测

    create table `三月销量预测` (
           id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
           `预算制定流水号` varchar(200),
           `预算填写人` varchar(100),
           `预算期间` varchar(30),
           `预算截止期` varchar(30),
           `预算部门` varchar(60),
           `预测销售总金额` float,
           `预计新增门店数` int,
           `线下渠道预估轻饮酒总销量（瓶）` int,
           `线下渠道预估蓝气罐总销量（箱）` int,
           `电商预估轻饮酒总销量（瓶）` int,
           `电商预估蓝气罐总销量（箱）` int,  
           `预测销售总金额-二月` float,
           `预计新增门店数-二月` int,
           `线下渠道预估轻饮酒总销量（瓶）-二月` int,
           `线下渠道预估蓝气罐总销量（箱）-二月` int,
           `电商预估轻饮酒总销量（瓶）-二月` int,
           `电商预估蓝气罐总销量（箱）-二月` int, 
           `预测销售总金额-三月` float,
           `预计新增门店数-三月` int,
           `线下渠道预估轻饮酒总销量（瓶）-三月` int,
           `线下渠道预估蓝气罐总销量（箱）-三月` int,
           `电商预估轻饮酒总销量（瓶）-三月` int,
           `电商预估蓝气罐总销量（箱）-三月` int, 
           `销售预测` varchar(20),
           `大区-第一月线下` varchar(20),
           `省份-第一月线下` varchar(20),
           `区域-第一月线下` varchar(255),
           `大区-第二月线下` varchar(20),
           `省份-第二月线下` varchar(20),
           `区域-第二月线下` varchar(255),
           `大区-第三月线下` varchar(20),
           `省份-第三月线下` varchar(20),
           `区域-第三月线下` varchar(255),
           `电商平台` varchar(20),
           `备注` varchar(200),
           `预测销售总金额（三个月）` float,
           `填写日期` varchar(20)
        )
    
    
### 单月销量预测
    
    create table 单月销量预测(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        预算制定流水号 varchar(200),
        预算填写人 varchar(100),
        预算期间 varchar(30),
        预算部门 varchar(30),
        预测销售总金额 float,
        预计新增门店数 int,
        `线下渠道预估轻饮酒总销量（瓶）` int,
        `线下渠道预估蓝气罐总销量（箱）` int,
        `电商预估轻饮酒总销量（瓶）` int,
        `电商预估蓝气罐总销量（箱）` int,        
        销售预测 varchar(20),
        大区 varchar(30),
        省份 varchar(30),
        区域 varchar(255),
        电商平台 varchar(30),
        备注 varchar(200),
        填写日期 varchar(20)
    )

### 单月销量预测第二月

    create table 单月销量预测第二月(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        预算制定流水号 varchar(200),
        预算填写人 varchar(100),
        预算期间 varchar(30),
        预算部门 varchar(30),
        预测销售总金额 float,
        预计新增门店数 int,
        `线下渠道预估轻饮酒总销量（瓶）` int,
        `线下渠道预估蓝气罐总销量（箱）` int,
        `电商预估轻饮酒总销量（瓶）` int,
        `电商预估蓝气罐总销量（箱）` int,        
        销售预测 varchar(20),
        大区 varchar(30),
        省份 varchar(30),
        区域 varchar(255),
        电商平台 varchar(30),
        备注 varchar(200),
        填写日期 varchar(20)
    )

### 单月销量预测第三月

    create table 单月销量预测第三月(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        预算制定流水号 varchar(200),
        预算填写人 varchar(100),
        预算期间 varchar(30),
        预算部门 varchar(30),
        预测销售总金额 float,
        预计新增门店数 int,
        `线下渠道预估轻饮酒总销量（瓶）` int,
        `线下渠道预估蓝气罐总销量（箱）` int,
        `电商预估轻饮酒总销量（瓶）` int,
        `电商预估蓝气罐总销量（箱）` int,        
        销售预测 varchar(20),
        大区 varchar(30),
        省份 varchar(30),
        区域 varchar(255),
        电商平台 varchar(30),
        备注 varchar(200),
        填写日期 varchar(20)
    )





