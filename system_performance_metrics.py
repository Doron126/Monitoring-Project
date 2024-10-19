from prometheus_client import start_http_server, Gauge
import psutil
import time

resource_monitoring_metric = Gauge('system_performance', 'System performance metrics for CPU and memory',
                                   ['resource_type'])

def update_metrics():
    while True:
        memory_info = psutil.virtual_memory()
        memory_usage_percent = memory_info.percent
        resource_monitoring_metric.labels(resource_type='memory_usage_percent').set(memory_usage_percent)

        cpu_usage_percent = psutil.cpu_percent(interval=1)
        resource_monitoring_metric.labels(resource_type='cpu_usage_percent').set(cpu_usage_percent)

        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    print("Serving metrics on http://localhost:8000")

    update_metrics()
