# 0x01-shell_permissions

This project contains a series of shell scripts that demonstrate various aspects of file permissions in a Unix-like shell environment. Each script is designed to perform specific tasks related to file ownership, group permissions, and access control.

Below is a brief description of each script and its purpose:

## 0-iam_betty
This script switches the current user to the user "betty" using the `su` command. It's designed to change the active user to "betty."

## 1-who_am_i
This script prints the effective username of the current user using the `whoami` command. It provides a simple way to determine the currently logged-in user.

## 2-groups
This script prints all the groups the current user is a part of using the `groups` command. It displays a list of groups associated with the user.

## 3-new_owner
This script changes the owner of the file "hello" to the user "betty" using the `chown` command. It demonstrates how to modify file ownership.

## 4-empty
This script creates an empty file called "hello" using the `touch` command. It showcases how to create files in the shell.

## 5-execute
This script adds execute permission to the owner of the file "hello" using the `chmod` command. It illustrates how to modify file permissions.

## 6-multiple_permissions
This script adds execute permission to the owner and the group owner and read permission to other users for the file "hello" using the `chmod` command. It demonstrates how to set multiple permissions.

## 7-everybody
This script adds execution permission to the owner, the group owner, and other users for the file "hello" using the `chmod` command. It grants universal execute access.

## 8-James_Bond
This script sets specific permissions for the file "hello": no permission for the owner and group owner, and all permissions for other users using the `chmod` command. It showcases fine-grained permission control.

## 9-John_Doe
This script sets a custom mode for the file "hello," changing the permissions for the owner, group owner, and others using the `chmod` command. It offers flexibility in permission management.

## 10-mirror_permissions
This script sets the mode of the file "hello" to match the mode of the file "olleh" using the `chmod` command. It synchronizes permissions between two files.

## 11-directories_permissions
This script adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users, while leaving regular files unchanged. It demonstrates directory-specific permission modification.

## 12-directory_permissions
This script creates a directory called "my_dir" with permissions 751 (read, execute, and search for owner; execute and search for group; no permissions for others) in the working directory using the `mkdir` and `chmod` commands.

## 13-change_group
This script changes the group owner of the file "hello" to "school" using the `chown` command. It showcases group ownership modification.

## 100-change_owner_and_group
This advanced script changes the owner to "vincent" and the group owner to "staff" for all files and directories in the working directory using the `chown` command. It demonstrates bulk ownership and group ownership modification.

## 101-symbolic_link_permissions
This advanced script changes the owner and group owner of the symbolic link "_hello" to "vincent" and "staff," respectively, using the `chown` command. It addresses symbolic link permissions.

## 102-if_only
This advanced script changes the owner of the file "hello" to "betty" only if it is currently owned by the user "guillaume" using conditional logic and the `chown` command.

## 103-Star_Wars
This script is not code-related but is intended to play the Star Wars IV episode in the terminal, providing a fun and unique shell experience.

Feel free to explore these scripts to learn more about shell permissions and how to manage file and directory access control in a Unix-like environment.

