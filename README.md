
# 🚀 AI Flask App with Kubernetes Deployment

This project demonstrates how to containerize a Flask-based AI application, push it to Docker Hub, and deploy it on a local Kubernetes cluster using Minikube. Ideal for DevOps learners integrating AI, Docker, and K8s in real-world workflows.

---

## 📁 Project Structure

```

ai-flask-kubernetes/
├── app/
│   ├── app.py                  # Flask backend
│   └── requirements.txt        # Python dependencies
├── Dockerfile                  # For building Docker image
├── deployment.yaml             # Kubernetes Deployment spec
├── service.yaml                # Kubernetes Service (NodePort)
└── README.md                   # You're reading it!

````

---

## 🔧 Step-by-Step Setup

### 1. ✅ Create and Test Flask App

Inside `app/app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "🚀 AI mode is alive"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
````

Install dependencies:

```bash
pip install flask
```

Test it locally:

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 2. 🐳 Dockerize the Flask App

**Dockerfile**

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app/ /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and tag the image:

```bash
docker build -t lavanyajc/ai-flask:latest .
```

Test it locally (optional):

```bash
docker run -p 5000:5000 lavanyajc/ai-flask:latest
```

---

### 3. 📤 Push Docker Image to Docker Hub

Login:

```bash
docker login
```

Push:

```bash
docker push lavanyajc/ai-flask:latest
```

---

### 4. ☸️ Setup Kubernetes with Minikube

Start minikube:

```bash
minikube start
```

Enable Docker-env if needed:

```bash
eval $(minikube docker-env)
```

---

### 5. 📦 Kubernetes Deployment

**deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-flask-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ai-flask
  template:
    metadata:
      labels:
        app: ai-flask
    spec:
      containers:
      - name: ai-flask-container
        image: lavanyajc/ai-flask:latest
        ports:
        - containerPort: 5000
```

Apply it:

```bash
kubectl apply -f deployment.yaml
```

Check pods:

```bash
kubectl get pods
```

---

### 6. 🌐 Kubernetes Service (NodePort)

**service.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ai-flask-service
spec:
  type: NodePort
  selector:
    app: ai-flask
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30007
```

Apply service:

```bash
kubectl apply -f service.yaml
```

List services:

```bash
kubectl get service
```

---

### 7. 🌍 Access the App via Minikube

Open service in browser:

```bash
minikube service ai-flask-service
```

Or visit manually:

```bash
http://127.0.0.1:<tunnel-port>
```

> Output: `🚀 AI mode is alive`

---

## 🧼 Cleanup

```bash
kubectl delete deployment ai-flask-deployment
kubectl delete service ai-flask-service
minikube stop
```

---

## 🤖 Tech Stack

* Python 3.9
* Flask
* Docker
* Docker Hub
* Kubernetes
* Minikube (on Windows)
* GitHub

---

## 📌 Author

**Lavanya J C**
DevOps | AI | Cloud Enthusiast
[GitHub](https://github.com/Lavanyajc) | [LinkedIn](https://linkedin.com/in/lavanyajc22)

---

## 🌟 Future Plans

* Integrate OpenAI API
* Add CI/CD with GitHub Actions
* Deploy to GKE or AWS EKS

---
