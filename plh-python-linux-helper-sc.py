
import subprocess
import os

print("Checking if the working directory exists...")
user_dir = os.path.expanduser("~")
working_dir = os.path.join(user_dir, "plh")
if os.path.isdir(working_dir) == True:
    print("Working directory found.")
elif os.path.isdir(working_dir) == False:
    print("Working directory not found.")
    print("Making a new working directory...")
    os.mkdir(working_dir)
    print("Made a new directory.")
print("Changing to the supposed working directory...")
os.chdir(working_dir)
print("Changed the working directory.")
print("Checking plhconf files...")
for i in range(1, 11):
    filename = "plhconf" + str(i) + ".txt"
    if os.path.exists(filename) == True:
        print(filename + " found.")
    elif os.path.exists(filename) == False:
        print(filename + " not found.")
        print("Making a new config file...")
        open(filename, "w").close()
print("Check complete.")

print("PLH V1.0T")
print()
print("Type 'help' to show the list of all available commands.")
print()

while True:
    plhshell = input("plh>")
    if plhshell == "help":
    	print("run plhconf[number].txt -- runs the selected config file.")
    	print("inspect plhconf[number].txt -- prints everything inside the selected config file.")
    	print("edit plhconf[number].txt -- enters the editor and lets you edit the selected config file.")
    	print("usg -- explains how to use plh. ")
    	print("exit -- exits plh")
    	print("clear plhconf[number].txt -- empties the config file.")
    if plhshell == "usg":
    	print("First, open the editor and edit one config file.")
    	print("Second, in the editor, type command by command, a command needs its own line")
    	print()
    	print("Ex:")
    	print("sudo apt update")
    	print("sudo apt upgrade")
    	print("echo 'Updating finished.'")
    	print()
    	print("Then save the file and run it using the 'run' command.")
    	print("Note: with this version you cannot load config files and edit them in plh, though you can with nano or vim. If you are willing to reuse a config file, use the clear command.")
    if plhshell.startswith("edit "):
    	plh_edittarg = plhshell[5: ]
    	print("Opening the editor shell...")
    	print()
    	print("Type 'exit' to exit the editor shell without saving.")
    	print("Type 'save' to exit the editor and save")
    	print()
    	plhedtmp = []
    	
    	while True:
    		plhedshell = input("plhed>")
    		if plhedshell == "save":
    			with open(plh_edittarg, "w") as file:
    				for line in plhedtmp:
    					file.write(line + "\n")
    			del plhedtmp
    			break
    		elif plhedshell == "exit":
    			del plhedtmp
    			break
    		elif plhedshell != "exit" and plhedshell != "save":
    			plhedtmp.append(plhedshell)
    elif plhshell.startswith("inspect "):
    	plh_inspecttarg = plhshell[8: ]
    	with open(plh_inspecttarg, "r") as file:
    		plhcfc = file.read()
    	print(plhcfc)			
    elif plhshell == "exit":
    	print("Exiting...")
    	break
    elif plhshell.startswith("clear "):
    	plh_cleartarg = plhshell[6: ]
    	print("Emptying the file...")
    	with open(plh_cleartarg, "w") as file:
    		pass
    	print("File emptied.")
    elif plhshell.startswith("run "):
    	plh_runtarg = plhshell[4: ]
    	with open(plh_runtarg, "r") as file:
    		plh_fcffr = file.read()
    	result = subprocess.run(
    		plh_fcffr,
    		shell=True,
    	)
    	
