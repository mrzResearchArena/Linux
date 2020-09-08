# GPU Setup:

##### Step 1: Initialization
```console
user@machine:~$ LAMBDA_REPO=$(mktemp) && wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && sudo apt-get update && sudo apt-get install -y lambda-stack-cuda
```

##### Step 2: Reboot / Restart
```console
user@machine:~$ sudo reboot # Run after 3-4 minutes.
```

##### Step 3: Nvidia Initialization
```console
user@machine:~$ sudo docker build -t lambda-stack -f Dockerfile.$(lsb_release -cs) git://github.com/lambdal/lambda-stack-dockerfiles.git
```

##### Step 4: Nvidia Installation
```console
user@machine:~$ LAMBDA_REPO=$(mktemp) && wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && sudo apt-get update && sudo apt-get --yes upgrade && sudo apt-get install --yes --no-install-recommends lambda-server && sudo apt-get install --yes --no-install-recommends nvidia-440 libcuda1-440 nvidia-opencl-icd-440 && sudo apt-get install --yes --no-install-recommends lambda-stack-cuda
```

##### Step-5: Reboot / Restart (Again)
```console
user@machine:~$ sudo reboot # Run after 3-4 minutes.
```
