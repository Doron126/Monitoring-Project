# **Monitoring-Project**
## **Overview**
In this project I set up a free, real-time monitoring solution using Python, Prometheus, and Grafana.
The script builed a single metric in Prometheus that later it can be used on Grafana, that is collecting data on CPU and Memory usage.

## **Thecnologies Used**
* Python
* Python libaries: psutil, prometheus_client, time
* Prometheus
* Grafana

## **Instructions**
  1. SET up an Ubuntu server machine.
     
  2. Install python3 on your machine:
     "apt install python3 python3-pip"
     
  3. Create a virtual enviroment for the packages and install them:
     "python3 -m venv myenv"
     "source myenv/bin/activate"
     "pip install psutil prometheus_client"
     
  4. Install Prometheus:
     "wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz:
     "tar -xvzf prometheus-2.47.0.linux-amd64.tar.gz"
     
  5. Install Grafana:
     "apt-get install -y software-properties-common"
     "add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
     "apt-get update"
     "apt-get install grafana"
     "systemctl start grafana-server"
     "systemctl enable grafana-server"
     * Your Grafana should be now on http://localhost:3000, the default login credentials are admin/admin.
      
  6. Write and run the python script to create the metric in Prometheus:
     "nano monitoring_tool.py":
     copy the script of the project.
     "nohup python3 monitoring_tool.py > monitoring_tool.log 2>&1 &"

  7. Configure Prometheus and run it:
     "cd prometheus-2.47.0.linux-amd64"
     "nano prometheus.yml"
     Configure the scrape configuration to look like that:\
     "global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'python-monitoring'
    static_configs:
      - targets: ['localhost:8000']"
     Save the file and run Prometheus:
     "nohup ./prometheus --config.file=prometheus.yml > prometheus.log 2>&1 &"
     Now you should see Prometheus on http://localhost:9090 and the scrapinmg metric on http://localhost:8000,
     You can also query the metric name in Prometheus and see the result.

   8. Set up Grafana dashboard:
      Go to "Data sources" and add http://localhost:9090 as a data source.
      Go to "Dashboards" and Create a new dashboard using Prometheus as the datasource and the metric of the script named 'system_performance' as a metric.
      You can change the name of the metric by editing the first value inside the bracelet of the Gauge configuration in the script.


        
