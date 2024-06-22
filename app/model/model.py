import onnxruntime as _ort
from onnxruntime_extensions import get_library_path as _lib_path
from hezar.models import Model
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

def speech_to_text(voice):
    ASR = Model.load("hezarai/whisper-small-fa")
    transcripts = ASR.predict(voice)
    return transcripts

def sentiment_classifier(text):
    labels = {
        0 : 'happy',
        1 : 'sad'
    }

    so = _ort.SessionOptions()
    so.register_custom_ops_library(_lib_path())

    # Run the ONNXRuntime Session as per ONNXRuntime docs suggestions.
    sess = _ort.InferenceSession(f"{BASE_DIR}/parsbert_quant_with_pre_post_processing.onnx", so)

    # Run inference
    input_name = sess.get_inputs()[0].name
    output_name = sess.get_outputs()[0].name
    model_output = sess.run([output_name], {input_name: [[text]]})
    label = labels[model_output[0].argmax()]
    return label