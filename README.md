# javadevops-poc

To build the application:
docker build -t sample javadevops-poc/ <br>
To run the application:
docker run -dit --name sample -p 8084:8080  sample<br>
Application url: http://{HOSTNAME}:8084/hello/{greetings}
