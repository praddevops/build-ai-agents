# Prereq

1. Go to ollama.com and download the appropriate ollama package for your OS and cpu architecture



### Installation:
`curl -fsSL https://ollama.com/install.sh | sh`

### Update Ollama:
Update Ollama by running the install script again:

### Uninstall Ollama:

#### Remove the ollama service:
```
sudo systemctl stop ollama
sudo systemctl disable ollama
sudo rm /etc/systemd/system/ollama.service
```

#### Remove ollama libraries from your lib directory (either /usr/local/lib, /usr/lib, or /lib):
`sudo rm -r $(which ollama | tr 'bin' 'lib')`

#### Remove the ollama binary from your bin directory (either /usr/local/bin, /usr/bin, or /bin):

`sudo rm $(which ollama)`

#### Remove the downloaded models and Ollama service user and group:

```
sudo userdel ollama
sudo groupdel ollama
sudo rm -r /usr/share/ollama
```



## Troubleshooting:
### Viewing logs
To view logs of Ollama running as a startup service, run:
`journalctl -e -u ollama`

## Integrations
https://docs.ollama.com/integrations/vscode


## References:

https://docs.ollama.com/cli
https://docs.ollama.com/linux

