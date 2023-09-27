Script: 0-current_working_directory
Description: Prints the absolute path name of the current working directory.

Script: 1-listit
Description: Displays the contents list of the current directory.

Script: 2-bring_me_home
Description: Changes the working directory to the user's home directory without using shell variables.

Script: 3-listfiles
Description: Displays current directory contents in a long format.

Script: 4-listmorefiles
Description: Displays current directory contents, including hidden files, using the long format.

Script: 5-listfilesdigitonly
Description: Displays current directory contents in long format with user and group IDs displayed numerically, including hidden files.

Script: 6-firstdirectory
Description: Creates a directory named my_first_directory in the /tmp/ directory.

Script: 7-movethatfile
Description: Moves the file betty from /tmp/ to /tmp/my_first_directory.

Script: 8-firstdelete
Description: Deletes the file betty from /tmp/my_first_directory.

Script: 9-firstdirdeletion
Description: Deletes the directory my_first_directory from the /tmp directory.

Script: 10-back
Description: Changes the working directory to the previous one.

Script: 11-lists
Description: Lists all files, including hidden ones, in the current directory, the parent of the working directory, and the /boot directory (in this order), in long format.

Script: 12-file_type
Description: Prints the type of the file named ‘iamafile’, which will be located in the /tmp directory when the script is run.

Script: 13-symbolic_link
Description: Creates a symbolic link to /bin/ls named __ls__ in the current working directory.

Script: 14-copy_html
Description: Copies all HTML files from the current working directory to the parent of the working directory, but only if the files don't exist in the parent directory or are newer.


Make sure to follow the specific requirements mentioned in each task, including the script naming conventions, file permissions, and the system (Ubuntu 20.04 LTS) on which the scripts will be tested.
Remember to keep each script exactly two lines long, with the appropriate shebang line, and ensure that all files end with a new line. For testing, use the provided examples as a reference.
Have fun completing these shell scripting tasks!

