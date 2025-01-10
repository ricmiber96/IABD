# Imagen base de Hadoop con Java
FROM bde2020/hadoop-base:2.0.0-hadoop2.7.4-java8
# Instalar dependencias y descargar Flume
RUN apt-get update && apt-get install -y wget \
 && wget https://downloads.apache.org/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz \
 && tar -xzf apache-flume-1.9.0-bin.tar.gz -C /usr/local/ \
 && mv /usr/local/apache-flume-1.9.0-bin /usr/local/flume \
 && rm apache-flume-1.9.0-bin.tar.gz
# Configurar variables de entorno
ENV FLUME_HOME=/usr/local/flume
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$FLUME_HOME/bin:$HADOOP_HOME/bin
# Copiar archivo de configuración de Flume
COPY flume-conf.properties $FLUME_HOME/conf/
# Exponer puertos necesarios
EXPOSE 44444 8042 8088 9870
# Comando por defecto para iniciar bash
CMD ["bash"]