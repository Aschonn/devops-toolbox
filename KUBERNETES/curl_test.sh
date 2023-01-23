# this file tests whether an webapp is running
url=$1

for i in {1..20}; do
    kubectl exec --namespace=kube-public curl -- sh - c 'test=`wget -qO- -T 2 $url 2>&1` && echo "$test OK" || echo "Failed"';
    echo ""
done