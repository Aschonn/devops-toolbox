# install meant for linux 

version=$1

cd $HOME

# check if you are running root. if not it will exit
if [ "EID" -ne 0 ]
then
        echo "please run as root"
        exit 1
fi

if [ $version ]
then
        curl -LO "https://dl.k8s.io/release/$version/bin/linux/amd64/kubectl"
else

        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
fi

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl


echo "Kubernetes Has Been Successfully Installed"

kubectl version --client --output=yaml