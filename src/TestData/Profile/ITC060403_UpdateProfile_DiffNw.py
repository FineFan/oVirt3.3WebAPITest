#encoding:utf-8

nw_name = 'network001'
dc_name = 'Default'
profile_name = 'p001'



'''
@note: PreData
'''
nw_info = '''
<network>
    <name>%s</name>
    <data_center id= "5849b030-626e-47cb-ad90-3ce782d831b3"/>    
</network>
''' %nw_name


profile_info = '''
    <vnic_profile>
        <name>p001</name>
        <description>shelled</description>
        <network id="%s"/>
    </vnic_profile>
'''

'''
@note: TestData
'''
update_info = '''
    <vnic_profile>
        <description>shelled</description>
        <network id=""/>
        <port_mirroring>true</port_mirroring>
    </vnic_profile>
'''

'''
@note: ExpectedData
'''
expected_status_code = 400
expected_info = '''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot edit VM network interface profile. VM network interface profile's network cannot be changed.]</detail>
</fault>
'''
