# Setting Ansible Up

## Installation.
`~$ sudo apt update && sudo apt install ansible -y`

## Verifying Correct Installation.
`~$ ansible --version`

## Creating a Configuration File.
* Create the `ansible.cfg` file in the path `/etc/ansible/`
    - `~$ sudo mkdir -p /etc/ansible/`
    - Create the [`ansible.cfg`](ansible/ansible.cfg) file using either 'vi' or 'nano' or any text editor.
    
## Configure and Verify SSH Access to the Remote System.

## Create an Ansible Inventory File.
* Create an [`inventory.ini`](ansible/inventory.ini) file in the current working directory.
* Purpose : Defines the list of hosts to connect to, how to connect and other parameters for task automation on them.

## Testing Ansible Connectivity.
* Running the ping test : `~$ ansible -i inventory.ini servers -m ping`

## Wrting the requried Ansible Playbook.
* Playbooks are nothing but YML files which are used to define tasks.
* Written using text editors and saved with the `.yml` extension.
* To run a playbook : ```ansible-playbook -i inventory.ini <playbook-name>.yml```
