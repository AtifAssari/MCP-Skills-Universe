---
title: fp16_int8_quantization
url: https://skills.sh/davidcastagnetoa/skills/fp16_int8_quantization
---

# fp16_int8_quantization

skills/davidcastagnetoa/skills/fp16_int8_quantization
fp16_int8_quantization
Installation
$ npx skills add https://github.com/davidcastagnetoa/skills --skill fp16_int8_quantization
SKILL.md
fp16_int8_quantization

Aplica técnicas de cuantización FP16 e INT8 a los modelos de machine learning del pipeline de verificación de identidad (ArcFace, MiniFASNet, YOLOv8) para reducir el consumo de memoria y acelerar la inferencia. Incluye calibración con datos representativos del dominio KYC para mantener la precisión de reconocimiento facial y detección de vida dentro de los umbrales aceptables.

When to use

Usa esta skill cuando necesites optimizar el tamaño y velocidad de los modelos ML dentro del model_server_agent. Aplica cuando los modelos en FP32 consumen demasiada memoria GPU/CPU o cuando la latencia de inferencia excede el objetivo de 8 segundos del pipeline completo de verificación.

Instructions

Evaluar el modelo original en FP32 como baseline, midiendo FAR, FRR y latencia:

from modules.face_match.evaluator import evaluate_model
baseline_metrics = evaluate_model("models/arcface_fp32.onnx", test_dataset)
print(f"FAR: {baseline_metrics['far']}, FRR: {baseline_metrics['frr']}, Latency: {baseline_metrics['latency_ms']}ms")


Aplicar cuantización FP16 para una reducción rápida de tamaño sin calibración:

from onnxruntime.transformers import float16
import onnx

model = onnx.load("models/arcface_fp32.onnx")
model_fp16 = float16.convert_float_to_float16(model, keep_io_types=True)
onnx.save(model_fp16, "models/arcface_fp16.onnx")


Preparar un dataset de calibración representativo para cuantización INT8 (mínimo 100-500 muestras de rostros y documentos reales):

class KYCCalibrationDataReader(CalibrationDataReader):
    def __init__(self, calibration_images_dir: str):
        self.data = self._load_and_preprocess(calibration_images_dir)
        self.iter = iter(self.data)

    def get_next(self):
        return next(self.iter, None)


Ejecutar cuantización INT8 estática con el dataset de calibración:

from onnxruntime.quantization import quantize_static, QuantType

quantize_static(
    model_input="models/arcface_fp32.onnx",
    model_output="models/arcface_int8.onnx",
    calibration_data_reader=KYCCalibrationDataReader("data/calibration/faces/"),
    quant_format=QuantFormat.QDQ,
    weight_type=QuantType.QInt8,
    activation_type=QuantType.QInt8
)


Comparar métricas del modelo cuantizado contra el baseline FP32:

quantized_metrics = evaluate_model("models/arcface_int8.onnx", test_dataset)
degradation = baseline_metrics['far'] - quantized_metrics['far']
assert degradation < 0.01, "Degradación de FAR inaceptable tras cuantización"


Si la degradación es excesiva, aplicar cuantización mixta excluyendo capas sensibles (primeras y últimas capas del modelo facial):

quantize_static(
    model_input="models/arcface_fp32.onnx",
    model_output="models/arcface_mixed.onnx",
    calibration_data_reader=calibration_reader,
    nodes_to_exclude=["first_conv", "final_fc", "bn_final"]
)


Generar un informe de comparación con tamaño del modelo, latencia y métricas de precisión para cada variante (FP32, FP16, INT8, mixta).

Notes
La cuantización INT8 requiere calibración con datos representativos del dominio KYC; usar imágenes genéricas puede degradar significativamente la precisión en rostros de documentos de identidad.
FP16 es generalmente seguro para modelos faciales con degradación mínima (<0.5% en FAR), mientras que INT8 requiere validación cuidadosa especialmente en el modelo de liveness detection.
Siempre mantener el modelo FP32 original como referencia y nunca desplegar un modelo cuantizado sin comparar métricas de FAR/FRR contra los umbrales definidos (FAR < 0.1%, FRR < 5%).
Weekly Installs
10
Repository
davidcastagnetoa/skills
First Seen
Mar 3, 2026