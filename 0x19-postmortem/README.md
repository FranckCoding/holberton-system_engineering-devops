# PostMortem

## Issue Summary

01 june 2021, 10h30 to 11h00. </br>
Some users create tickets to report a bug with the discord bot. When the user type a command in the discord chat. The bot give the message of an error, where the bot can't find the command. </br>
The cause of that, it's the config file of the bot it was deleted. The solution is to create a new config file with new Token for discord.

## Timeline

10H00 - The firts tickets was send by the users. </br>
10H30 - The issue is relieve to the production team. The prod' team investigate to this issue. </br>
10H50 - The origin of the issue is find, it's the config file it was deleted when the develop branch it was merged in main branch. A dev have deleted accidently the config file in a feature branch. </br>
11H00 - The new config file is created and merged in the main branch.

## Root Cause

A dev deleted the config file accidently, when he worked in a feature of the bot. This deletion was merged in main branch. </br>
A new config file is created by another dev, with new tokens and config.

## Corrective and Preventative measures.

To avoid another deletion of files. Reauthorize the system to send a message when you do the deletion. </br>
Next, assign a dev to code review and verify if a mistake is not in a develop branch.
