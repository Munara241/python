# import digitalocean


# def create_droplet(token, ssh_key_fingerprint):
#    manager = digitalocean.Manager(token=token)
#    # Specify the SSH key to use by its fingerprint or ID
#    ssh_key = [ssh_key_fingerprint]  # You can add multiple keys here if needed


#    droplet = digitalocean.Droplet(token=token,
#                                   name= name,
#                                   region='nyc1',  # Choose a region
#                                   image='ubuntu-20-04-x64',  # Ubuntu 20.04 image
#                                   size_slug='s-1vcpu-1gb',  # Droplet size
#                                   ssh_keys=ssh_key,  # Use a specific SSH key
#                                   backups=False)
#    droplet.create()
#    return droplet


# if __name__ == '__main__':
#    token = ''
#    ssh_key_fingerprint = ''
#    droplet_names = ['kaizen', 'Hello', 'World']


# for name in droplet_names:
#    droplate = create_droplet(token, ssh_key_fingerprint)
#    print(f"Droplet {name} is being created") 
