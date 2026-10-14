import json

output = []
with open(r'C:\Users\sonuk\.gemini\antigravity\brain\0b94f66f-5c44-478e-9d37-5034b7b80c20\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'replace_file_content' in line and 'bento' in line.lower():
            try:
                data = json.loads(line)
                if 'tool_calls' in data:
                    for tc in data['tool_calls']:
                        if tc['name'] == 'replace_file_content':
                            output.append(tc['args'])
            except:
                pass

with open('bento_replacements.json', 'w') as f:
    json.dump(output, f, indent=2)
