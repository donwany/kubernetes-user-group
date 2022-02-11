### Downloads
```shell
## Docker
https://www.docker.com/products/docker-desktop
## Minikube
https://minikube.sigs.k8s.io/docs/start/
## kubectl
https://kubernetes.io/docs/tasks/tools/
```
### Build and Tag Image
```shell
docker build -t worldbosskafka/fraud:1.0.2 .
docker images
docker container ls
docker ps
```
### Exec into Container
```dockerfile
 docker exec -it <CONTAINER_NAME:cb215fa030de> sh
```
### Run Container/Test Locally
```shell
docker run -p 23321:23321 fraud:1.0.2
curl http://localhost:23321/fraud
curl http://127.0.0.1:23321/fraud
```
### Push to DockerHub
```shell
docker login
docker push worldbosskafka/fraud:1.0.2
```
### Deploy to Kubernetes
```shell
kubectl create namespace fraud
kubectl config set-context --current --namespace=fraud

kubectl run fraud \
--image=worldbosskafka/fraud:1.0.2 \
--dry-run=client \
--port=5000 \
-o yaml > flask-pod.yaml

kubectl create deployment fraud-deployment \
--image=worldbosskafka/fraud:1.0.2 \
--port=23321 -n fraud \
--dry-run=client \
-o yaml > fraud-deployment.yaml

kubectl apply -f fraud-namespace.yaml -n fraud
kubectl apply -f flask-pod.yaml -n fraud

kubectl apply -f fraud-deployment.yaml -n fraud
kubectl apply -f fraud-service.yaml -n fraud
kubectl apply -f fraud-service.json -n fraud
```
### Expose Service to outside world
```shell
 kubectl expose deployment fraud-deployment \
 --port 23321 \
 --target-port 23321 \
 --type=NodePort \
 -o yaml
 
 $ kubectl get service -o wide
 $ minikube service fraud-deployment --url -n fraud
 
 $ minikube ip
```
### Python API Request
```python
import requests

url = "http://192.168.1.245:23321/fraud"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
### Java
```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("http://192.168.1.245:23321/fraud")
  .method("GET", null)
  .build();
Response response = client.newCall(request).execute();
```
### CURL
```shell
curl --location --request GET 'http://192.168.1.245:23321/fraud'
```
