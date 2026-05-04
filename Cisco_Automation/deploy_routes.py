from netmiko import ConnectHandler

# This list contains the "Inventory" of your network
# For your BSc IT project, we use the specific IPs you've set up
routers = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.10.1',  # Replace with the actual IP of Router0
        'username': 'admin',
        'password': 'cisco',
        # These are the commands that the script will push automatically
        'config_commands': [
            'ip route 192.168.20.0 255.255.255.0 10.0.0.2',
            'ip route 192.168.30.0 255.255.255.0 10.0.0.2'
        ]
    }
    # You can add Router1 and Router2 here as well
]

def apply_network_config(device_list):
    for device in device_list:
        print(f"--- Attempting to automate {device['host']} ---")
        
        # We separate the commands from the connection parameters
        connection_params = {
            'device_type': device['device_type'],
            'host': device['host'],
            'username': device['username'],
            'password': device['password'],
        }
        
        try:
            # MODE 1: Establishing SSH Connection (User Exec Mode)
            net_connect = ConnectHandler(**connection_params)
            
            # MODE 2: Configuration Mode
            # .send_config_set() automatically enters 'conf t' and exits it
            print(f"Pushing Static Routes to {device['host']}...")
            output = net_connect.send_config_set(device['config_commands'])
            print(output)
            
            # MODE 3: Privileged EXEC Mode (Saving)
            # This is the equivalent of 'write memory' or 'copy run start'
            net_connect.save_config()
            print(f"Configuration saved successfully on {device['host']}\n")
            
            # Disconnect safely
            net_connect.disconnect()
            
        except Exception as e:
            print(f"Failed to connect to {device['host']}. Error: {e}")

if __name__ == "__main__":
    apply_network_config(routers)