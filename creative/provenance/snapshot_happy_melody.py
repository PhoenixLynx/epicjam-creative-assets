"""Preserve the first supplied happy render without changing working originals."""
from pathlib import Path
import datetime, gzip, hashlib, json, shutil, struct, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[2]
dest = root / 'creative/audio/source/MUS-001_happy_milestone_2026-11-15T020159Z'
dest.mkdir(parents=True, exist_ok=False)
render = root / 'OriginalCompositions/PhoenixLynx - Halycion_Melody_Positive_11-14_2026.wav'
project = root / 'Halycion Project'
inputs = [(render, dest / render.name), (project / 'Halycion_Melody_Positive.als', dest / 'Halycion Project/Halycion_Melody_Positive.als')]
inputs += [(p, dest / 'Halycion Project' / p.relative_to(project)) for p in (project / 'Samples').rglob('*') if p.is_file() and p.suffix.lower() in ('.aif','.aiff','.wav','.flac')]
files = []
for source, target in inputs:
    before = source.read_bytes()
    digest = hashlib.sha256(before).hexdigest()
    stat = source.stat()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(before)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
    assert hashlib.sha256(source.read_bytes()).hexdigest() == digest, 'Source changed during snapshot'
    files.append(dict(source=str(source.relative_to(root)), snapshot=str(target.relative_to(root)), sha256=digest, bytes=len(before), source_mtime_utc=datetime.datetime.fromtimestamp(stat.st_mtime,datetime.timezone.utc).isoformat()))
xml = ET.fromstring(gzip.decompress((dest / 'Halycion Project/Halycion_Melody_Positive.als').read_bytes()))
tempo = [e.attrib for e in xml.findall('.//Tempo/Manual')]
references = sorted(set(e.get('Value') for e in xml.findall('.//FileRef/RelativePath') if e.get('Value')))
record = dict(asset_id='MUS-001-HAPPY-RENDER-MILESTONE-001', descriptive_filename=str(render.relative_to(root)), purpose='Human original happy melody render; preserved source for later arrangement', human_contributors=['PhoenixLynx: user reports original composition and Ableton render'], ai_systems_and_tools=['Sol / ChatGPT: read-only inspection, byte-preserving snapshot, hashes and documentation; no music edits'], original_creation_utc=None, first_observed_utc='2026-11-15T02:01:59Z', observation_source='clock.curr_time tool during first file inventory', snapshot_recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), timestamp_limits='Observation time, not proof of composition date. Filesystem mtime is recorded metadata, not trusted creation evidence. No independent timestamp authority receipt obtained.', source_prompts=['User: I made an original melody happy render, it is a new folder; record a timestamp and supporting evidence.'], settings=dict(ableton_creator=xml.get('Creator'), tempo_manual_values=tempo, render_sample_rate_hz=44100, render_pcm_bits=16, channels=2, duration_seconds=16388132/176400), input_references_and_dependencies=references, dependency_limits='Collected samples preserved locally. Preset paths indicate dependencies but do not establish audible use or complete portability. External preset/plugin files not copied. Human attribution confirmation pending.', origin_classification='User-reported original human composition; instrument/sample/preset origins recorded separately and pending confirmation', license_and_attribution='No public license granted. Dependency rights not assessed; do not redistribute raw factory samples without confirming applicable terms.', revision_history=['First observed happy render and current Ableton set preserved unchanged; earlier source history retained'], git_commit_hash=None, files=files, integration_status='Source milestone preserved; not an approved loop or Unreal import. Current render differs from requested 48kHz/24-bit delivery spec.', unresolved=['Human BPM/key confirmation','Whether composition includes pre-jam material','Preset/sample/loop attribution','Musical feedback and arrangement direction after listening','External timestamp or remote snapshot receipt'])
out = root / 'creative/provenance/MUS-001_happy_milestone_001.json'
out.write_text(json.dumps(record,indent=2),encoding='utf-8')
manifest = '\n'.join(f"{f['sha256']}  {f['snapshot']}" for f in files)+'\n'
(dest / 'SHA256SUMS.txt').write_text(manifest,encoding='utf-8')
print(json.dumps(dict(snapshot=str(dest),files=len(files),tempo=tempo,render_sha256=files[0]['sha256'],record=str(out)),indent=2))
