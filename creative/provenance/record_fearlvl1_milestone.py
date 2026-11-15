"""Archive user FearLvl1 render and available project dependencies unchanged."""
from pathlib import Path
import datetime,gzip,hashlib,json,wave,xml.etree.ElementTree as ET
import numpy as np
root=Path(__file__).resolve().parents[2]
src=root/'OriginalCompositions/PhoenixLynx - Halycion_Melody_FearLvL1_11-14_2026.wav'
project=root/'Halycion Project'; als=project/'Halycion_Melody_Fear.als'
dest=root/'creative/audio/source/MUS-FEARLVL1_milestone_2026-11-15T062201Z'
dest.mkdir(parents=True,exist_ok=False)
inputs=[(src,dest/src.name),(als,dest/'Halycion Project'/als.name)]
inputs += [(p,dest/'Halycion Project'/p.relative_to(project)) for p in (project/'Samples').rglob('*') if p.is_file() and p.suffix.lower() in ['.wav','.aif','.aiff','.flac']]
files=[]
for p,t in inputs:
    b=p.read_bytes(); digest=hashlib.sha256(b).hexdigest(); t.parent.mkdir(parents=True,exist_ok=True); t.write_bytes(b)
    assert hashlib.sha256(t.read_bytes()).hexdigest()==digest and hashlib.sha256(p.read_bytes()).hexdigest()==digest
    files.append(dict(source=str(p.relative_to(root)),snapshot=str(t.relative_to(root)),sha256=digest,bytes=len(b)))
with wave.open(str(dest/src.name),'rb') as w:
    rate=w.getframerate(); width=w.getsampwidth(); channels=w.getnchannels(); frames=w.getnframes(); raw=w.readframes(frames)
assert len(raw)==frames*width*channels
if width==3:
    b=np.frombuffer(raw,dtype=np.uint8).reshape(-1,3).astype(np.int32); a=b[:,0]|(b[:,1]<<8)|(b[:,2]<<16); a=((a^0x800000)-0x800000)/8388608.
elif width==2: a=np.frombuffer(raw,dtype='<i2').astype(float)/32768
else: raise ValueError('Inspect unsupported PCM width before proceeding')
xml=ET.fromstring(gzip.decompress((dest/'Halycion Project'/als.name).read_bytes()))
settings=dict(sample_rate_hz=rate,pcm_bits=width*8,channels=channels,frames=frames,duration_seconds=frames/rate,sample_peak_dbfs=float(20*np.log10(abs(a).max())),full_scale_samples=int(np.sum(abs(a)>=1-1/(2**(width*8-1)))),ableton_creator=xml.get('Creator'),tempo_manual_values=[e.attrib for e in xml.findall('.//Tempo/Manual')])
r=dict(asset_id='MUS-FEARLVL1-MILESTONE-001',descriptive_filename=str(src.relative_to(root)),purpose='Human FearLvl1 composition source milestone; gameplay cue mapping pending',human_contributors=['PhoenixLynx: supplied FearLvl1 composition and requested commit'],ai_systems_and_tools=['Sol / ChatGPT: read-only inspection, byte-preserving archive, metadata and hashes','Python wave/numpy/hashlib/XML'],original_creation_utc=None,first_observed_utc='2026-11-15T06:22:01Z',snapshot_recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),timestamp_limits='Observation time from clock tool, not original creation time or independent timestamp certificate',source_prompts=['User: I have a new one to commit, FearLvl1'],settings=settings,input_references_and_dependencies=sorted(set(e.get('Value') for e in xml.findall('.//FileRef/RelativePath') if e.get('Value'))),dependency_limits='Available collected samples archived; external preset/plugin files not copied. Current Fear set is a candidate source for FearLvl1; exact render linkage unverified.',origin_classification='User-supplied human composition; dependency origin and pre-jam content confirmation pending',license_and_attribution='No public license granted; sample/preset attribution and applicable terms pending confirmation',revision_history=['Original FearLvl1 render, current Fear Ableton set and collected samples preserved unchanged'],git_commit_hash=None,commit_lookup='git log --follow -- creative/provenance/MUS-FEARLVL1_milestone_001.json',sha256=files[0]['sha256'],files=files,integration_status='Source milestone; not an approved loop or integrated cue',validation='Full WAV payload read; source and snapshot hashes match. No listening, key estimate, true peak or loop-seam test performed.')
(dest/'SHA256SUMS.txt').write_text('\n'.join(f"{f['sha256']}  {f['snapshot']}" for f in files)+'\n',encoding='utf-8')
(root/'creative/provenance/MUS-FEARLVL1_milestone_001.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps(settings,indent=2)); print('Preserved files:',len(files));print('Render SHA256:',files[0]['sha256'])
