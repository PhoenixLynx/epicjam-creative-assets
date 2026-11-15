from pathlib import Path
import wave,json,numpy as np
root=Path(__file__).resolve().parents[2]
p=root/'OriginalCompositions/PhoenixLynx - Halycion_Melody_Positive_11-14_2026.wav'
with wave.open(str(p),'rb') as w:
    rate=w.getframerate(); channels=w.getnchannels(); frames=w.getnframes()
    audio=np.frombuffer(w.readframes(frames),dtype='<i2').reshape(-1,channels).astype(float)/32768
mono=audio.mean(axis=1)[::4]; sr=rate/4
n=8192; hop=4096; freq=np.fft.rfftfreq(n,1/sr)
valid=(freq>=65)&(freq<=2100)
idx=np.flatnonzero(valid); midi=69+12*np.log2(freq[idx]/440)
pitch=np.rint(midi).astype(int)%12
window=np.hanning(n); chromas=[]
for start in range(0,len(mono)-n,hop):
    spec=abs(np.fft.rfft(mono[start:start+n]*window))
    peaks=(spec[idx]>spec[idx-1])&(spec[idx]>=spec[idx+1])
    weights=np.sqrt(spec[idx])*peaks
    c=np.bincount(pitch,weights=weights,minlength=12)
    if c.sum()>0:chromas.append(c/c.sum())
chroma=np.mean(chromas,axis=0)
major=np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
minor=np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
names=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
scores=sorted([dict(key=names[k]+' '+mode,correlation=float(np.corrcoef(chroma,np.roll(profile,k))[0,1])) for mode,profile in [('major',major),('minor',minor)] for k in range(12)],key=lambda x:-x['correlation'])
peak=float(np.max(abs(audio))); rms=float(np.sqrt(np.mean(audio**2)))
out=dict(file=str(p.relative_to(root)),sample_rate_hz=rate,pcm_bits=16,channels=channels,duration_seconds=frames/rate,bpm_human_confirmed=62,bpm_ableton_manual=62,key_candidates=scores[:5],pitch_class_strength=dict(zip(names,map(float,chroma))),sample_peak_dbfs=float(20*np.log10(peak)),rms_dbfs=float(20*np.log10(rms)),full_scale_samples=int(np.sum(abs(audio)>=32767/32768)),method='Read-only numpy FFT local-peak chroma, square-root spectral weighting, major/minor profile correlation; 65-2100 Hz, 8192 frame, 4096 hop, downsample4. Tempo not estimated from audio.',limitations='Rough tonal estimate, not a transcription or listening judgment. Harmonics/drums/mix and unfiltered downsampling can bias scores. Correlation is not probability. No LUFS or true-peak measurement. No audio modified.')
(root/'creative/provenance/MUS-001_happy_audio_analysis.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
