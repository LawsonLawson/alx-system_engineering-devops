## Command line for the win

# Steps I followed to use the SFTP command-line tool for this project.

# 1
- After taking the screenshots, I highlighted the respective levels
for each file and made sure I had them in the `command_line_for_the_win`
directory locally.

# 2
- On my local machine and present working directory being
`/home/lawson/ALX/alx-system_engineering-devops`,I copied and pasted the SFTP
link as well as the password from the intranet respectively, hitting `Enter`
key in both cases in order to be connected to the virtual machine.

# 3
- After the connection was secured, I used `pwd` command to be sure of where I
was, which in my case was `/`.

# 4
- I then used the `cd` command to navigate to the `alx-system_engineering-devops`
directory.

# 5
- I run an `ls` to see the contents of the directory. In this case, it had everything
from before with the exception of the `command_line_for_the_win` directiory.

# 6
- I used the `put` command followed by the directory I was copying recursively and the path
I want to upload to.
like this:
--- put -R command_line_for_the_win/ . ---
I used the `exit` to close the connection was now on my local space.

# 7
- I then now staged my files, committed and pushed them to
github per the instructions.
