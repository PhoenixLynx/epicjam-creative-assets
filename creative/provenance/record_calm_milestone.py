from pathlib import Path
import wave,json,hashlib,datetime,gzip,xml.etree.ElementTree as ET
import numpy as np
root=Path(__file__).resolve().parents[2]
src=root/'OriginalCompositions/PhoenixLynx - Halycion_Melody_Calm_48KHz_11-14_2026.wav'
data=src.read_bytes(); digest=hashlib.sha256(data).hexdigest()
with wave.open(str(src),'rb') as w:
    rate=w.getframerate(); width=w.getsampwidth(); channels=w.getnchannels(); frames=w.getnframes(); raw=w.readframes(frames)
assert len(raw)==frames*channels*width, 'Incomplete WAV payload'
assert width==3, 'Expected 24-bit PCM; inspect before proceeding'
b=np.frombuffer(raw,dtype=np.uint8).reshape(-1,3).astype(np.int32)
v=b[:,0]|(b[:,1]<<8)|(b[:,2]<<16); v=(v^0x800000)-0x800000
audio=v.reshape(-1,channels)/8388608.; mono=audio.mean(axis=1)
n=32768; hop=16384; freq=np.fft.rfftfreq(n,1/rate); idx=np.flatnonzero((freq>=65)&(freq<=2100))
pc=np.rint(69+12*np.log2(freq[idx]/440)).astype(int)%12
chromas=[]; win=np.hanning(n)
for start in range(0,len(mono)-n,hop):
    spectrum=abs(np.fft.rfft(mono[start:start+n]*win))
    peaks=(spectrum[idx]>spectrum[idx-1])&(spectrum[idx]>=spectrum[idx+1])
    c=np.bincount(pc,weights=np.sqrt(spectrum[idx])*peaks,minlength=12)
    if c.sum()>0: chromas.append(c/c.sum())
major=[6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]
minor=[6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17]
names=['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']
def rank(c):
    return sorted([dict(key=names[k]+' '+mode,correlation=float(np.corrcoef(c,np.roll(profile,k))[0,1])) for mode,profile in [('major',major),('minor',minor)] for k in range(12)],key=lambda x:-x['correlation'])[:5]
analysis=dict(rate_hz=rate,pcm_bits=width*8,channels=channels,frames=frames,duration_seconds=frames/rate,sample_peak_dbfs=float(20*np.log10(abs(audio).max())),rms_dbfs=float(20*np.log10(np.sqrt(np.mean(audio**2)))),full_scale_samples=int(np.sum(abs(v)>=8388607)),key_candidates=rank(np.mean(chromas,axis=0)),key_by_thirds=[rank(np.mean(c,axis=0))[:2] for c in np.array_split(np.array(chromas),3)],method='Native-rate FFT local-peak pitch-class profile, 32768 frame/16384 hop, 65-2100Hz, square-root magnitude weighting, major/minor profile correlation.',limitations='Rough spectral estimate, not listening or transcription. Harmonics and mix can bias key. Scores are correlations, not probabilities. Sample peak is not true peak; no LUFS measurement. Loop seams not tested.')
dest=root/'creative/audio/source/MUS-011_calm_milestone_2026-11-15T024521Z'; dest.mkdir(parents=True,exist_ok=False)
inputs=[(src,dest/src.name)]
project=root/'Halycion Project'; als=project/'Halycion_Melody_Calm.als'
inputs.append((als,dest/'Halycion Project'/als.name))
inputs += [(p,dest/'Halycion Project'/p.relative_to(project)) for p in (project/'Samples').rglob('*') if p.is_file() and p.suffix.lower() in ['.wav','.aif','.aiff','.flac']]
records=[]
for p,t in inputs:
    content=p.read_bytes(); sha=hashlib.sha256(content).hexdigest();t.parent.mkdir(parents=True,exist_ok=True);t.write_bytes(content)
    assert hashlib.sha256(t.read_bytes()).hexdigest()==sha and hashlib.sha256(p.read_bytes()).hexdigest()==sha
    records.append(dict(source=str(p.relative_to(root)),snapshot=str(t.relative_to(root)),sha256=sha,bytes=len(content)))
assert hashlib.sha256(src.read_bytes()).hexdigest()==digest, 'Render changed during analysis'
xml=ET.fromstring(gzip.decompress((dest/'Halycion Project'/als.name).read_bytes()))
record=dict(asset_id='MUS-011-CALM-MILESTONE-001',descriptive_filename=str(src.relative_to(root)),purpose='Human calm melody source candidate; not yet approved game loop',human_contributors=['PhoenixLynx: composition/render; confirms same 62 BPM and suggests C minor'],ai_systems_and_tools=['Sol / ChatGPT: archival copy, metadata and spectral analysis only','Python wave/numpy/hashlib/XML'],original_creation_utc=None,first_observed_utc='2026-11-15T02:45:21Z',snapshot_recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),timestamp_limits='Clock tool observation time, not proof of original composition date or independent timestamp certificate',completion_evidence='Stable size/mtime across observations; user confirmed render is there; full declared WAV payload read; hash unchanged after analysis and copy',source_prompts=['User requests formal asset recording and key estimate after render finishes'],settings=dict(ableton_creator=xml.get('Creator'),bpm_human=62,tempo_manual_values=[e.attrib for e in xml.findall('.//Tempo/Manual')],audio=analysis),input_references_and_dependencies=sorted(set(e.get('Value') for e in xml.findall('.//FileRef/RelativePath') if e.get('Value'))),dependency_limits='Only available collected samples copied; external presets/plugins not copied. Source-to-render association inferred from naming/timing; not reproduced.',origin_classification='User-created calm composition; dependency attribution pending human confirmation',license_and_attribution='No public license granted; sample/preset rights and pre-jam source material not yet confirmed',revision_history=['First calm render snapshot; original unchanged'],git_commit_hash=None,sha256=digest,files=records,integration_status='Archived source candidate; format verified, human creative approval and loop test pending')
(root/'creative/provenance/MUS-011_calm_milestone_001.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
(root/'creative/provenance/MUS-011_calm_audio_analysis.json').write_text(json.dumps(analysis,indent=2),encoding='utf-8')
(dest/'SHA256SUMS.txt').write_text('\n'.join(f"{r['sha256']}  {r['snapshot']}" for r in records)+'\n',encoding='utf-8')
print(json.dumps(analysis,indent=2));print('Preserved files:',len(records));print('Render SHA256:',digest)
