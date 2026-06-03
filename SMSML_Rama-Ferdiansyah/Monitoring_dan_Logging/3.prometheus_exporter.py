import psutil
from prometheus_client import start_http_server, Counter, Histogram, Gauge

# ==========================================
# 1. Mendefinisikan Metrics
# ==========================================

# A. Metrik Aplikasi (Model)
REQUEST_COUNT = Counter('model_request_count_total', 'Total jumlah request yang masuk ke model')
ERROR_COUNT = Counter('model_error_count_total', 'Total jumlah request yang error/gagal')
LATENCY = Histogram('model_prediction_latency_seconds', 'Waktu yang dibutuhkan untuk memproses satu prediksi (detik)')

# B. Metrik Sistem (Infrastruktur)
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Penggunaan CPU oleh sistem (%)')
MEMORY_USAGE = Gauge('system_memory_usage_percent', 'Penggunaan Memori oleh sistem (%)')

# ==========================================
# 2. Fungsi Pendukung
# ==========================================

def start_metrics_server(port: int = 8000) -> None:
    """
    Memulai server HTTP untuk mengekspos metrik ke Prometheus.
    """
    start_http_server(port)
    print(f"✅ Prometheus Exporter berhasil berjalan dan mengekspos metrik di http://localhost:{port}")

def update_system_metrics():
    """
    Membaca resource CPU dan RAM saat ini, lalu menyimpannya ke metrik Gauge.
    """
    CPU_USAGE.set(psutil.cpu_percent(interval=None))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
