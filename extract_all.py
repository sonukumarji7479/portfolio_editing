import json

output = []
with open(r'C:\Users\sonuk\.gemini\antigravity\brain\0b94f66f-5c44-478e-9d37-5034b7b80c20\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'replace_file_content' in line:
            try:
                data = json.loads(line)
                created_at = data.get('created_at', '')
                if created_at:
                    time_str = created_at[11:16]
                    if '07:00' <= time_str <= '07:50':
                        if 'tool_calls' in data:
                            for tc in data['tool_calls']:
                                if tc['name'] == 'replace_file_content':
                                    output.append({
                                        'time': time_str,
                                        'file': tc['args'].get('TargetFile'),
                                        'instruction': tc['args'].get('Instruction'),
                                        'content': tc['args'].get('ReplacementContent')
                                    })
            except Exception as e:
                pass

with open('all_replacements.json', 'w') as f:
    json.dump(output, f, indent=2)
