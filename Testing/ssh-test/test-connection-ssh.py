from pyats.topology import loader
# Step 0: load the testbed
testbed = loader.load(f'./testbed-ssh.yaml')

# Step 1: testbed is a dictionary. Extract the device iol-test
ios1 = testbed.devices["Test-IOS"]

# Step 2: Connect to the device
ios1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

# Step 3: saving the `show ip interface brief` output in a variable
show_interface = ios1.execute('show ip interface brief')

# Step 4: printing the `show interface brief` output
print(show_interface)

# Step 5: disconnect from the device
ios1.disconnect()