# find specify string from given string

png_file_name = "0343434_039222.png"

# method1
match = png_file_name.rfind('_') 
label = png_file_name[:match] #=> 0343434
image_id = png_file_name[match+1:-4] #=> 039222

# method 2
match = re.search(r'^(\d+)_(\d+)\.png$', png_file_name)
label = match.group(1) #=> 0343434
image_id = match.group(2) #=> 039222
