FROM openjdk:8
LABEL "Maintainer"="Demo"

RUN groupadd demo && adduser --quiet --home /opt/app --ingroup demo --gecos 'demo' --disabled-password demo
WORKDIR /opt/apps
COPY demo-0.0.1-SNAPSHOT.jar /opt/apps

RUN chown -R demo:demo /opt/apps
#
# RUNTIME
#
USER demo
EXPOSE 8080
ENTRYPOINT ["java","-jar","demo-0.0.1-SNAPSHOT.jar"]
