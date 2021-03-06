#encoding:utf-8

__authors__ = ['"Liu Fei" <fei.liu@cs2c.com.cn>']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/10/24          初始版本                                                            Liu Fei 
#---------------------------------------------------------------------------------
'''

'''---------------------------------------------------------------------------------
@PreData
---------------------------------------------------------------------------------'''


'''---------------------------------------------------------------------------------
@note: TestData
---------------------------------------------------------------------------------'''
dc_info = '''
<data_driver>
    <data_center>
        <storage_type>nfs</storage_type>
        <version minor="3" major="3"/>
    </data_center>
    <data_center>
        <name>DC-ITC0101030301-1</name>
        <version minor="2" major="3"/>
    </data_center>
    <data_center>
        <name>DC-ITC0101030301-1</name>
        <storage_type>fcp</storage_type>
    </data_center>
</data_driver>
'''

'''---------------------------------------------------------------------------------
@note: ExpectedResult
---------------------------------------------------------------------------------'''
expected_status_code = 400
expected_info_list = [
'''
<fault><reason>Incomplete parameters</reason><detail>DataCenter [name] required for add</detail></fault>
''',
'''
<fault><reason>Incomplete parameters</reason><detail>DataCenter [storageType] required for add</detail></fault>
''',
'''
<fault><reason>Operation Failed</reason><detail>[Cannot create Data Center. Selected Compatibility Version is not supported.]</detail></fault>
'''
]