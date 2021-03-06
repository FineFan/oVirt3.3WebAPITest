#encoding:utf-8

__authors__ = ['"Wei Keke" <keke.wei@cs2c.com.cn>']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/10/09          初始版本                                                            Wei Keke 
#---------------------------------------------------------------------------------
'''

from TestAPIs.StorageDomainAPIs import StorageDomainAPIs
import TestData.Disk.ITC08_SetUp as ModuleData

'''---------------------------------------------------------------------------------------------------
@note: PreData
---------------------------------------------------------------------------------------------------'''
disk_name = 'Test-DISK'
sd_id = StorageDomainAPIs().getStorageDomainIdByName(ModuleData.data1_nfs_name)
disk_info = '''
<data_driver>
<disk>
    <alias>Test-DISK</alias>
    <size>1059061760</size>
    <interface>virtio</interface>
    <format>raw</format>
</disk>
<disk>
    <alias>Test-DISK</alias>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <interface>virtio</interface>
    <format>raw</format>
</disk>
<disk>
    <alias>Test-DISK</alias>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>1059061760</size>
    <format>raw</format>
</disk>
<disk>
    <alias>Test-DISK</alias>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>1059061760</size>
    <interface>virtio</interface>
</disk>
</data_driver>
'''% (sd_id, sd_id, sd_id)

'''---------------------------------------------------------------------------------------------------
@note: ExpectedData
---------------------------------------------------------------------------------------------------'''
expected_status_code = 400
expected_info_list = [
'''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot add Virtual Machine Disk. Storage Domain doesn't exist.]</detail>
</fault>
'''
,
'''
<fault>
    <reason>Incomplete parameters</reason>
    <detail>Disk [provisionedSize|size] required for add</detail>
</fault>
'''
,
'''
<fault>
    <reason>Incomplete parameters</reason>
    <detail>Disk [interface] required for add</detail>
</fault>
'''
,
'''
<fault>
    <reason>Incomplete parameters</reason>
    <detail>Disk [format] required for add</detail>
</fault>
'''
]
