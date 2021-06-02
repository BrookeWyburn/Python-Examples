#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brook
#
# Created:     25/04/2021
# Copyright:   (c) brook 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os , platform


os_name = platform.system
os_platform = platform.platform
os_relase = platform.release

print("your operatoring system is:", os_name)
print("your operatoring system platform is:", os_platform)
print("your operatoring system release is:", os_relase)

