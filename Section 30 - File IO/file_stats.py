#write a function to count number of lines, words and characters in the text file

def statistics(file_name):
    with open(file_name) as file:
        statistics = {
            'lines': 0,
            'words': 0,
            'characters': 0
        }
        for line in file:
            #line = line.strip('\n')
            words = line.split()
            
            statistics['lines'] += 1
            statistics['words'] += len(words)
            statistics['characters'] += len(line)
            
    return statistics


def statistics_v2(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }