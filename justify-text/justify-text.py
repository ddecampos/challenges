class JustifyText():
    
    def __init__(self, text, length):
        self.text = text
        self.length = length
    
    def spaces_text(self, line, spaces):
        output_line = ''
        spaces_received = line.count('#')
        words = line.split('#')
        spaces_to_include = spaces_received + spaces
        i = 0
        
        # se retira de la lista los elementos vacios
        for index in range(len(words)):
            if words[index] == '':
                words.pop(index)

        while i < spaces_to_include:
            for j in range(len(words)):
                if words[j] != words[-1]:
                    words[j] += '*'
                    i += 1
                if i == spaces_to_include:
                    break

        output_line = ''.join(words)           

        return output_line
    
    def format_words(self):
        words = self.text.split(' ')
        output_text = ''
        line = ''

        for word in words:
            word_len = len(word)
            temp_sum = len(line) + word_len 
            line_len = len(line)
            

            if line_len < self.length:

                if temp_sum > self.length:
                    spaces = self.length - line_len
                    output_text += line + spaces * '*' + '\n'
                    line = ''
                    line += word + '#'
                elif temp_sum == self.length:
                    line += word
                    output_text += line + '\n'
                    line = ''
                    line += word + '#'
                else:
                    line += word + '#'
                    if word == words[-1]:
                        line = line[:-1]
                        output_text += line
            
            elif line_len == self.length:
                output_text += line + '\n'
                line = ''
                if temp_sum > self.length:
                    line += word + '#'

            
        return output_text

input_text = 'La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.'
obj = JustifyText(input_text,30)

print(obj.format_words())

