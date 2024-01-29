FROM adoptopenjdk/openjdk11:alpine-slim

COPY target/mkt-persistence-0.0.1-SNAPSHOT.jar app.jar

ENV JAVA_OPTS="-Xmx450m"

ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]

EXPOSE 8373