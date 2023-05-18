"""
https://github.com/openai/whisper
# How to make a virtual python env for your project.
> python -m venv venv
>
On Windows: venv\Scripts\activate.bat
On Unix or Linux: source venv/bin/activate
> pip install whisper
> deactivate
"""
import whisper

# ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large']
# print(whisper.available_models())
model = whisper.load_model("base")
result = model.transcribe("/Users/khaledlela/Downloads/audio.mp3", fp16=False)
print(result["text"])

# model = whisper.load_model("medium")

# load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("/Users/khaledlela/Downloads/audio.mp3")
# audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)
# model = whisper.load_model("medium")
# result = model.transcribe(audio, fp16=False)


# print the recognized text
# print(result["text"])