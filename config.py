import platform


class Parameters:
    
    
    
    Image_Root_Path = r'/media/vvd/新加卷/pic'                                   # root of source raw images
    Hexo_Root_Path =r'/home/vvd/VVD_Work/Hexo/VVD_Hexo'                         # root of Hexo dir  
    Hexo_Sub_Dir_to_Photos = r'source/photos'                                   # my source dir for album
    Uploading_Temp_Image_Path = r'/home/vvd/VVD_Work/Hexo/Album_Temp'           # root of temp image dir
    Album_Ddescription_File_Name = 'readme.json'                                # name of json file in each image dir
    Log_File_Name = 'Album_Log.log'                                             # name of log file
    Album_Total_Json = 'album.json'                                             # json info of album
    Album_Md_File_Name = 'index.md'                                             # name of markdown file of hexo 
    Qshell_Config_File_Name = 'upload.conf'                                     # qiniu qshell config file name 
    
    Logging_Object = None                                                       # object of logging class
    Image_Info_Get_Object = None                                                # instance of PhotoExifInfo
    
    Image_Extension_List =['jpg','png','jpeg','bmp']                            # list of common image extensions 
    Image_Resize_Width = 2000                                                   # image width after resize
    Whether_Overwrite_Old_Temp_File = False                                     # whether overwrite old file while the program run again
    Image_Url_Prefix =r'https://photos.zywvvd.com/vvd_hexo/'                    # prefix of image url
    Force_Upload = False                                                        # upload images no matter what happens

    Current_System = platform.system()                                          # current operating system
    if Current_System == 'Linux':
        Split_Char ='/'                                                         # split char of current operating system
    elif Current_System == 'Windows':
        Split_Char ='\\'