#coding:utf-8


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

from TestData.DataCenter import ITC01_SetUp as ModuleData

'''
---------------------------------------------------------------------------------------------------
@note: ModuleTestData
---------------------------------------------------------------------------------------------------
'''
########################################################################
# 1个数据中心信息（使用模块测试环境中的dc_nfs）                                                                                                                                    
########################################################################
dc_nfs_name = ModuleData.dc_nfs_name

########################################################################
# 1个集群信息（使用模块测试环境中的cluster_nfs）                                                                                                                                    
########################################################################
cluster_nfs_name = ModuleData.cluster_nfs_name

########################################################################
# 1个主机信息（使用模块测试环境中的host1）                                                                                                                                    
########################################################################
host_name = ModuleData.host1_name

#######################################################################################
# 1个存储域信息（只需要提供存储域名称，因为它是在模块测试环境中已经创建的data2_nfs）                                                                                                                               
#######################################################################################
export1_name = ModuleData.export1_name

'''
---------------------------------------------------------------------------------------------------
@note: Post-Test-Data
---------------------------------------------------------------------------------------------------
'''




'''
---------------------------------------------------------------------------------------------------
@note: ExpectedResult
---------------------------------------------------------------------------------------------------
'''
expected_status_code_attach_sd = 201                    # 将存储域附加到数据中心，成功，返回状态码
expected_status_code_deactivate_sd = 200                # 将存储域设置为维护状态，成功，返回状态码
expected_status_code_detach_sd = 200                    # 将存储域从数据中心分离，成功，返回状态码