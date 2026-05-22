import os, glob

BASE = r'D:\Ginterma\Desktop\evaluation\evaluation\wavs'

# GT pervadinimas
GT_MAP = {
    'gt_lin': ('test-happy-', 'gt_lin_'),
    'gt_neu': ('test-neutral-', 'gt_neu_'),
    'gt_liu': ('test-sad-', 'gt_liu_'),
}

for folder, (old_prefix, new_prefix) in GT_MAP.items():
    wavs = sorted(glob.glob(f'{BASE}\\{folder}\\*.wav'))
    print(f'\n{folder}: {len(wavs)} failų')
    for i, w in enumerate(wavs, start=1):
        new_name = f'{new_prefix}{str(i).zfill(2)}.wav'
        new_path = os.path.join(BASE, folder, new_name)
        os.rename(w, new_path)
        print(f'  {os.path.basename(w)} → {new_name}')

# Sintezuotų pervadinimas (s11-s20 → 01-10)
SYNTH_FOLDERS = [
    'b1_lin', 'b1_neu', 'b1_liu',
    'b2_lin', 'b2_neu', 'b2_liu',
    'b3_lin', 'b3_neu', 'b3_liu',
    's_lin',  's_neu',  's_liu',
]

for folder in SYNTH_FOLDERS:
    wavs = sorted(glob.glob(f'{BASE}\\{folder}\\*.wav'))
    print(f'\n{folder}: {len(wavs)} failų')
    for i, w in enumerate(wavs, start=1):
        new_name = f'{folder}_{str(i).zfill(2)}.wav'
        new_path = os.path.join(BASE, folder, new_name)
        os.rename(w, new_path)
        print(f'  {os.path.basename(w)} → {new_name}')

print('\nViskas pervadinta ✓')