This is the directory of the shell permissions project. You can find scripts for enable/disable/remove permissions.

0-iam_betty
	Switch the current user to the user betty

1-who_am_i
	Print the effective username of the current user

2-groups
	Print all the groups the current user is part of

3-new_owner
	Change the owner of the file hello to the user betty

4-empty
	Create an empty fille called hello

5-execute
	Add execute permission to the owner of the file hello

6-multiple_permissions
	Add execute permission to the owner and the groupe owner, and read permission to other users, to the file hello

7-everybody
	Add execute permission to the owner, the groupe owner and the other users, to the file hello

8-James_Bond
	No permission to owner and owner group, set all the permission to other users, to the file hello

9-John_Doe
	Set all the permissions to owner, read and execute permission to owner group and write and execute permission to other users, to the file hello

10-mirror_permissions
	Set the mode of the file hello the same as olleh's mode

11-directories_permissions
	Add execute permission to all subdirectories of the current directory for the owner, owner group and all other users

12-directory_permissions
	Create a directory called my_dire with permissions : all for owner, read and execute for owner group, execute for all other users

13-change_group
	Change the groupe owner to school for the file hello

100-change_owner_and_group
	Change the owner to vincent and the group owner to staff for all the files and directories in the working directory

101-symbolic_link_permissions
	Change the owner and the group owner of _hello to vincent and staff

102-if_only
	Change the owner of the file hello to vincent only if it is owned by the user guillaume

103-Star_Wars
	Play the StarWars IV episode in the terminal
