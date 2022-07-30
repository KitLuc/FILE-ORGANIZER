from enum import Enum, unique


@unique
class Extends_enum(Enum): #NOSONAR
    PICTURES:list = ['.png','jpg','jpeg','.svg','.gif','.tiff','tif','.bmp']
    PHOTO_EDIT:list = ['.ai','.eps']
    VIDEO:list = ['.mp4','.mov','.avi','.mkv','.flv']
    DOCUMENTS:list = ['.pdf','.xlsx','.xls','.docx']
    SYSTEM_DATA:list = ['.iso']
    TEXT:list = ['.txt']
    COMPRESS:list = ['.zip','.rar']
    