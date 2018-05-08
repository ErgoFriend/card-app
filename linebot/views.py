from django.shortcuts import render
import paramiko
# Create your views here.

def index(request):
    if request.method == 'GET':
        k = "http://drive.google.com/uc?export=view&id=1_mCedTUusHIMJzvd8fUy9Q8d7Zkp2gtK"
        client = paramiko.SSHClient() 
        client.load_system_host_keys(k) 
        client.connect('ark-cg.com')
        stdin, stdout, stderr = client.exec_command('sh test.sh')
    return None