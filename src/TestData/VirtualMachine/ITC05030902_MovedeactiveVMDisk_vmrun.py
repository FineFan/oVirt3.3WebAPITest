#encoding:utf-8
from TestAPIs.StorageDomainAPIs import StorageDomainAPIs
import TestData.VirtualMachine.ITC05_SetUp as ModuleData
'''
@note: PreData
'''
'''
@note: 存储域名称应该由该模块的Setup用例初始化获得，这里暂时用字符串代替
'''
disk_name = 'DISK-1%s'%ModuleData.vm_name
sd_id = StorageDomainAPIs().getStorageDomainIdByName(ModuleData.data1_nfs_name)
disk_info='''
<disk>
    <name>%s</name>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>1059061760</size>
    <sparse>false</sparse>
    <interface>virtio</interface>
    <format>raw</format>
    <bootable>true</bootable>
    <shareable>false</shareable>
    <wipe_after_delete>false</wipe_after_delete>
</disk>
'''%(disk_name,sd_id)

'''
@note: TestData
'''
move_option='''
<action>
    <storage_domain>
        <name>%s</name>
    </storage_domain>
    <async>false</async>
</action>
'''%ModuleData.data2_nfs_name
'''
@note: ExpectedData
'''
expected_status_code = 200

