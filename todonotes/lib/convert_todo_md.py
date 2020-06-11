import json

def main():
    fr = open('todo.md')
    notes = []
    note = {}
    for line in fr:
        if line.startswith('##'):
            title = line.strip().replace('## ', '')
            note = {'title': title, 'body': []}
        elif line.startswith(' -'):
            bodyItem = line.strip().replace('-', '')
            note['body'].append(bodyItem)
        elif line == '\n':
            notes.append(note)
    fr.close()
    
    json.dump(notes, open('todo.json', 'w'), indent=4, sort_keys=False)

if __name__ == '__main__':
    main()
