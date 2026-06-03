import time
import random
from prometheus_exporter import (
    start_metrics_server,
    update_system_metrics,
    REQUEST_COUNT,
    ERROR_COUNT,
    LATENCY
)

# Simulasi load model yang sudah dituning
print("Memuat model MLflow (Simulasi) dari eksperimen 'Latihan Credit Scoring Optimization'...")
time.sleep(2)  # simulasi waktu loading model
print("Model berhasil dimuat. Siap melayani request.")

def process_request():
    """Simulasi fungsi inference untuk menerima request."""
    # Mencatat metrik: ada 1 request masuk
    REQUEST_COUNT.inc()

    # Hitung waktu mulai prediksi
    start_time = time.time()

    # Simulasi waktu komputasi ML model inference
    time.sleep(random.uniform(0.1, 0.5))

    # Simulasi keberhasilan/kegagalan (95% sukses)
    if random.random() > 0.95:
        # Mencatat metrik error
        ERROR_COUNT.inc()
        # Mencatat latensi (walaupun error tetap dihitung waktunya)
        end_time = time.time()
        LATENCY.observe(end_time - start_time)
        raise Exception("Gagal memprediksi skor kredit")

    # Hitung dan catat metrik latensi untuk request sukses
    end_time = time.time()
    LATENCY.observe(end_time - start_time)

    # Kembalikan skor kredit acak dari 0-2 (sesuai target dataset jika ada)
    return random.randint(0, 2)

if __name__ == '__main__':
    # Start server Prometheus exporter di port 8000
    start_metrics_server(8000)

    # Simulasi menerima request secara terus-menerus
    while True:
        try:
            # Perbarui metrik penggunaan CPU dan RAM tiap iterasi
            update_system_metrics()

            # Panggil fungsi inference
            hasil = process_request()
            print(f"Prediksi berhasil dengan hasil: {hasil}")
        except Exception as e:
            print(f"Error prediksi: {e}")

        # Jeda antar request (0.5 hingga 2 detik)
        time.sleep(random.uniform(0.5, 2.0))

