import json

with open(r'C:\Users\sonuk\.gemini\antigravity\brain\0b94f66f-5c44-478e-9d37-5034b7b80c20\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f, open('all_html_edits.txt', 'w', encoding='utf-8') as out:
    for line in f:
        if 'replace_file_content' in line:
            try:
                data = json.loads(line)
                if 'tool_calls' in data:
                    for tc in data['tool_calls']:
                        if tc['name'] == 'replace_file_content':
                            args = tc['args']
                            if 'index.html' in args.get('TargetFile', ''):
                                out.write("=== EDIT ===\n")
                                out.write(f"Time: {data.get('created_at')}\n")
                                out.write(f"Instruction: {args.get('Instruction')}\n")
                                out.write("Replacement:\n")
                                out.write(args.get('ReplacementContent') + "\n\n")
            except Exception as e:
                pass
