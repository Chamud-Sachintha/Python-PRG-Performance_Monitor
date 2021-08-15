import win32api,os,shutil,psutil,platform
import subprocess

def GetBasicDriveInfo():
    drive_alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drive_list = []

    for each_letter in drive_alp:
        try:
            drive_name = each_letter + "://"
            os.chdir(drive_name)
        except:
            continue
        drive_list.append(drive_name)

    return drive_list

def GetSelectedVolumeInformations(self, GetCurrentDriveLetter):
        #Get Volume Informations Using Win32api library and shutil library
        CompleteVolumeInfo = []
        VolumeTypeInfo = list(win32api.GetVolumeInformation(GetCurrentDriveLetter))
        VolumeInfo = list(shutil.disk_usage(GetCurrentDriveLetter))

        CompleteVolumeInfo.append(VolumeInfo)
        CompleteVolumeInfo.append(VolumeTypeInfo[0])
        CompleteVolumeInfo.append(VolumeTypeInfo[4])

        return CompleteVolumeInfo

def GetOperatingSystemInformations(self):
    os_details = []
    SystemOSDetails = platform.uname()
    os_details.append(SystemOSDetails.system)
    os_details.append(SystemOSDetails.node)
    os_details.append(SystemOSDetails.release)
    os_details.append(SystemOSDetails.version)
    os_details.append(SystemOSDetails.machine)
    os_details.append(SystemOSDetails.processor)

    return os_details

def GetCompleteDiskStorageInformationStatus():
    PartitionSize = []
    DiskSize = ""
    SysDiskInfo = list(subprocess.run(["wmic","diskdrive","get","size"],capture_output=True).stdout.decode())
    for each_num in SysDiskInfo:
        if(each_num.isnumeric()):
            DiskSize = DiskSize + each_num
        else:
            continue

    DriveList = GetBasicDriveInfo()
    PartitionSize.append(int(DiskSize))
    for each_drive in DriveList:
        EachPartitionSize = shutil.disk_usage(each_drive)
        PartitionSize.append(EachPartitionSize[0])

    return PartitionSize