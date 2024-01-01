create folders:
config_folder1.txt - conatin path to config folder , example "c:\img_bg_clean_config1"

c:\img_bg_clean_config1 contain 2 files:
root_path1.txt - contain path to root folder of images , example "c:\memomi_folder2\glass_pics_8\"
file_path1.txt - contan path to image for proceessing , example "980376340_2\195768205504__A"

for create first sobel data for one image have to set 2 flags in cform1:
self.compute_sobel=True        
self.compute_sobel_imgs1=True