### NetworkPolicy
```shell
kubectl run payment-processor --image=nginx --restart=Never \
    -l app=payment-processor,role=api --port 80
    
kubectl create -f networkpolicy-api.yaml  

kubectl get networkpolicy

######## Check to see if  coffeeshop can talk to payment processor
kubectl run coffeeshop --rm -it --image=busybox \
    --restart=Never -l app=coffeeshop,role=backend -- /bin/sh

wget --spider --timeout=1 <PAYMENT-PROCESSOR-IP>

######## Check to see if groceryshop can talk to payment processor
kubectl run grocery-store --rm -it --image=busybox \
    --restart=Never -l app=grocery-store,role=backend -- /bin/sh
    
wget --spider --timeout=1 <PAYMENT-PROCESSOR-IP>
```